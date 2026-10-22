"""
Automated tests for AI Advisor fallback mechanism and response synthesis.
"""

from engine.ai_advisor import get_career_ai_advice, generate_simulated_ai_insight
from engine.careers_data import get_career_by_key


def test_ai_advisor_fallback_without_key():
    """Verify that when no AI API key is configured, advisor returns structured heuristic output."""
    career = get_career_by_key("ai_ml_engineer")
    assert career is not None

    advice = get_career_ai_advice(
        top_career=career,
        user_skills=["Python", "SQL"],
        user_interests=["Artificial Intelligence"],
        user_experience="0-1 years (Entry-Level)",
        user_goals="Target AI roles in 6 months",
        api_key=None
    )

    assert advice is not None
    assert advice["is_ai_generated"] is False
    assert "narrative" in advice
    assert len(advice["action_plan"]) == 3
    assert "interview_tip" in advice
    assert "market_insight" in advice

    # Check that narrative references key parameters
    assert "AI & Machine Learning Engineer" in advice["narrative"]
    assert "Days 1 - 30" in advice["action_plan"][0]["days"]


def test_simulated_insight_generation():
    """Verify generated simulated insights contain complete structure."""
    career = get_career_by_key("cybersecurity_engineer")
    insight = generate_simulated_ai_insight(
        top_career=career,
        user_skills=["Linux", "Network Security"],
        user_interests=["Cybersecurity"],
        user_experience="1-3 years",
        user_goals="Become an ethical hacker"
    )

    assert "narrative" in insight
    assert "Ethical Hacker" in insight["narrative"] or "Cybersecurity" in insight["narrative"]
    assert len(insight["action_plan"]) == 3
