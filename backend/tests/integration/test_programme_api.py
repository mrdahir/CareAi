"""Programme data API tests."""

import pytest


@pytest.mark.integration
@pytest.mark.asyncio
async def test_programme_summary(client):
    r = await client.get("/api/programme/summary")
    if r.status_code == 404:
        pytest.skip("Western Kenya stats not generated — run western_kenya_pipeline.py")
    assert r.status_code == 200
    data = r.json()
    assert data["total_client_visits"] > 0
    assert len(data["top_methods"]) >= 1
