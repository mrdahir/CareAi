"""Chat API routes."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.chat_models import (
    ChatHistoryResponse,
    ChatRequest,
    ChatResponse,
    FeedbackRequest,
    FeedbackResponse,
)
from app.db.models import UserFeedback
from app.services.chat_service import ChatService
# from app.services.claude_service import get_claude_service
from app.services.llm_service import get_llm_service
from app.services.knowledge_base import get_knowledge_base
from app.utils.language_detection import detect_language

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest, db: AsyncSession = Depends(get_db)):
    service = ChatService(db)
    return await service.process_chat(request)


@router.post("/stream")
async def chat_stream(request: ChatRequest):
    lang = detect_language(request.message, request.language)
    kb = get_knowledge_base()
    context = kb.get_context_snippet(request.message, lang)
    llm = get_llm_service()

    async def event_generator():
        async for chunk in llm.stream_chat(
            request.message, context=context, language=lang
        ):
            yield chunk

    return StreamingResponse(event_generator(), media_type="text/plain")


@router.get("/history", response_model=ChatHistoryResponse)
async def chat_history(
    user_id: UUID = Query(...),
    limit: int = Query(10, ge=1, le=50),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    service = ChatService(db)
    return await service.get_history(user_id, limit=limit, offset=offset)


@router.post("/feedback", response_model=FeedbackResponse)
async def submit_feedback(
    request: FeedbackRequest, db: AsyncSession = Depends(get_db)
):
    fb = UserFeedback(
        user_id=request.user_id,
        message_id=request.message_id,
        rating=request.rating,
        feedback_text=request.feedback,
    )
    db.add(fb)
    await db.flush()
    return FeedbackResponse()
