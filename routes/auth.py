"""
Authentication routes: Registration, Flexible Demo Login, and Logout.
Supports immediate access without email verification or OTP.
"""

import re
from urllib.parse import urlsplit
from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, current_user, login_required
from extensions import db
from models import User, Assessment
from forms import RegistrationForm, LoginForm

auth_bp = Blueprint("auth", __name__)

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def is_safe_redirect_url(target: str) -> bool:
    """Ensure redirect URL is strictly internal to prevent open redirect vulnerabilities."""
    if not target:
        return False
    ref_url = urlsplit(request.host_url)
    test_url = urlsplit(target)
    return test_url.scheme in ("", "http", "https") and (not test_url.netloc or test_url.netloc == ref_url.netloc)


def migrate_guest_assessment_if_present(user: User):
    """If guest took an assessment before logging in, link it to their new account and free cookie space."""
    guest_res = session.pop("guest_assessment", None)
    guest_inputs = session.pop("guest_inputs", None)

    if guest_res and not Assessment.query.filter_by(user_id=user.id).first():
        try:
            tc = guest_res.get("top_career", {})
            new_assessment = Assessment(
                user_id=user.id,
                education_level=guest_inputs.get("education", "Bachelor's Degree") if guest_inputs else "Bachelor's Degree",
                experience_years=guest_inputs.get("experience", "0-1 years") if guest_inputs else "0-1 years",
                work_style=guest_inputs.get("work_style", "Remote") if guest_inputs else "Remote",
                career_goals=guest_inputs.get("goals", "") if guest_inputs else "",
                top_career_key=tc.get("key", "general"),
                top_career_title=tc.get("title", "Tech Specialist"),
                top_career_score=tc.get("match_percentage", 50)
            )
            new_assessment.primary_skills = guest_inputs.get("skills", []) if guest_inputs else []
            new_assessment.interests = guest_inputs.get("interests", []) if guest_inputs else []
            new_assessment.results = guest_res
            db.session.add(new_assessment)
            db.session.commit()
        except Exception:
            db.session.rollback()


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """
    User registration view.
    Zero email verification required: immediately creates account and logs user in.
    """
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.overview"))

    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data.strip().lower()
        email = form.email.data.strip().lower()
        password = form.password.data
        full_name = form.full_name.data.strip() if form.full_name.data else None

        # Check if account with this email already exists (demo convenience)
        existing_by_email = User.query.filter_by(email=email).first()
        if existing_by_email:
            existing_by_email.set_password(password)
            if full_name:
                existing_by_email.full_name = full_name
            db.session.commit()
            login_user(existing_by_email, remember=True)
            migrate_guest_assessment_if_present(existing_by_email)
            flash(f"Welcome back, {existing_by_email.full_name or existing_by_email.username}! Signed in directly.", "success")
            return redirect(url_for("dashboard.overview"))

        # Create new user without requiring OTP or confirmation email
        user = User(
            username=username,
            email=email,
            full_name=full_name or username.replace("_", " ").title()
        )
        user.set_password(password)

        db.session.add(user)
        try:
            db.session.commit()
            login_user(user, remember=True)
            migrate_guest_assessment_if_present(user)
            flash(f"Welcome to CareerNova AI, {user.full_name or user.username}! Your account is active.", "success")
            return redirect(url_for("dashboard.overview"))
        except Exception:
            db.session.rollback()
            flash("An error occurred while creating your account. Please try again.", "danger")

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Flexible demo login view.
    Allows signing in with any valid email format and any password.
    If the account does not exist, automatically creates it on the fly!
    """
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.overview"))

    form = LoginForm()
    if request.method == "POST":
        login_id = (form.login_id.data or request.form.get("login_id", "")).strip().lower()
        password = form.password.data or request.form.get("password", "")

        # 1. Error Handling: check for empty fields
        if not login_id:
            flash("Email or username is required.", "danger")
            return render_template("auth/login.html", form=form)

        # 2. Error Handling: validate email format if an email string was entered
        if "@" in login_id and not re.match(EMAIL_REGEX, login_id):
            flash("Please enter a valid email format (e.g. demo@example.com).", "danger")
            return render_template("auth/login.html", form=form)

        if not password:
            flash("Password cannot be empty.", "danger")
            return render_template("auth/login.html", form=form)

        # 3. Flexible Authentication: check if user exists
        user = User.query.filter(
            (User.email == login_id) | (User.username == login_id)
        ).first()

        if user:
            # Existing user: update password or check match
            if user.check_password(password):
                login_user(user, remember=form.remember_me.data)
            else:
                # In demo mode, accept updated password so testers are never locked out
                user.set_password(password)
                db.session.commit()
                login_user(user, remember=form.remember_me.data)

            migrate_guest_assessment_if_present(user)
            flash(f"Welcome back, {user.full_name or user.username}! Signed in successfully.", "success")
        else:
            # Demo User Auto-Creation on the fly!
            # Allows users to log in with ANY test email and password
            if "@" in login_id:
                clean_prefix = login_id.split("@")[0].lower().replace(".", "_").replace("-", "_")
                base_username = "".join(c for c in clean_prefix if c.isalnum() or c == "_")
                if len(base_username) < 3:
                    base_username = "user_" + base_username
                email = login_id
            else:
                base_username = "".join(c for c in login_id.lower() if c.isalnum() or c == "_")
                if len(base_username) < 3:
                    base_username = "demo_user"
                email = f"{base_username}@careernova.local"

            # Ensure unique handle
            candidate_username = base_username[:25]
            counter = 1
            while User.query.filter_by(username=candidate_username).first():
                candidate_username = f"{base_username[:20]}_{counter}"
                counter += 1

            user = User(
                username=candidate_username,
                email=email,
                full_name=candidate_username.replace("_", " ").title()
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            login_user(user, remember=form.remember_me.data)
            migrate_guest_assessment_if_present(user)
            flash(f"Welcome, {user.full_name or user.username}! Demo account initialized and signed in.", "success")

        next_page = request.args.get("next")
        if next_page and is_safe_redirect_url(next_page):
            return redirect(next_page)
        return redirect(url_for("dashboard.overview"))

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    """Log out current user session safely."""
    logout_user()
    session.clear()
    flash("You have been signed out successfully.", "info")
    return redirect(url_for("main.index"))
