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
def test_breastfeeding_excludes_combined_pill_logic():
    engine = RecommendationEngine()
    req = RecommendRequest(
        age=25,
        breastfeeding=True,
        pregnancy_goals="space_children",
        preferred_duration="long_term",
        language="en",
    )
    result = engine.recommend(req)
    methods = [r.method_id for r in result.recommendations]
    assert "implant" in methods or "condom" in methods or "injectable" in methods
