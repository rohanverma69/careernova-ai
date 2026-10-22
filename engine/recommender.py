"""
Rule-Based Career Recommendation Engine for CareerNova AI.
Computes multi-dimensional alignment scores, transparent skill-gap analysis,
and structured personalized roadmaps.
"""

from typing import List, Dict, Any
from engine.careers_data import CAREERS_DATABASE, get_all_careers


def normalize_skill(skill: str) -> str:
    """Normalize skill name for case-insensitive and punctuation-agnostic comparison."""
    return skill.lower().replace("-", " ").replace("/", " ").replace(".", "").strip()


def is_skill_match(skill_a: str, skill_b: str) -> bool:
    """Check if two skills match via normalization or token overlap."""
    na = normalize_skill(skill_a)
    nb = normalize_skill(skill_b)
    if na == nb or na in nb or nb in na:
        return True
    # Check word token overlap (e.g. "JavaScript / TypeScript" with "JavaScript")
    tokens_a = set(na.split())
    tokens_b = set(nb.split())
    common = tokens_a.intersection(tokens_b) - {"and", "&", "or"}
    return len(common) > 0


def calculate_career_match(
    career: Dict[str, Any],
    user_skills: List[str],
    user_interests: List[str],
    user_work_style: str,
    user_experience: str,
    user_education: str,
    user_goals: str = ""
) -> Dict[str, Any]:
    """Calculate multi-dimensional alignment score between user and a career profile."""
    # 1. Core Skills Match
    matched_core = []
    missing_core = []
    for c_skill in career["core_skills"]:
        if any(is_skill_match(u_skill, c_skill) for u_skill in user_skills):
            matched_core.append(c_skill)
        else:
            missing_core.append(c_skill)

    # 2. Secondary Skills Match
    matched_secondary = []
    missing_secondary = []
    for s_skill in career["secondary_skills"]:
        if any(is_skill_match(u_skill, s_skill) for u_skill in user_skills):
            matched_secondary.append(s_skill)
        else:
            missing_secondary.append(s_skill)

    # Compute skill score component (Max: 55 points)
    # Each matched core skill yields up to 9.5 points (capped at 42)
    core_score = min(42.0, len(matched_core) * 9.5)
    # Secondary skills add up to 13 points (3.5 points each)
    secondary_score = min(13.0, len(matched_secondary) * 3.5)
    skill_score = core_score + secondary_score

    # 3. Interests Alignment (Max: 22 points)
    matched_interests = []
    for c_interest in career["interests"]:
        if any(is_skill_match(u_int, c_interest) for u_int in user_interests):
            matched_interests.append(c_interest)

    # Each strong matched domain interest contributes 11 points (up to 22)
    interest_score = min(22.0, len(matched_interests) * 11.0)

    # 4. Work Style Alignment (Max: 12 points)
    style_score = 5.0  # baseline
    norm_user_style = normalize_skill(user_work_style)
    for style in career["work_styles"]:
        if norm_user_style and (norm_user_style in normalize_skill(style) or normalize_skill(style) in norm_user_style):
            style_score = 12.0
            break

    # 5. Experience / Education baseline fit (Max: 9 points)
    exp_score = 7.0
    if "Entry" in user_experience or "0-1" in user_experience:
        exp_score = 8.0
    elif "2-4" in user_experience or "1-3" in user_experience:
        exp_score = 9.0
    elif "5+" in user_experience:
        exp_score = 9.0

    raw_total = skill_score + interest_score + style_score + exp_score
    # Clamp final percentage between 20% and 98%
    match_percentage = int(max(20, min(98, round(raw_total))))

    # Build transparent explanation
    explanation_parts = []
    if matched_core:
        explanation_parts.append(
            f"You demonstrate strong alignment with core competencies including {', '.join(matched_core[:3])}."
        )
    if matched_interests:
        explanation_parts.append(
            f"Your personal interest in {matched_interests[0]} directly mirrors this role's everyday mission."
        )
    if missing_core:
        explanation_parts.append(
            f"Focusing on high-leverage skills like {missing_core[0]} will significantly accelerate your market readiness."
        )
    if not matched_core and not matched_interests:
        explanation_parts.append(
            f"This career represents an exciting pivot opportunity. Prioritize Phase 1 of the roadmap to build foundational proficiency."
        )

    explanation = " ".join(explanation_parts)

    return {
        "key": career["key"],
        "title": career["title"],
        "category": career["category"],
        "badge": career["badge"],
        "tagline": career["tagline"],
        "description": career["description"],
        "salary_range": career["salary_range"],
        "growth_rate": career["growth_rate"],
        "match_percentage": match_percentage,
        "matched_core_skills": matched_core,
        "missing_core_skills": missing_core,
        "matched_secondary_skills": matched_secondary,
        "missing_secondary_skills": missing_secondary,
        "total_skills_matched": len(matched_core) + len(matched_secondary),
        "total_skills_missing": len(missing_core) + len(missing_secondary),
        "explanation": explanation,
        "roadmap": career["roadmap"],
        "resources": career["resources"],
        "roles": career["roles"]
    }


def compute_skill_radar_dimensions(user_skills: List[str]) -> Dict[str, int]:
    """Compute 6-dimensional skill readiness radar index (0-100) for charts."""
    norm_skills = {normalize_skill(s) for s in user_skills}

    dimensions = {
        "Software Engineering": ["python", "javascript", "typescript", "react", "node.js", "git", "html5", "css3", "solidity", "flutter"],
        "AI & Data Science": ["python", "machine learning", "pytorch", "tensorflow", "math & statistics", "deep learning", "pandas", "sql"],
        "Cloud & DevOps": ["docker", "kubernetes", "linux", "aws", "gcp", "terraform", "ci/cd", "bash", "prometheus"],
        "Security & Systems": ["network security", "ethical hacking", "linux", "cryptography", "wireshark", "owasp", "siem"],
        "Product & Strategy": ["product roadmap", "agile", "user research", "kpi", "prd writing", "a/b testing", "sql"],
        "UI/UX Design": ["figma", "wireframing", "design systems", "ui visual design", "usability testing", "html5"]
    }

    scores = {}
    for dim_name, domain_skills in dimensions.items():
        matches = sum(1 for ds in domain_skills if any(normalize_skill(ds) in s or s in normalize_skill(ds) for s in norm_skills))
        # Scale between 20 (base) and 95
        score = min(95, 20 + int((matches / len(domain_skills)) * 80))
        scores[dim_name] = score

    return scores


def recommend_careers(
    user_skills: List[str],
    user_interests: List[str],
    user_work_style: str,
    user_experience: str,
    user_education: str,
    user_goals: str = "",
    top_n: int = 5
) -> Dict[str, Any]:
    """
    Main recommendation routine: runs matching across the entire career database,
    ranks matches, generates skill gaps and readiness dimensions.
    """
    all_results = []
    for career in get_all_careers():
        match = calculate_career_match(
            career=career,
            user_skills=user_skills,
            user_interests=user_interests,
            user_work_style=user_work_style,
            user_experience=user_experience,
            user_education=user_education,
            user_goals=user_goals
        )
        all_results.append(match)

    # Sort descending by match percentage
    all_results.sort(key=lambda x: x["match_percentage"], reverse=True)

    top_matches = all_results[:top_n]
    radar_dimensions = compute_skill_radar_dimensions(user_skills)

    top_career = top_matches[0] if top_matches else None

    # Calculate overall profile readiness index
    avg_score = sum(m["match_percentage"] for m in top_matches) // len(top_matches) if top_matches else 50

    return {
        "top_career": top_career,
        "recommendations": top_matches,
        "all_scored": all_results,
        "radar_dimensions": radar_dimensions,
        "overall_readiness_score": avg_score,
        "total_evaluated_careers": len(all_results),
        "inputs_summary": {
            "skills_count": len(user_skills),
            "interests_count": len(user_interests),
            "experience": user_experience,
            "education": user_education,
            "work_style": user_work_style,
            "goals": user_goals
        }
    }
