"""Integration tests for API."""

import pytest


@pytest.mark.integration
@pytest.mark.asyncio
async def test_health(client):
    r = await client.get("/api/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_recommend(client):
    r = await client.post(
        "/api/recommend",
        json={
            "age": 28,
            "breastfeeding": False,
            "pregnancy_goals": "space_children",
            "preferred_duration": "long_term",
            "region": "Kenya",
            "language": "en",
        },
    )
    assert r.status_code == 200
    assert "recommendations" in r.json()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_myth_check(client):
    r = await client.post(
        "/api/myth-check",
        json={
            "statement": "Family planning causes permanent infertility",
            "language": "en",
        },
    )
    assert r.status_code == 200
    data = r.json()
    assert data["is_myth"] is True


@pytest.mark.integration
@pytest.mark.asyncio
async def test_chat(client):
    r = await client.post(
        "/api/chat",
        json={"message": "Is the implant safe?", "language": "en"},
    )
    assert r.status_code == 200
    assert "message" in r.json()
