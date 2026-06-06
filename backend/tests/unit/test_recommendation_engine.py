"""Unit tests for recommendation engine."""

import pytest

from app.models.recommend_models import RecommendRequest
from app.services.recommendation_engine import RecommendationEngine


@pytest.mark.unit
def test_recommend_returns_top_methods():
    engine = RecommendationEngine()
    req = RecommendRequest(
        age=28,
        breastfeeding=False,
        pregnancy_goals="space_children",
        preferred_duration="long_term",
        region="Kenya",
        language="en",
    )
    result = engine.recommend(req)
    assert len(result.recommendations) >= 1
    assert result.recommendations[0].match_score > 0


@pytest.mark.unit
def test_breastfeeding_bonus_applied_to_lactation_compatible_methods():
    engine = RecommendationEngine()
    req = RecommendRequest(
        age=25,
        breastfeeding=True,
        pregnancy_goals="space_children",
        preferred_duration="long_term",
        language="en",
    )
    no_bf = RecommendRequest(
        age=25,
        breastfeeding=False,
        pregnancy_goals="space_children",
        preferred_duration="long_term",
        language="en",
    )
    bf_result = engine.recommend(req)
    no_bf_result = engine.recommend(no_bf)
    bf_implant = next(
        (r for r in bf_result.recommendations if r.method_id == "implant"), None
    )
    no_bf_implant = next(
        (r for r in no_bf_result.recommendations if r.method_id == "implant"), None
    )
    assert bf_implant is not None and no_bf_implant is not None
    assert bf_implant.match_score >= no_bf_implant.match_score
