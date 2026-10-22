"""
Automated tests for CareerNova Recommendation Engine & Skill-Gap Analysis.
"""

from engine.recommender import recommend_careers, compute_skill_radar_dimensions
from engine.careers_data import get_all_careers, get_career_by_key


def test_career_catalog_integrity():
    """Verify career database contains valid structures and required fields."""
    careers = get_all_careers()
    assert len(careers) >= 12

    for career in careers:
        assert "key" in career
        assert "title" in career
        assert "category" in career
        assert "salary_range" in career
        assert "core_skills" in career
        assert len(career["core_skills"]) >= 3
        assert "roadmap" in career
        assert len(career["roadmap"]) == 4


def test_ai_career_matching_accuracy():
    """Verify AI engineer skills yield AI/ML as top recommendation."""
    result = recommend_careers(
        user_skills=["Python", "Machine Learning", "PyTorch", "Math & Statistics"],
        user_interests=["Artificial Intelligence", "Neural Networks"],
        user_work_style="Analytical & Research-heavy",
        user_experience="0-1 years (Entry-Level)",
        user_education="Bachelor's Degree",
        user_goals="Become an AI Engineer"
    )

    top_career = result["top_career"]
    assert top_career is not None
    assert top_career["key"] == "ai_ml_engineer"
    assert top_career["match_percentage"] >= 70
    assert "Python" in top_career["matched_core_skills"]
    assert "PyTorch" in top_career["matched_core_skills"]


def test_full_stack_matching_accuracy():
    """Verify web dev skills yield Full-Stack Developer as top recommendation."""
    result = recommend_careers(
        user_skills=["JavaScript / TypeScript", "React", "Node.js", "HTML5 & CSS3"],
        user_interests=["Web Development", "Building Products"],
        user_work_style="Collaborative",
        user_experience="1-3 years (Junior)",
        user_education="Bootcamp",
        user_goals="Build scalable SaaS products"
    )

    top_career = result["top_career"]
    assert top_career is not None
    assert top_career["key"] == "full_stack_dev"
    assert top_career["match_percentage"] >= 70


def test_radar_dimension_bounds():
    """Ensure radar dimensions produce scores within 0-100 range."""
    dimensions = compute_skill_radar_dimensions(["python", "docker", "figma", "sql"])
    assert "Software Engineering" in dimensions
    assert "AI & Data Science" in dimensions
    assert "Cloud & DevOps" in dimensions
    assert "UI/UX Design" in dimensions

    for dim_name, score in dimensions.items():
        assert 0 <= score <= 100
