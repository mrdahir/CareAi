"""Chat business logic."""

import uuid
from typing import Optional
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.chat_models import ChatHistoryItem, ChatHistoryResponse, ChatRequest, ChatResponse
from app.db.models import ChatMessage, User
# from app.services.claude_service import get_claude_service
from app.services.llm_service import get_llm_service
from app.services.knowledge_base import get_knowledge_base
from app.services.programme_service import get_programme_context_snippet
from app.utils.language_detection import detect_language, get_follow_up_suggestions


class ChatService:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db
        self.llm = get_llm_service()
        self.kb = get_knowledge_base()

    async def process_chat(self, req: ChatRequest) -> ChatResponse:
        lang = detect_language(req.message, req.language)
        context = self.kb.get_context_snippet(req.message, lang)
        msg_lower = req.message.lower()
        if any(
            k in msg_lower
            for k in ("kenya", "busia", "siaya", "bondo", "western", "msk", "programme")
        ):
            prog = get_programme_context_snippet(req.message, region="Kenya")
            if prog:
                context = f"{context}\n\n{prog}".strip() if context else prog
        response_text, tokens = await self.llm.complete(
            req.message, context=context, language=lang
        )

        sources = []
        if context:
            sources.extend(["WHO_2022_contraceptive_methods", "CareApp_Knowledge_Base"])
        myth = self.kb.find_myth(req.message, lang)
        if myth:
            sources.extend(myth.get("sources", []))

        user_id = req.user_id
        if user_id is None:
            user = User(language=lang)
            self.db.add(user)
            await self.db.flush()
            user_id = user.id

        msg = ChatMessage(
            user_id=user_id,
            message_text=req.message,
            ai_response=response_text,
            language_detected=lang,
            tokens_used=tokens,
            sources=sources,
        )
        self.db.add(msg)
        await self.db.flush()

        return ChatResponse(
            response_id=msg.id,
            message=response_text,
            sources=sources,
            confidence=0.92 if context else 0.75,
            follow_up_suggestions=get_follow_up_suggestions(lang),
            tokens_used=tokens,
            language_detected=lang,
        )

    async def get_history(
        self, user_id: UUID, limit: int = 10, offset: int = 0
    ) -> ChatHistoryResponse:
        count_q = await self.db.execute(
            select(func.count()).select_from(ChatMessage).where(ChatMessage.user_id == user_id)
        )
        total = count_q.scalar() or 0
        result = await self.db.execute(
            select(ChatMessage)
            .where(ChatMessage.user_id == user_id)
            .order_by(ChatMessage.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        rows = result.scalars().all()
        messages = [
            ChatHistoryItem(
                message_id=m.id,
                user_message=m.message_text,
                ai_response=m.ai_response,
                created_at=m.created_at.isoformat() if m.created_at else "",
            )
            for m in rows
        ]
        return ChatHistoryResponse(messages=messages, total_count=total)
