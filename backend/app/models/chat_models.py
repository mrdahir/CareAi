"""Chat API request/response schemas."""

from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ChatContext(BaseModel):
    age: Optional[int] = None
    breastfeeding: Optional[bool] = None


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    user_id: Optional[UUID] = None
    language: str = Field(default="en", pattern="^(en|sw|am|fr|so)$")
    context: Optional[ChatContext] = None


class ChatResponse(BaseModel):
    response_id: UUID
    message: str
    sources: List[str] = []
    confidence: float = Field(ge=0, le=1)
    follow_up_suggestions: List[str] = []
    tokens_used: int = 0
    language_detected: str = "en"
    disclaimer: str = (
        "This information is educational only. Consult a healthcare provider for medical advice."
    )


class ChatHistoryItem(BaseModel):
    message_id: UUID
    user_message: str
    ai_response: str
    created_at: str


class ChatHistoryResponse(BaseModel):
    messages: List[ChatHistoryItem]
    total_count: int


class FeedbackRequest(BaseModel):
    message_id: UUID
    rating: int = Field(..., ge=1, le=5)
    feedback: Optional[str] = None
    user_id: Optional[UUID] = None


class FeedbackResponse(BaseModel):
    status: str = "success"
