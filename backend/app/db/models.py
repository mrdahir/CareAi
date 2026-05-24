"""SQLAlchemy ORM models for CareApp."""

import uuid
from datetime import datetime
from typing import Any, List, Optional

from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from app.db.base import Base, SoftDeleteMixin, TimestampMixin


def _uuid_pk() -> Mapped[uuid.UUID]:
    return mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class User(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = _uuid_pk()
    language: Mapped[str] = mapped_column(String(5), default="en")
    last_active_at: Mapped[Optional[datetime]] = mapped_column(nullable=True)

    messages: Mapped[List["ChatMessage"]] = relationship(back_populates="user")
    feedback: Mapped[List["UserFeedback"]] = relationship(back_populates="user")


class ChatMessage(Base, TimestampMixin):
    __tablename__ = "chat_messages"

    id: Mapped[uuid.UUID] = _uuid_pk()
    user_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    message_text: Mapped[str] = mapped_column(Text)
    ai_response: Mapped[str] = mapped_column(Text)
    language_detected: Mapped[str] = mapped_column(String(5), default="en")
    tokens_used: Mapped[int] = mapped_column(Integer, default=0)
    response_quality_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    sources: Mapped[Optional[Any]] = mapped_column(JSON, default=list)

    user: Mapped[Optional["User"]] = relationship(back_populates="messages")
    feedback: Mapped[List["UserFeedback"]] = relationship(back_populates="message")


class ContraceptiveMethod(Base, TimestampMixin):
    __tablename__ = "contraceptive_methods"

    id: Mapped[uuid.UUID] = _uuid_pk()
    slug: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    descriptions_i18n: Mapped[Optional[Any]] = mapped_column(JSON, default=dict)
    effectiveness_percentage: Mapped[float] = mapped_column(Float)
    duration: Mapped[str] = mapped_column(String(64))
    side_effects: Mapped[Optional[Any]] = mapped_column(JSON, default=list)
    contraindications: Mapped[Optional[Any]] = mapped_column(JSON, default=list)
    cost_level: Mapped[str] = mapped_column(String(16), default="low")
    accessibility: Mapped[str] = mapped_column(String(64), default="clinic_only")


class KnowledgeBase(Base, TimestampMixin):
    __tablename__ = "knowledge_base"

    id: Mapped[uuid.UUID] = _uuid_pk()
    category: Mapped[str] = mapped_column(String(64), index=True)
    content: Mapped[str] = mapped_column(Text)
    content_i18n: Mapped[Optional[Any]] = mapped_column(JSON, default=dict)
    source_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    source_authority: Mapped[str] = mapped_column(String(64), default="WHO")
    language: Mapped[str] = mapped_column(String(5), default="en", index=True)
    verified_by: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)


class Myth(Base, TimestampMixin):
    __tablename__ = "myths"

    id: Mapped[uuid.UUID] = _uuid_pk()
    myth_slug: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    myth_text: Mapped[str] = mapped_column(Text)
    myth_text_i18n: Mapped[Optional[Any]] = mapped_column(JSON, default=dict)
    fact_text: Mapped[str] = mapped_column(Text)
    fact_text_i18n: Mapped[Optional[Any]] = mapped_column(JSON, default=dict)
    evidence: Mapped[str] = mapped_column(Text)
    sources: Mapped[Optional[Any]] = mapped_column(JSON, default=list)
    severity: Mapped[str] = mapped_column(String(16), default="medium")
    language: Mapped[str] = mapped_column(String(5), default="en", index=True)


class UserFeedback(Base, TimestampMixin):
    __tablename__ = "user_feedback"

    id: Mapped[uuid.UUID] = _uuid_pk()
    user_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    message_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("chat_messages.id", ondelete="SET NULL"),
        nullable=True,
    )
    rating: Mapped[int] = mapped_column(Integer)
    feedback_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    user: Mapped[Optional["User"]] = relationship(back_populates="feedback")
    message: Mapped[Optional["ChatMessage"]] = relationship(back_populates="feedback")
