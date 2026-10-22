"""
Assessment wizard routes: Questionnaire submission, scoring, and results visualization.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, session, abort
from flask_login import current_user
from config import Config
from extensions import db
from models import Assessment, SkillProgress
from forms import CareerAssessmentForm
from engine.recommender import recommend_careers
from engine.ai_advisor import get_career_ai_advice
from engine.careers_data import get_career_by_key

assessment_bp = Blueprint("assessment", __name__)


def hydrate_results(results: dict) -> dict:
    """Ensure roadmap and learning resources are enriched from catalog."""
    if not results:
        return {}
    tc = results.get("top_career")
    if tc and "key" in tc:
        career_meta = get_career_by_key(tc["key"])
        if career_meta:
            if not tc.get("roadmap"):
                tc["roadmap"] = career_meta.get("roadmap", [])
            if not tc.get("resources"):
                tc["resources"] = career_meta.get("resources", [])
            if not tc.get("salary_range"):
                tc["salary_range"] = career_meta.get("salary_range", {})
    return results


def build_compact_payload(recommendation_data: dict, ai_advice: dict) -> dict:
    """Create an ultra-lightweight payload suitable for client session cookies without exceeding limits."""
    top_c = recommendation_data.get("top_career", {})
    compact_top = {
        "key": top_c.get("key"),
        "title": top_c.get("title"),
        "category": top_c.get("category"),
        "badge": top_c.get("badge"),
        "tagline": top_c.get("tagline"),
        "salary_range": top_c.get("salary_range"),
        "growth_rate": top_c.get("growth_rate"),
        "match_percentage": top_c.get("match_percentage"),
        "matched_core_skills": top_c.get("matched_core_skills", []),
        "missing_core_skills": top_c.get("missing_core_skills", []),
        "matched_secondary_skills": top_c.get("matched_secondary_skills", []),
        "missing_secondary_skills": top_c.get("missing_secondary_skills", []),
        "explanation": top_c.get("explanation"),
        "roles": top_c.get("roles", [])
    }

    recs = []
    for r in recommendation_data.get("recommendations", [])[:4]:
        recs.append({
            "key": r["key"],
            "title": r["title"],
            "category": r["category"],
            "salary_range": r["salary_range"],
            "match_percentage": r["match_percentage"],
            "tagline": r.get("tagline", "")
        })

    return {
        "top_career": compact_top,
        "recommendations": recs,
        "radar_dimensions": recommendation_data.get("radar_dimensions", {}),
        "overall_readiness_score": recommendation_data.get("overall_readiness_score", 50),
        "ai_advisor": ai_advice
    }


@assessment_bp.route("/assessment", methods=["GET", "POST"])
def wizard():
    """Interactive career assessment wizard questionnaire."""
    form = CareerAssessmentForm()

    if form.validate_on_submit():
        # Combine predefined selected skills with any custom skills entered by user
        selected_skills = list(form.skills.data or [])
        custom_skills_raw = request.form.get("custom_skills", "").strip()
        if custom_skills_raw:
            for item in custom_skills_raw.split(","):
                clean_item = item.strip()
                if clean_item and clean_item not in selected_skills:
                    selected_skills.append(clean_item)

        selected_interests = list(form.interests.data or [])
        custom_interests_raw = request.form.get("custom_interests", "").strip()
        if custom_interests_raw:
            for item in custom_interests_raw.split(","):
                clean_item = item.strip()
                if clean_item and clean_item not in selected_interests:
                    selected_interests.append(clean_item)

        # Run multi-factor recommendation engine
        recommendation_data = recommend_careers(
            user_skills=selected_skills,
            user_interests=selected_interests,
            user_work_style=form.work_style.data,
            user_experience=form.experience_years.data,
            user_education=form.education_level.data,
            user_goals=form.career_goals.data or "",
            top_n=5
        )

        top_career = recommendation_data.get("top_career")

        # Generate tailored executive advice
        ai_advice = get_career_ai_advice(
            top_career=top_career,
            user_skills=selected_skills,
            user_interests=selected_interests,
            user_experience=form.experience_years.data,
            user_goals=form.career_goals.data or "",
            api_key=Config.AI_API_KEY,
            provider=Config.AI_PROVIDER
        )

        stored_results = build_compact_payload(recommendation_data, ai_advice)

        # Save to database if user is authenticated
        if current_user.is_authenticated:
            assessment = Assessment(
                user_id=current_user.id,
                education_level=form.education_level.data,
                experience_years=form.experience_years.data,
                work_style=form.work_style.data,
                career_goals=form.career_goals.data or "",
                top_career_key=top_career.get("key") if top_career else "general",
                top_career_title=top_career.get("title") if top_career else "Tech Specialist",
                top_career_score=top_career.get("match_percentage", 50) if top_career else 50
            )
            assessment.primary_skills = selected_skills
            assessment.interests = selected_interests
            assessment.results = stored_results

            db.session.add(assessment)

            # Auto-seed initial missing skills into SkillProgress for user dashboard tracking
            if top_career and top_career.get("missing_core_skills"):
                for missing_skill in top_career["missing_core_skills"][:5]:
                    existing_skill = SkillProgress.query.filter_by(
                        user_id=current_user.id,
                        skill_name=missing_skill
                    ).first()
                    if not existing_skill:
                        new_skill_progress = SkillProgress(
                            user_id=current_user.id,
                            skill_name=missing_skill,
                            career_key=top_career["key"],
                            status="to_learn"
                        )
                        db.session.add(new_skill_progress)

            try:
                db.session.commit()
                flash("Assessment completed! Here are your personalized recommendations.", "success")
                return redirect(url_for("assessment.results_detail", assessment_id=assessment.id))
            except Exception:
                db.session.rollback()
                flash("Could not save assessment to database. Displaying results in session.", "warning")

        # Fallback for guests: store compact payload in session
        session["guest_assessment"] = stored_results
        session["guest_inputs"] = {
            "education": form.education_level.data,
            "experience": form.experience_years.data,
            "work_style": form.work_style.data,
            "skills": selected_skills,
            "interests": selected_interests,
            "goals": form.career_goals.data or ""
        }
        return redirect(url_for("assessment.results_guest"))

    return render_template("assessment/wizard.html", form=form)


@assessment_bp.route("/assessment/results/<int:assessment_id>")
def results_detail(assessment_id: int):
    """View saved assessment results for an authenticated user."""
    assessment = db.session.get(Assessment, assessment_id)
    if not assessment:
        abort(404)

    # Authorization check
    if current_user.is_authenticated and assessment.user_id != current_user.id:
        abort(403)

    hydrated = hydrate_results(assessment.results)

    return render_template(
        "assessment/results.html",
        results=hydrated,
        assessment=assessment,
        is_guest=False
    )


@assessment_bp.route("/assessment/results/latest")
def results_guest():
    """View results from current guest session."""
    results = session.get("guest_assessment")
    if not results:
        flash("No active assessment session found. Please take the assessment to view your results.", "info")
        return redirect(url_for("assessment.wizard"))

    hydrated = hydrate_results(results)

    return render_template(
        "assessment/results.html",
        results=hydrated,
        assessment=None,
        is_guest=True
    )
