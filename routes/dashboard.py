"""
Protected user dashboard: Overview, history, saved careers, and profile settings.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from extensions import db
from models import Assessment, SavedCareer, SkillProgress
from forms import ProfileSettingsForm
from engine.careers_data import get_career_by_key

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.route("/")
@login_required
def overview():
    """Main user dashboard overview."""
    # Fetch recent assessments
    assessments = Assessment.query.filter_by(user_id=current_user.id).order_by(
        Assessment.created_at.desc()
    ).limit(5).all()

    latest_assessment = assessments[0] if assessments else None

    # Fetch saved careers
    saved_careers = SavedCareer.query.filter_by(user_id=current_user.id).order_by(
        SavedCareer.created_at.desc()
    ).all()

    # Enrich saved careers with data from catalog
    enriched_saved = []
    for sc in saved_careers:
        career_meta = get_career_by_key(sc.career_key)
        enriched_saved.append({
            "record": sc,
            "meta": career_meta
        })

    # Fetch skill progresses
    skills = SkillProgress.query.filter_by(user_id=current_user.id).order_by(
        SkillProgress.updated_at.desc()
    ).all()

    skills_to_learn = [s for s in skills if s.status == "to_learn"]
    skills_in_progress = [s for s in skills if s.status == "in_progress"]
    skills_completed = [s for s in skills if s.status == "completed"]

    total_skills = len(skills) or 1
    mastery_percent = int((len(skills_completed) / total_skills) * 100) if skills else 0

    return render_template(
        "dashboard/index.html",
        latest_assessment=latest_assessment,
        assessments_count=len(assessments),
        saved_careers=enriched_saved,
        skills_to_learn=skills_to_learn,
        skills_in_progress=skills_in_progress,
        skills_completed=skills_completed,
        mastery_percent=mastery_percent
    )


@dashboard_bp.route("/history")
@login_required
def history():
    """Assessment history archive."""
    assessments = Assessment.query.filter_by(user_id=current_user.id).order_by(
        Assessment.created_at.desc()
    ).all()

    return render_template("dashboard/history.html", assessments=assessments)


@dashboard_bp.route("/saved")
@login_required
def saved_careers_list():
    """Bookmarked careers and roadmaps."""
    saved_records = SavedCareer.query.filter_by(user_id=current_user.id).order_by(
        SavedCareer.created_at.desc()
    ).all()

    enriched_saved = []
    for sc in saved_records:
        career_meta = get_career_by_key(sc.career_key)
        enriched_saved.append({
            "record": sc,
            "meta": career_meta
        })

    return render_template("dashboard/saved_careers.html", saved_careers=enriched_saved)


@dashboard_bp.route("/skills")
@login_required
def skills_board():
    """Interactive kanban-style skill acquisition tracker."""
    skills = SkillProgress.query.filter_by(user_id=current_user.id).all()

    to_learn = [s for s in skills if s.status == "to_learn"]
    in_progress = [s for s in skills if s.status == "in_progress"]
    completed = [s for s in skills if s.status == "completed"]

    return render_template(
        "dashboard/skills.html",
        to_learn=to_learn,
        in_progress=in_progress,
        completed=completed
    )


@dashboard_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """User profile and target career preferences settings."""
    form = ProfileSettingsForm(obj=current_user)

    if form.validate_on_submit():
        current_user.full_name = form.full_name.data.strip() if form.full_name.data else None
        current_user.target_role = form.target_role.data.strip() if form.target_role.data else None
        current_user.experience_level = form.experience_level.data
        current_user.bio = form.bio.data.strip() if form.bio.data else None

        try:
            db.session.commit()
            flash("Your profile settings have been updated successfully.", "success")
            return redirect(url_for("dashboard.profile"))
        except Exception as e:
            db.session.rollback()
            flash("Failed to update profile settings. Please try again.", "danger")

    return render_template("dashboard/profile.html", form=form)
