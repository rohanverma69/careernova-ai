"""
Main website routes: Landing page, Career Catalog, and Career Details.
"""

from flask import Blueprint, render_template, abort, request
from engine.careers_data import get_all_careers, get_career_by_key

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@main_bp.route("/api/index")
@main_bp.route("/api/index/")
def index():
    """High-converting animated landing page."""
    featured_careers = get_all_careers()[:6]
    return render_template("index.html", featured_careers=featured_careers)


@main_bp.route("/careers")
def careers_list():
    """Browse all future-proof career paths with category filtering and search."""
    all_careers = get_all_careers()
    selected_category = request.args.get("category", "").strip()
    search_query = request.args.get("q", "").strip().lower()

    # Extract unique categories
    categories = sorted(list({c["category"] for c in all_careers}))

    filtered_careers = all_careers
    if selected_category:
        filtered_careers = [c for c in filtered_careers if c["category"] == selected_category]

    if search_query:
        filtered_careers = [
            c for c in filtered_careers
            if search_query in c["title"].lower()
            or search_query in c["tagline"].lower()
            or any(search_query in s.lower() for s in c["core_skills"])
        ]

    return render_template(
        "careers/index.html",
        careers=filtered_careers,
        categories=categories,
        selected_category=selected_category,
        search_query=search_query,
        total_careers=len(all_careers)
    )


@main_bp.route("/careers/<career_key>")
def career_detail(career_key: str):
    """Deep-dive profile for a specific career path with full roadmap and resources."""
    career = get_career_by_key(career_key)
    if not career:
        abort(404)

    # Suggest related careers in the same or adjacent categories
    all_careers = get_all_careers()
    related = [c for c in all_careers if c["key"] != career_key and c["category"] == career["category"]][:3]
    if len(related) < 3:
        related = [c for c in all_careers if c["key"] != career_key][:3]

    return render_template("careers/detail.html", career=career, related=related)


@main_bp.route("/about")
def about():
    """About CareerNova platform, methodology, and AI vision."""
    return render_template("about.html")
