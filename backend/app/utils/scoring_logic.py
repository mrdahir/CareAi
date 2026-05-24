"""Scoring helpers for recommendation engine."""

from typing import Dict, List


def score_effectiveness(effectiveness: float, pregnancy_goals: str) -> float:
    if pregnancy_goals == "prevent_pregnancy":
        return min(30.0, effectiveness / 100 * 30)
    if pregnancy_goals == "space_children":
        return min(28.0, effectiveness / 100 * 28)
    return min(25.0, effectiveness / 100 * 25)


def score_side_effects(tolerance: List[str], method_side_effects: List[str]) -> float:
    if not tolerance:
        return 15.0
    bleeding_ok = "minimal_bleeding" in tolerance or "bleeding_ok" in tolerance
    hormones_ok = "hormones_preferred" in tolerance or "hormones_ok" in tolerance
    score = 10.0
    joined = " ".join(method_side_effects).lower()
    if bleeding_ok and "bleeding" in joined:
        score += 5
    if hormones_ok and "hormone" in joined:
        score += 5
    return min(20.0, score)


def score_cost(cost_sensitive: bool, method_cost: str) -> float:
    if not cost_sensitive:
        return 12.0
    return 15.0 if method_cost == "low" else (10.0 if method_cost == "medium" else 5.0)


def score_duration(pref: str, method_duration: str) -> float:
    mapping = {
        "short_term": ("weeks", "months", "daily", "3-months"),
        "medium": ("1-year", "3-years", "3-5 years"),
        "long_term": ("3-5 years", "5-years", "10-years", "years"),
        "permanent": ("permanent",),
    }
    targets = mapping.get(pref, ())
    md = method_duration.lower()
    if any(t in md for t in targets):
        return 15.0
    return 8.0


REGIONAL_POPULARITY: Dict[str, Dict[str, str]] = {
    "Kenya": {"implant": "35%", "iud": "12%", "pill": "28%", "injectable": "18%"},
    "Ethiopia": {"implant": "40%", "iud": "8%", "pill": "22%", "injectable": "20%"},
    "default": {"implant": "30%", "iud": "10%", "pill": "25%", "injectable": "15%"},
}
