"""FAQ API integration tests."""

import pytest


@pytest.mark.integration
@pytest.mark.asyncio
async def test_faq(client):
    r = await client.post(
        "/api/faq",
        json={"question": "What is an IUD?", "language": "en"},
    )
    assert r.status_code == 200
    data = r.json()
    assert "answer" in data
    assert len(data["answer"]) > 0


@pytest.mark.integration
@pytest.mark.asyncio
async def test_contraceptives_list(client):
    r = await client.get("/api/contraceptives", params={"language": "en"})
    assert r.status_code == 200
    data = r.json()
    methods = data if isinstance(data, list) else data.get("methods", [])
    assert len(methods) >= 1
