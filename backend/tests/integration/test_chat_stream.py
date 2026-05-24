"""Streaming chat endpoint tests."""

import pytest


@pytest.mark.integration
@pytest.mark.asyncio
async def test_chat_stream(client):
    r = await client.post(
        "/api/chat/stream",
        json={"message": "Hello", "language": "en"},
    )
    assert r.status_code == 200
    body = r.text
    assert len(body) > 0
