"""
Automated tests for user authentication, registration, password hashing, and sessions.
Includes tests for flexible demo login without email verification.
"""

import pytest
from app import create_app
from extensions import db
from models import User
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


def test_password_hashing():
    """Verify passwords are secure and properly hashed with Scrypt."""
    user = User(username="security_tester", email="test@example.com")
    user.set_password("SuperSecretPass123")
    assert user.password_hash != "SuperSecretPass123"
    assert user.check_password("SuperSecretPass123") is True
    assert user.check_password("WrongPassword") is False


def test_user_registration(client, app):
    """Test user registration flow without requiring email verification."""
    response = client.post("/register", data={
        "username": "sarah_connor",
        "email": "sarah@cyberdyne.org",
        "full_name": "Sarah Connor",
        "password": "Password99!",
        "confirm_password": "Password99!"
    }, follow_redirects=True)

    assert response.status_code == 200
    with app.app_context():
        user = User.query.filter_by(username="sarah_connor").first()
        assert user is not None
        assert user.email == "sarah@cyberdyne.org"
        assert user.full_name == "Sarah Connor"


def test_duplicate_registration(client, app):
    """Ensure duplicate username is blocked with validation error."""
    with app.app_context():
        existing_user = User(username="existing_user", email="existing@example.com")
        existing_user.set_password("pass12345")
        db.session.add(existing_user)
        db.session.commit()

    # Attempt to register with same username
    response = client.post("/register", data={
        "username": "existing_user",
        "email": "different@example.com",
        "password": "Password99!",
        "confirm_password": "Password99!"
    })
    assert b"already taken" in response.data or b"Please choose another" in response.data


def test_login_flow(client, app):
    """Test login with email and with username."""
    with app.app_context():
        u = User(username="dev_ninja", email="ninja@example.com", full_name="Dev Ninja")
        u.set_password("ValidPassword123")
        db.session.add(u)
        db.session.commit()

    # Login with username
    login_resp = client.post("/login", data={
        "login_id": "dev_ninja",
        "password": "ValidPassword123"
    }, follow_redirects=True)
    assert login_resp.status_code == 200
    assert b"Welcome back" in login_resp.data

    # Log out
    logout_resp = client.get("/logout", follow_redirects=True)
    assert logout_resp.status_code == 200
    assert b"signed out successfully" in logout_resp.data

    # Login with email
    login_email_resp = client.post("/login", data={
        "login_id": "ninja@example.com",
        "password": "ValidPassword123"
    }, follow_redirects=True)
    assert login_email_resp.status_code == 200
    assert b"Welcome back" in login_email_resp.data


def test_flexible_demo_login_auto_creation(client, app):
    """Test flexible demo login: new fake/test credentials auto-create user and log in immediately."""
    response = client.post("/login", data={
        "login_id": "fresh_tester@fakecompany.org",
        "password": "anytestpassword123"
    }, follow_redirects=True)

    assert response.status_code == 200
    # Should redirect directly to dashboard
    assert b"Welcome" in response.data

    with app.app_context():
        created_user = User.query.filter_by(email="fresh_tester@fakecompany.org").first()
        assert created_user is not None
        assert created_user.check_password("anytestpassword123") is True


def test_login_validation_invalid_email(client):
    """Test login validation blocks invalid email format with clear message."""
    response = client.post("/login", data={
        "login_id": "invalid-email-format@",
        "password": "password123"
    })
    assert response.status_code == 200
    assert b"valid email format" in response.data


def test_login_validation_empty_password(client):
    """Test login validation blocks empty password with clear message."""
    response = client.post("/login", data={
        "login_id": "demo@example.com",
        "password": ""
    })
    assert response.status_code == 200
    assert b"Password cannot be empty" in response.data or b"required" in response.data


def test_protected_dashboard_redirects_unauthenticated(client):
    """Ensure accessing dashboard without login redirects to /login."""
    response = client.get("/dashboard/")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]
