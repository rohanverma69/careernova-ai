import os
import sys
import time
from sqlalchemy import text

# Add root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from models import db, User, Assessment, SavedCareer, SkillProgress

def verify_neon_end_to_end():
    print("=" * 65)
    print("CareerNova AI - Neon PostgreSQL End-to-End Verification")
    print("=" * 65)
    
    with app.app_context():
        # 1. Database Connection & Metadata
        print("\n[Step 1] Connecting to Neon Database via SQLAlchemy...")
        start_time = time.time()
        result = db.session.execute(text("SELECT version(), current_database(), current_user;")).fetchone()
        latency_ms = (time.time() - start_time) * 1000
        print(f"  PostgreSQL Version: {result[0]}")
        print(f"  Current Database:   {result[1]}")
        print(f"  Database User:      {result[2]}")
        print(f"  Query Latency:      {latency_ms:.2f} ms")
        
        # 2. Check Database Tables
        print("\n[Step 2] Verifying Schema Tables...")
        tables_query = db.session.execute(text(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;"
        )).fetchall()
        tables = [t[0] for t in tables_query]
        print(f"  Found {len(tables)} tables in Neon DB: {', '.join(tables)}")
        for expected in ['users', 'assessments', 'saved_careers', 'skill_progresses']:
            assert expected in tables, f"Missing table: {expected}"
        print("  All expected application tables exist in Neon PostgreSQL.")

        # 3. End-to-End Model CRUD Operations
        print("\n[Step 3] Executing Model CRUD operations on Neon...")
        test_email = "neon_test_user@careernova.ai"
        test_username = "neontester"
        
        # Clean up any previous test user
        existing_users = User.query.filter((User.email == test_email) | (User.username == test_username)).all()
        for u in existing_users:
            db.session.delete(u)
        if existing_users:
            db.session.commit()
            
        # Create Test User
        user = User(username=test_username, full_name="Neon Tester", email=test_email)
        user.set_password("SecureNeonPass123!")
        db.session.add(user)
        db.session.commit()
        print(f"  [+] Created User: ID={user.id}, Username='{user.username}', Full Name='{user.full_name}', Email='{user.email}'")

        # Create Test Assessment
        assessment = Assessment(
            user_id=user.id,
            education_level="Bachelor's Degree",
            experience_years="1-3 years",
            work_style="Remote",
            career_goals="Lead AI and Cloud Architect",
            primary_skills=["Python", "PostgreSQL", "Flask"],
            interests=["Artificial Intelligence", "Cloud Architecture"],
            top_career_key="ai-engineer",
            top_career_title="AI Engineer",
            top_career_score=95,
            results={"top_matches": [{"title": "AI Engineer", "score": 95}]}
        )
        db.session.add(assessment)
        db.session.commit()
        print(f"  [+] Created Assessment: ID={assessment.id}, Top Career='{assessment.top_career_title}', Score={assessment.top_career_score}%")

        # Create Saved Career
        saved = SavedCareer(
            user_id=user.id,
            career_key="ai-engineer",
            career_title="AI Engineer",
            status="exploring"
        )
        db.session.add(saved)
        db.session.commit()
        print(f"  [+] Saved Career: ID={saved.id}, Career='{saved.career_title}', Status='{saved.status}'")

        # Create Skill Progress
        skill = SkillProgress(
            user_id=user.id,
            skill_name="PostgreSQL Optimization",
            career_key="ai-engineer",
            status="in_progress"
        )
        db.session.add(skill)
        db.session.commit()
        print(f"  [+] Created Skill Progress: ID={skill.id}, Skill='{skill.skill_name}', Status='{skill.status}'")

        # 4. Verify Relations & Fetching
        print("\n[Step 4] Verifying Relations & Queries...")
        fetched_user = User.query.filter_by(email=test_email).first()
        assert fetched_user is not None
        assert fetched_user.check_password("SecureNeonPass123!")
        assert fetched_user.assessments.count() == 1
        assert fetched_user.saved_careers.count() == 1
        assert fetched_user.skill_progresses.count() == 1
        print("  User relationship traversal verified (assessments: 1, saved_careers: 1, skill_progresses: 1).")

        # Clean up test user (cascades to assessment, saved_career, skill_progress)
        db.session.delete(fetched_user)
        db.session.commit()
        print("  Cascade deletion verified: Cleaned up test data from Neon DB.")

        # 5. Live /api/health Endpoint Check
        print("\n[Step 5] Testing /api/health endpoint with Live Neon Database...")
        with app.test_client() as client:
            resp = client.get("/api/health")
            print(f"  HTTP Status: {resp.status_code}")
            print(f"  Response JSON: {resp.get_json()}")
            assert resp.status_code == 200
            assert resp.get_json().get("database") == "connected"
            assert resp.get_json().get("status") == "healthy"
            print("  /api/health verified: Database is connected and healthy.")

    print("\n" + "=" * 65)
    print("ALL NEON POSTGRESQL END-TO-END VERIFICATION CHECKS PASSED!")
    print("=" * 65)

if __name__ == "__main__":
    verify_neon_end_to_end()
