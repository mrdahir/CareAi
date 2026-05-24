"""Recommendation API schemas."""

from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class RecommendRequest(BaseModel):
    user_id: Optional[UUID] = None
    age: int = Field(..., ge=15, le=49)
    breastfeeding: bool = False
    months_postpartum: int = Field(default=0, ge=0, le=24)
    pregnancy_goals: str = Field(
        default="space_children",
        pattern="^(space_children|prevent_pregnancy|flexible)$",
    )
    health_conditions: List[str] = []
    side_effect_tolerance: List[str] = []
    preferred_duration: str = Field(
        default="long_term",
        pattern="^(short_term|medium|long_term|permanent)$",
    )
    cost_sensitive: bool = False
    privacy_needed: bool = False
    region: str = "Kenya"
    language: str = Field(default="en", pattern="^(en|sw|am|fr|so)$")


class RecommendationItem(BaseModel):
    rank: int
    method: str
    method_id: str
    match_score: float
    effectiveness: str
    duration: str
    side_effects: str
    accessibility: str
    cost: str
    why_recommended: List[str]
    regional_popularity: Optional[str] = None
    key_reasons: List[str] = []
    next_steps: str = "Visit a clinic and discuss with a healthcare provider."


class RecommendResponse(BaseModel):
    recommendations: List[RecommendationItem]
    survey_questions_answered: int = 6
    disclaimer: str = (
        "Recommendations are informational. Always consult a qualified healthcare provider."
    )
