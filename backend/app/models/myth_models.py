"""Myth-check and FAQ API schemas."""

from typing import List, Optional

from pydantic import BaseModel, Field


class MythCheckRequest(BaseModel):
    statement: str = Field(..., min_length=3, max_length=1000)
    language: str = Field(default="en", pattern="^(en|sw|am|fr|so)$")


class MythCheckResponse(BaseModel):
    is_myth: bool
    severity: str = "medium"
    myth: str
    fact: str
    evidence: str
    sources: List[str] = []
    similar_myths: List[str] = []
    confidence: float = Field(default=0.9, ge=0, le=1)


class FAQRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=500)
    language: str = Field(default="en", pattern="^(en|sw|am|fr|so)$")
    category: Optional[str] = None


class FAQResponse(BaseModel):
    question: str
    answer: str
    related_faqs: List[str] = []
    sources: List[str] = []
    find_clinic: str = "Visit your nearest health facility for personalized care."


class ContraceptiveMethodOut(BaseModel):
    id: str
    name: str
    description: str
    effectiveness: float
    duration: str
    side_effects: List[str] = []
    accessibility: str
    cost: str = "low"


class ContraceptivesListResponse(BaseModel):
    methods: List[ContraceptiveMethodOut]
