"""
API endpoints: Health check, career bookmarking, and skill status toggles.
"""

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from sqlalchemy import text
from extensions import db
from models import SavedCareer, SkillProgress
from engine.careers_data import get_career_by_key

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint for Vercel and uptime monitors.
    Verifies application and database connectivity without exposing secrets.
    """
    db_status = "connected"
    http_code = 200

    try:
        # Lightweight ping to verify DB connection
        db.session.execute(text("SELECT 1"))
    except Exception:
        db_status = "unavailable"
        http_code = 503

    return jsonify({
        "status": "healthy" if db_status == "connected" else "degraded",
        "database": db_status,
        "service": "CareerNova AI Guidance Engine",
        "version": "1.0.0"
    }), http_code


@api_bp.route("/careers/toggle-save", methods=["POST"])
@login_required
def toggle_save_career():
    """Bookmark or unbookmark a career path for the authenticated user."""
    data = request.get_json(silent=True) or {}
    career_key = data.get("career_key", "").strip()

    if not career_key:
        return jsonify({"success": False, "error": "Career key is required"}), 400

    career_meta = get_career_by_key(career_key)
    career_title = career_meta["title"] if career_meta else career_key

    existing = SavedCareer.query.filter_by(
        user_id=current_user.id,
        career_key=career_key
    ).first()

    if existing:
        db.session.delete(existing)
        db.session.commit()
        return jsonify({
            "success": True,
            "saved": False,
            "message": f"Removed {career_title} from your saved roadmaps."
        })
    else:
        new_save = SavedCareer(
            user_id=current_user.id,
            career_key=career_key,
            career_title=career_title,
            status="exploring"
        )
        db.session.add(new_save)
        db.session.commit()
        return jsonify({
            "success": True,
            "saved": True,
            "message": f"Added {career_title} to your saved roadmaps!"
        })


@api_bp.route("/skills/update-status", methods=["POST"])
@login_required
def update_skill_status():
    """Update progress status of a tracked skill."""
    data = request.get_json(silent=True) or {}
    skill_name = data.get("skill_name", "").strip()
    status = data.get("status", "to_learn")
    career_key = data.get("career_key", "")

    if not skill_name:
        return jsonify({"success": False, "error": "Skill name is required"}), 400

    if status not in ("to_learn", "in_progress", "completed"):
        return jsonify({"success": False, "error": "Invalid status value"}), 400

    skill_record = SkillProgress.query.filter_by(
        user_id=current_user.id,
        skill_name=skill_name
    ).first()

    if not skill_record:
        skill_record = SkillProgress(
            user_id=current_user.id,
            skill_name=skill_name,
            career_key=career_key or None,
            status=status
        )
        db.session.add(skill_record)
    else:
        skill_record.status = status

    db.session.commit()

    return jsonify({
        "success": True,
        "skill_name": skill_name,
        "status": status,
        "message": f"Skill '{skill_name}' updated to {status.replace('_', ' ')}."
    })


@api_bp.route("/skills/delete", methods=["POST"])
@login_required
def delete_skill():
    """Remove a tracked skill from user progress."""
    data = request.get_json(silent=True) or {}
    skill_name = data.get("skill_name", "").strip()

    if not skill_name:
        return jsonify({"success": False, "error": "Skill name required"}), 400

    record = SkillProgress.query.filter_by(
        user_id=current_user.id,
        skill_name=skill_name
    ).first()

    if record:
        db.session.delete(record)
        db.session.commit()

    return jsonify({"success": True, "message": f"Removed '{skill_name}' from tracker."})
