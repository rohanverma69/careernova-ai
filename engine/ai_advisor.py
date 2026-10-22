"""
AI Advisor integration for CareerNova AI.
Supports optional Google Gemini API or OpenAI compatible endpoints.
Provides intelligent, structured fallback advice when no AI API key is configured.
"""

import json
import logging
import urllib.request
import urllib.error
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


def generate_simulated_ai_insight(
    top_career: Dict[str, Any],
    user_skills: list,
    user_interests: list,
    user_experience: str,
    user_goals: str
) -> Dict[str, Any]:
    """
    Intelligent heuristic fallback advisor.
    Generates tailored career guidance, interview strategy, and 90-day action plan
    when no AI API key is configured in the environment.
    """
    title = top_career.get("title", "Software Specialist")
    matched_skills = top_career.get("matched_core_skills", [])
    missing_skills = top_career.get("missing_core_skills", [])
    salary = top_career.get("salary_range", {}).get("median", "$135,000")

    matched_txt = ", ".join(matched_skills[:3]) if matched_skills else "your versatile technical aptitude"
    priority_skill = missing_skills[0] if missing_skills else "system design and advanced production patterns"
    second_skill = missing_skills[1] if len(missing_skills) > 1 else "cloud infrastructure fundamentals"

    goals_clause = f" aligned with your goal to '{user_goals.strip()}'" if user_goals and user_goals.strip() else ""

    narrative = (
        f"Based on your profile ({user_experience} background), your strongest career convergence is as a **{title}**. "
        f"You already hold immediate leverage with {matched_txt}. By strategically targeting "
        f"**{priority_skill}** over the next 60 days, you can position yourself for median compensation packages around **{salary}**{goals_clause}."
    )

    action_plan = [
        {
            "days": "Days 1 - 30",
            "focus": f"Master {priority_skill}",
            "details": f"Dedicate 4-6 hours weekly to structured tutorials and build a focused prototype demonstrating practical {priority_skill} capability."
        },
        {
            "days": "Days 31 - 60",
            "focus": f"Portfolio Project & {second_skill}",
            "details": f"Synthesize your existing strengths in {matched_skills[0] if matched_skills else 'software'} with {priority_skill} into an open-source GitHub showcase with interactive demo."
        },
        {
            "days": "Days 61 - 90",
            "focus": "Interview Preparation & Targeted Outreach",
            "details": f"Prepare behavioral case studies, practice mock system design interviews, and connect with 5 senior {title} practitioners on LinkedIn."
        }
    ]

    interview_tip = (
        f"When interviewing for {title} roles, lead with how you solve ambiguity. "
        f"Be ready to articulate your mastery of {matched_skills[0] if matched_skills else 'core fundamentals'} and your rapid learning curve with {priority_skill}."
    )

    market_insight = (
        f"The {top_career.get('category', 'Technology')} sector is actively prioritizing engineers who combine "
        f"hands-on problem-solving with automated tooling. Your profile exhibits high adaptability."
    )

    return {
        "is_ai_generated": False,
        "provider": "CareerNova Rule-Based Intelligence Engine",
        "narrative": narrative,
        "action_plan": action_plan,
        "interview_tip": interview_tip,
        "market_insight": market_insight
    }


def call_gemini_api(api_key: str, prompt: str) -> Optional[str]:
    """Make lightweight REST call to Google Gemini 1.5 Flash API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "temperature": 0.4,
            "maxOutputTokens": 800,
            "responseMimeType": "application/json"
        }
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=6.0) as resp:
            body = resp.read().decode("utf-8")
            result = json.loads(body)
            candidates = result.get("candidates", [])
            if candidates:
                text_content = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                return text_content
    except Exception as e:
        logger.warning("Gemini API call failed: %s. Using rule-based fallback.", e)
        return None


def get_career_ai_advice(
    top_career: Dict[str, Any],
    user_skills: list,
    user_interests: list,
    user_experience: str,
    user_goals: str,
    api_key: Optional[str] = None,
    provider: str = "gemini"
) -> Dict[str, Any]:
    """
    Main AI advisor entry point.
    Attempts live LLM generation if API key is provided, or seamlessly falls back
    to rule-based heuristic synthesis.
    """
    if not api_key:
        return generate_simulated_ai_insight(
            top_career=top_career,
            user_skills=user_skills,
            user_interests=user_interests,
            user_experience=user_experience,
            user_goals=user_goals
        )

    # Prompt constructing structured JSON output
    prompt = f"""
You are CareerNova AI, an executive career counseling intelligence.
User Profile:
- Target Career Recommendation: {top_career.get('title')}
- Experience Level: {user_experience}
- Existing Skills: {', '.join(user_skills)}
- Interests: {', '.join(user_interests)}
- Career Goals: {user_goals or 'Accelerate career growth in modern tech'}
- Matched Skills: {', '.join(top_career.get('matched_core_skills', []))}
- Skills to Learn: {', '.join(top_career.get('missing_core_skills', []))}

Generate a JSON object matching this schema:
{{
  "narrative": "A high-impact 2-3 sentence personalized career recommendation narrative.",
  "action_plan": [
    {{"days": "Days 1 - 30", "focus": "Topic 1", "details": "Specific actionable milestone"}},
    {{"days": "Days 31 - 60", "focus": "Topic 2", "details": "Specific actionable milestone"}},
    {{"days": "Days 61 - 90", "focus": "Topic 3", "details": "Specific actionable milestone"}}
  ],
  "interview_tip": "One crisp high-value interview tip for this exact role.",
  "market_insight": "One concise sentence on current industry hiring demand."
}}
Return ONLY valid JSON.
"""

    raw_response = call_gemini_api(api_key, prompt)
    if raw_response:
        try:
            # Clean possible markdown fence if returned
            cleaned = raw_response.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            parsed = json.loads(cleaned.strip())
            parsed["is_ai_generated"] = True
            parsed["provider"] = "Google Gemini 1.5 Flash"
            return parsed
        except Exception as parse_err:
            logger.warning("Failed to parse AI response JSON: %s", parse_err)

    # Fallback if API fails or returns invalid format
    return generate_simulated_ai_insight(
        top_career=top_career,
        user_skills=user_skills,
        user_interests=user_interests,
        user_experience=user_experience,
        user_goals=user_goals
    )
