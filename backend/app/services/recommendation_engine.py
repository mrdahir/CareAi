"""Contraceptive recommendation engine with rule-based scoring."""

from typing import Any, Dict, List

from app.models.recommend_models import RecommendRequest, RecommendationItem, RecommendResponse
from app.services.knowledge_base import get_knowledge_base
from app.services.programme_service import get_programme_stats, get_regional_method_shares
from app.utils.language_detection import pick_i18n
from app.utils.scoring_logic import (
    REGIONAL_POPULARITY,
    score_cost,
    score_duration,
    score_effectiveness,
    score_side_effects,
)

CONTRAINDICATION_MAP = {
    "hypertension": ["pill_combined", "patch"],
    "breast_cancer_history": ["pill", "implant", "injectable", "patch"],
    "liver_disease": ["pill", "implant"],
    "smoking_over_35": ["pill_combined"],
}


class RecommendationEngine:
    """Score and rank contraceptive methods for a user profile."""

    def __init__(self) -> None:
        self.kb = get_knowledge_base()

    def recommend(self, req: RecommendRequest) -> RecommendResponse:
        methods = self.kb._methods
        scored: List[Dict[str, Any]] = []

        for raw in methods:
            method = self.kb._format_method(raw, req.language)
            if self._is_contraindicated(method, req):
                continue
            if req.breastfeeding and "combined" in method["id"]:
                continue
            if not self._duration_matches(req.preferred_duration, method):
                continue

            score = (
                score_effectiveness(method["effectiveness"], req.pregnancy_goals)
                + score_side_effects(req.side_effect_tolerance, method["side_effects"])
                + score_cost(req.cost_sensitive, method["cost"])
                + score_duration(req.preferred_duration, method["duration"])
                + self._accessibility_score(method, req)
                + self._breastfeeding_bonus(method, req)
            )
            scored.append({"method": method, "score": score})

        scored.sort(key=lambda x: x["score"], reverse=True)
        top = scored[:3]
        region_stats = dict(
            REGIONAL_POPULARITY.get(req.region, REGIONAL_POPULARITY["default"])
        )
        wk_shares = get_regional_method_shares(req.region)
        for method_id, share in wk_shares.items():
            region_stats[method_id] = share

        recommendations: List[RecommendationItem] = []
        for rank, item in enumerate(top, start=1):
            m = item["method"]
            pop = region_stats.get(m["id"], "widely used in your region")
            reasons = self._build_reasons(m, req)
            recommendations.append(
                RecommendationItem(
                    rank=rank,
                    method=m["name"],
                    method_id=m["id"],
                    match_score=round(min(100, item["score"]), 1),
                    effectiveness=f"{m['effectiveness']}%",
                    duration=m["duration"],
                    side_effects=", ".join(m["side_effects"][:2]) or "Varies by individual",
                    accessibility=m["accessibility"],
                    cost=m["cost"],
                    why_recommended=reasons,
                    key_reasons=reasons[:4],
                    regional_popularity=f"Used by {pop} of clients in Western Kenya programme data"
                    if wk_shares.get(m["id"])
                    else f"Used by {pop} of women in your area",
                )
            )

        if not recommendations:
            fallback = self.kb.get_method_by_id("condom", req.language)
            if fallback:
                recommendations.append(
                    RecommendationItem(
                        rank=1,
                        method=fallback["name"],
                        method_id=fallback["id"],
                        match_score=70.0,
                        effectiveness=f"{fallback['effectiveness']}%",
                        duration=fallback["duration"],
                        side_effects="Generally minimal",
                        accessibility=fallback["accessibility"],
                        cost=fallback["cost"],
                        why_recommended=["Widely available", "No hormones", "Safe while breastfeeding"],
                        regional_popularity="Available over the counter",
                    )
                )

        return RecommendResponse(recommendations=recommendations)

    def _is_contraindicated(self, method: Dict[str, Any], req: RecommendRequest) -> bool:
        mid = method["id"]
        for condition in req.health_conditions:
            blocked = CONTRAINDICATION_MAP.get(condition.lower().replace(" ", "_"), [])
            if any(b in mid for b in blocked):
                return True
            if condition.lower() in [c.lower() for c in method.get("contraindications", [])]:
                return True
        return False

    def _duration_matches(self, pref: str, method: Dict[str, Any]) -> bool:
        cat = method.get("duration_category", "long_term")
        if pref == "flexible":
            return True
        if pref == "permanent":
            return cat == "permanent"
        return cat == pref or cat in ("medium", "long_term")

    def _accessibility_score(self, method: Dict[str, Any], req: RecommendRequest) -> float:
        if req.privacy_needed and method["accessibility"] == "available_ota":
            return 18.0
        if method["accessibility"] == "clinic_only":
            return 12.0
        return 15.0

    def _breastfeeding_bonus(self, method: Dict[str, Any], req: RecommendRequest) -> float:
        if not req.breastfeeding:
            return 0.0
        best_for = method.get("best_for", [])
        if any("breastfeeding" in tag for tag in best_for):
            return 10.0
        if method["id"] in ("implant", "iud", "condom", "injectable"):
            return 8.0
        return 0.0

    def _build_reasons(self, method: Dict[str, Any], req: RecommendRequest) -> List[str]:
        reasons = [
            f"{method['effectiveness']}% effective for pregnancy prevention",
            f"Duration: {method['duration']}",
        ]
        if req.breastfeeding:
            reasons.append("Compatible with breastfeeding when clinically appropriate")
        if req.pregnancy_goals == "space_children":
            reasons.append("Supports healthy child spacing")
        if method["cost"] == "low":
            reasons.append("Low cost option")
        return reasons


def get_recommendation_engine() -> RecommendationEngine:
    return RecommendationEngine()
