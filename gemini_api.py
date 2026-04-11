"""
gemini_api.py
AI integration using Groq API (free tier)
Model: llama-3.3-70b-versatile
LexMatch AI — Hackathon 2026
"""

from groq import Groq
import json

# ── Paste your Groq API key here ──────────────────────────────
# Get free key at: https://console.groq.com
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)
MODEL  = "llama-3.3-70b-versatile"


def call_groq(prompt: str, max_tokens: int = 1000) -> str:
    """Core function to call Groq API."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def analyze_case(user_case: str, category: str, local_cases: list) -> dict:
    """
    Full AI legal assessment of user's case.
    Returns structured JSON with strength, law, outcome, action.
    """
    case_summaries = "\n".join([
        f"{i+1}. {c['title']} ({c.get('year','N/A')}, {c.get('court','N/A')}): "
        f"{c.get('summary','')[:150]} → Outcome: {c.get('outcome','N/A')}"
        for i, c in enumerate(local_cases[:5])
    ])

    prompt = f"""You are a senior Indian legal advocate with 20 years of experience in {category} law.

A client has described their case:
"{user_case}"

Most similar local cases from database:
{case_summaries}

Provide your expert assessment. Return ONLY valid JSON — no markdown, no backticks, no extra text:
{{
  "caseStrength": "Strong",
  "strengthScore": 75,
  "strengthReason": "one clear sentence explaining why this case is strong or weak",
  "relevantLaw": "Most applicable Indian law, IPC section, or Act with section number",
  "likelyOutcome": "one sentence prediction of most probable outcome",
  "urgentAction": "the single most important thing the client must do right now",
  "timeline": "estimated realistic time to resolution",
  "summary": "2 professional sentences summarizing the case assessment",
  "riskFactors": ["specific risk 1", "specific risk 2", "specific risk 3"]
}}"""

    result  = call_groq(prompt, max_tokens=800)
    cleaned = result.replace("```json", "").replace("```", "").strip()

    # Find JSON object in response
    start = cleaned.find("{")
    end   = cleaned.rfind("}") + 1
    if start != -1 and end > start:
        cleaned = cleaned[start:end]

    try:
        return json.loads(cleaned)
    except Exception:
        return {
            "caseStrength":   "Moderate",
            "strengthScore":  60,
            "strengthReason": "Assessment generated — consult a lawyer for full evaluation.",
            "relevantLaw":    "Consult advocate for specific sections",
            "likelyOutcome":  "Outcome depends on evidence and legal representation.",
            "urgentAction":   "Consult a qualified advocate immediately.",
            "timeline":       "6-18 months depending on court",
            "summary":        "Your case has been analyzed. Please consult a verified Patna advocate for detailed guidance.",
            "riskFactors":    ["Insufficient documentation may weaken case", "Timeline delays possible", "Evidence must be properly preserved"],
        }


def score_matches(user_case: str, local_cases: list) -> list:
    """
    Score each local case against user case description.
    Returns list of {index, score, reason}.
    """
    case_list = "\n".join([
        f'{i}: title="{c["title"]}" '
        f'facts="{", ".join(c.get("key_facts", []))}" '
        f'summary="{c.get("summary","")[:100]}"'
        for i, c in enumerate(local_cases)
    ])

    prompt = f"""You are a legal case matching AI.

User's case: "{user_case}"

Local cases to score:
{case_list}

Score each case 0-100 based on similarity to the user's case.
Consider: legal category, facts, type of dispute, parties involved.

Return ONLY a valid JSON array — no markdown, no backticks:
[{{"index": 0, "score": 85, "reason": "Both involve corporate fraud with forged documents"}},
 {{"index": 1, "score": 30, "reason": "Different area of law"}},
 ...include ALL {len(local_cases)} cases]"""

    result  = call_groq(prompt, max_tokens=1200)
    cleaned = result.replace("```json", "").replace("```", "").strip()

    # Find JSON array
    start = cleaned.find("[")
    end   = cleaned.rfind("]") + 1
    if start != -1 and end > start:
        cleaned = cleaned[start:end]

    try:
        scores = json.loads(cleaned)
        # Fill missing indices with default score
        scored_indices = {s["index"] for s in scores}
        for i in range(len(local_cases)):
            if i not in scored_indices:
                scores.append({"index": i, "score": 5, "reason": "Different legal area"})
        return scores
    except Exception:
        # Fallback: return default scores
        return [{"index": i, "score": 10, "reason": "Unable to score"} for i in range(len(local_cases))]


def detect_category(case_text: str) -> str:
    """Auto-detect legal category from case description."""
    prompt = f"""Read this legal case and return ONLY one word from this list:
criminal, civil, family, corporate, constitutional, environmental

Case: "{case_text}"

Return exactly one word only, nothing else:"""

    result = call_groq(prompt, max_tokens=10)
    word   = result.strip().lower().split()[0] if result.strip() else "civil"
    valid  = ["criminal", "civil", "family", "corporate", "constitutional", "environmental"]
    return word if word in valid else "civil"


def ask_legal_question(question: str) -> str:
    """Answer any question about Indian law in plain language."""
    prompt = f"""You are an expert Indian legal consultant with 25 years of experience.

A citizen asks: "{question}"

Provide a comprehensive, helpful answer. Use clear section headings. Cover:
1. **Direct Answer** — answer their question immediately
2. **Relevant Laws & Sections** — specific IPC/CrPC/Acts that apply
3. **Your Legal Rights** — what rights they have in this situation
4. **Step-by-Step Process** — exactly what to do
5. **Documents Needed** — what evidence/paperwork is required
6. **Timeline & Costs** — realistic expectations
7. **Important Warning** — one critical caution

Write in simple Hindi-friendly English. No complex legal jargon.
Be specific, practical, and actionable. Cite exact section numbers."""

    return call_groq(prompt, max_tokens=1500)
