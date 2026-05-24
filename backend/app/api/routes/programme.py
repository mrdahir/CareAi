"""Programme monitoring data API (Western Kenya dataset)."""

from fastapi import APIRouter, HTTPException, Query

from app.services.programme_service import get_programme_stats

router = APIRouter(prefix="/programme", tags=["programme"])


@router.get("/stats")
async def programme_stats(
    county: str | None = Query(None, description="Filter county summary"),
):
    stats = get_programme_stats()
    if not stats:
        raise HTTPException(
            status_code=404,
            detail="Programme data not loaded. Run: python scripts/data_processing/western_kenya_pipeline.py",
        )
    if county:
        counties = stats.get("client_services", {}).get("counties", [])
        match = next(
            (c for c in counties if c["county"].lower() == county.lower()),
            None,
        )
        if not match:
            raise HTTPException(status_code=404, detail=f"No data for county: {county}")
        return {"programme": stats["programme"], "county": match}
    return stats


@router.get("/summary")
async def programme_summary():
    stats = get_programme_stats()
    if not stats:
        raise HTTPException(status_code=404, detail="Programme data not loaded.")
    cs = stats["client_services"]
    return {
        "programme": stats["programme"],
        "region": stats["region"],
        "total_client_visits": cs["total_client_visits"],
        "counselled_rate": cs["counselled_rate"],
        "top_methods": cs["top_methods"][:5],
        "county_count": len(cs["counties"]),
    }
