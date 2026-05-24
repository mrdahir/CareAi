"""Pytest fixtures."""

import os
import pytest
from httpx import ASGITransport, AsyncClient

os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///./test_care_app.db")
os.environ.setdefault("LLM_PROVIDER", "gemini")
os.environ.setdefault("RATE_LIMIT_ENABLED", "false")
os.environ.setdefault("GEMINI_API_KEY", "")
os.environ.setdefault("GROQ_API_KEY", "")

from app.main import app  # noqa: E402
from app.db.init_db import init_db  # noqa: E402


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
async def setup_db():
    await init_db()
    yield


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
