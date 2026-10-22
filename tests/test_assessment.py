"""
Integration tests for assessment submission, results display, and dashboard interactions.
"""

import pytest
from app import create_app
from extensions import db
from models import User, Assessment, SavedCareer, SkillProgress
from config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_guest_assessment_submission(client):
    """Test guest assessment submission flows into session and renders results."""
    resp = client.post("/assessment", data={
        "education_level": "Bachelor's Degree",
        "experience_years": "0-1 years (Entry-Level)",
        "work_style": "Analytical & Research-heavy",
        "skills": ["Python", "Machine Learning", "PyTorch"],
        "interests": ["Artificial Intelligence"],
        "career_goals": "Master AI agents"
    }, follow_redirects=True)

    assert resp.status_code == 200
    assert b"AI &amp; Machine Learning Engineer" in resp.data or b"AI & Machine Learning" in resp.data
    assert b"Temporary Guest Session" in resp.data


def test_authenticated_assessment_submission(client, app):
    """Test logged-in user assessment saves to DB and auto-populates skill progress."""
    # 1. Create and login user
    with app.app_context():
        u = User(username="test_scholar", email="scholar@example.com")
        u.set_password("pass12345")
        db.session.add(u)
        db.session.commit()
        u_id = u.id

    client.post("/login", data={"login_id": "test_scholar", "password": "pass12345"})

    # 2. Submit assessment
    resp = client.post("/assessment", data={
        "education_level": "Master's / Postgraduate",
        "experience_years": "1-3 years (Junior)",
        "work_style": "Collaborative & Fast-paced",
        "skills": ["JavaScript / TypeScript", "React", "Node.js"],
        "interests": ["Web Development", "Building Products"],
        "career_goals": "Scale high-availability web apps"
    }, follow_redirects=True)

    assert resp.status_code == 200
    assert b"Full-Stack Web Developer" in resp.data

    # Verify database persistence
    with app.app_context():
        saved_assessment = Assessment.query.filter_by(user_id=u_id).first()
        assert saved_assessment is not None
        assert saved_assessment.top_career_key == "full_stack_dev"
        assert saved_assessment.top_career_score > 60

        # Verify auto-seeded missing skills in SkillProgress
        progress_items = SkillProgress.query.filter_by(user_id=u_id).all()
        assert len(progress_items) > 0


def test_api_career_save_and_toggle(client, app):
    """Test saving and unsaving career bookmarks via API endpoint."""
    with app.app_context():
        u = User(username="career_saver", email="saver@example.com")
        u.set_password("pass12345")
        db.session.add(u)
        db.session.commit()
        u_id = u.id

    # Try saving when unauthenticated -> 302 or 401
    unauth_resp = client.post("/api/careers/toggle-save", json={"career_key": "ai_ml_engineer"})
    assert unauth_resp.status_code in (302, 401)

    # Login
    client.post("/login", data={"login_id": "career_saver", "password": "pass12345"})

    # Save career
    save_resp = client.post("/api/careers/toggle-save", json={"career_key": "ai_ml_engineer"})
    assert save_resp.status_code == 200
    assert save_resp.get_json()["saved"] is True

    # Check DB
    with app.app_context():
        bookmark = SavedCareer.query.filter_by(user_id=u_id, career_key="ai_ml_engineer").first()
        assert bookmark is not None

    # Toggle again -> should remove bookmark
    toggle_resp = client.post("/api/careers/toggle-save", json={"career_key": "ai_ml_engineer"})
    assert toggle_resp.status_code == 200
    assert toggle_resp.get_json()["saved"] is False

    with app.app_context():
        bookmark_deleted = SavedCareer.query.filter_by(user_id=u_id, career_key="ai_ml_engineer").first()
        assert bookmark_deleted is None


def test_api_skill_status_update(client, app):
    """Test updating skill progress status via API endpoint."""
    with app.app_context():
        u = User(username="skill_master", email="master@example.com")
        u.set_password("pass12345")
        db.session.add(u)
        db.session.commit()
        u_id = u.id

    client.post("/login", data={"login_id": "skill_master", "password": "pass12345"})

    # Update to 'in_progress'
    update_resp = client.post("/api/skills/update-status", json={
        "skill_name": "Kubernetes",
        "status": "in_progress",
        "career_key": "cloud_devops_architect"
    })
    assert update_resp.status_code == 200
    assert update_resp.get_json()["status"] == "in_progress"

    # Check DB
    with app.app_context():
        skill_item = SkillProgress.query.filter_by(user_id=u_id, skill_name="Kubernetes").first()
        assert skill_item is not None
        assert skill_item.status == "in_progress"
