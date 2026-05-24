"""Initial CareApp schema

Revision ID: 001
Revises:
Create Date: 2026-05-24

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

uuid_type = postgresql.UUID(as_uuid=True)


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", uuid_type, primary_key=True),
        sa.Column("language", sa.String(5), server_default="en"),
        sa.Column("last_active_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
    )
    op.create_table(
        "chat_messages",
        sa.Column("id", uuid_type, primary_key=True),
        sa.Column("user_id", uuid_type, sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=True),
        sa.Column("message_text", sa.Text(), nullable=False),
        sa.Column("ai_response", sa.Text(), nullable=False),
        sa.Column("language_detected", sa.String(5), server_default="en"),
        sa.Column("tokens_used", sa.Integer(), server_default="0"),
        sa.Column("response_quality_score", sa.Float(), nullable=True),
        sa.Column("sources", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
    )
    op.create_table(
        "contraceptive_methods",
        sa.Column("id", uuid_type, primary_key=True),
        sa.Column("slug", sa.String(64), unique=True, index=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("descriptions_i18n", sa.JSON(), nullable=True),
        sa.Column("effectiveness_percentage", sa.Float(), nullable=False),
        sa.Column("duration", sa.String(64), nullable=False),
        sa.Column("side_effects", sa.JSON(), nullable=True),
        sa.Column("contraindications", sa.JSON(), nullable=True),
        sa.Column("cost_level", sa.String(16), server_default="low"),
        sa.Column("accessibility", sa.String(64), server_default="clinic_only"),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
    )
    op.create_table(
        "knowledge_base",
        sa.Column("id", uuid_type, primary_key=True),
        sa.Column("category", sa.String(64), index=True),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("content_i18n", sa.JSON(), nullable=True),
        sa.Column("source_url", sa.String(512), nullable=True),
        sa.Column("source_authority", sa.String(64), server_default="WHO"),
        sa.Column("language", sa.String(5), server_default="en", index=True),
        sa.Column("verified_by", sa.String(128), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
    )
    op.create_table(
        "myths",
        sa.Column("id", uuid_type, primary_key=True),
        sa.Column("myth_slug", sa.String(64), unique=True, index=True),
        sa.Column("myth_text", sa.Text(), nullable=False),
        sa.Column("myth_text_i18n", sa.JSON(), nullable=True),
        sa.Column("fact_text", sa.Text(), nullable=False),
        sa.Column("fact_text_i18n", sa.JSON(), nullable=True),
        sa.Column("evidence", sa.Text(), nullable=False),
        sa.Column("sources", sa.JSON(), nullable=True),
        sa.Column("severity", sa.String(16), server_default="medium"),
        sa.Column("language", sa.String(5), server_default="en", index=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
    )
    op.create_table(
        "user_feedback",
        sa.Column("id", uuid_type, primary_key=True),
        sa.Column("user_id", uuid_type, sa.ForeignKey("users.id", ondelete="SET NULL"), nullable=True),
        sa.Column(
            "message_id",
            uuid_type,
            sa.ForeignKey("chat_messages.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("feedback_text", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP")),
    )


def downgrade() -> None:
    op.drop_table("user_feedback")
    op.drop_table("myths")
    op.drop_table("knowledge_base")
    op.drop_table("contraceptive_methods")
    op.drop_table("chat_messages")
    op.drop_table("users")
