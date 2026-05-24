"""Recommendation API routes."""

from fastapi import APIRouter

from app.models.recommend_models import RecommendRequest, RecommendResponse
from app.services.recommendation_engine import get_recommendation_engine

router = APIRouter(prefix="/recommend", tags=["recommend"])


@router.post("", response_model=RecommendResponse)
async def recommend(request: RecommendRequest):
    engine = get_recommendation_engine()
    return engine.recommend(request)
