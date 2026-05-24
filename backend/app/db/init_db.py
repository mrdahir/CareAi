"""Initialize database tables."""

from app.db.base import Base
from app.db.database import engine
from app.db import models  # noqa: F401


async def init_db() -> None:
    """Create all tables (development bootstrap).

    For PostgreSQL production, prefer: ``alembic upgrade head``
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
