"""
Integration tests for core Flask application routes, health check, and static assets.
"""

import pytest
from app import create_app
from extensions import db
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


def test_homepage_loads(client):
    """Test landing page returns HTTP 200 and brand title."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"CareerNova" in response.data
    assert b"Navigate Your Next" in response.data


def test_careers_list_route(client):
    """Test career library view returns HTTP 200 and career cards."""
    response = client.get("/careers")
    assert response.status_code == 200
    assert b"Future-Proof Tech Career Library" in response.data
    assert b"AI &amp; Machine Learning Engineer" in response.data or b"AI & Machine Learning" in response.data


def test_career_detail_valid(client):
    """Test deep-dive career profile page for valid career key."""
    response = client.get("/careers/ai_ml_engineer")
    assert response.status_code == 200
    assert b"AI &amp; Machine Learning Engineer" in response.data or b"AI & Machine Learning" in response.data
    assert b"4-Phase Professional Roadmap" in response.data


def test_career_detail_invalid(client):
    """Test invalid career key returns 404."""
    response = client.get("/careers/non_existent_career_role_123")
    assert response.status_code == 404
    assert b"404" in response.data


def test_about_route(client):
    """Test methodology/about page."""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"How CareerNova AI Operates" in response.data


def test_health_check_endpoint(client):
    """Test /api/health returns 200 and healthy DB status."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["database"] == "connected"
    assert data["version"] == "1.0.0"


def test_static_assets(client):
    """Verify core static CSS, JS, and image assets load successfully."""
    css_res = client.get("/static/css/style.css")
    assert css_res.status_code == 200
    assert b"--bg-cosmos" in css_res.data

    anim_res = client.get("/static/css/animations.css")
    assert anim_res.status_code == 200

    js_res = client.get("/static/js/main.js")
    assert js_res.status_code == 200

    icon_res = client.get("/static/images/favicon.svg")
    assert icon_res.status_code == 200
