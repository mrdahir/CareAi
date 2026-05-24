"""Load Western Kenya programme monitoring statistics."""

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

STATS_PATH = (
    Path(__file__).resolve().parents[2] / "data" / "processed" / "western_kenya_stats.json"
)


@lru_cache
def get_programme_stats() -> dict[str, Any] | None:
    if not STATS_PATH.exists():
        return None
    with open(STATS_PATH, encoding="utf-8") as f:
        return json.load(f)


def get_regional_method_shares(region: str) -> dict[str, str]:
    """Method popularity shares for recommendation scoring."""
    stats = get_programme_stats()
    if not stats:
        return {}
    region_l = region.lower()
    kenya_counties = {c["county"].lower() for c in stats.get("client_services", {}).get("counties", [])}
    if region_l in ("kenya", "western kenya") or region_l in kenya_counties:
        return stats.get("regional_method_share") or {}
    return {}


def get_programme_context_snippet(query: str = "", region: str = "Kenya") -> str:
    """Short context from real programme data for LLM prompts."""
    stats = get_programme_stats()
    if not stats:
        return ""
    cs = stats["client_services"]
    top = ", ".join(
        f"{m['method']} ({m['share']})" for m in cs.get("top_methods", [])[:5]
    )
    counties = len(cs.get("counties", []))
    lines = [
        f"Western Kenya programme data ({cs['total_client_visits']:,} client visits, {counties} counties):",
        f"Top methods adopted: {top}.",
        f"Counselling rate: {cs.get('counselled_rate', 'N/A')}.",
    ]
    mob = stats.get("mobilisation")
    if mob:
        lines.append(
            f"Community mobilisation: {mob['total_activities']:,} activities, "
            f"~{mob['estimated_people_reached']:,} people reached."
        )
    return "\n".join(lines)
