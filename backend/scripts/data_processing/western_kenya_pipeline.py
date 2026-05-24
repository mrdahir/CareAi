"""Process Western Kenya programme monitoring CSVs into CareApp stats."""

from __future__ import annotations

import csv
import json
import logging
import os
from collections import Counter
from pathlib import Path
from typing import Any

logger = logging.getLogger("western_kenya")

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DATA_DIR = Path(
    os.environ.get(
        "WESTERN_KENYA_DATA_DIR",
        str(
            REPO_ROOT
            / "reversing-the-stall-in-fertility-decline-in-western-kenya-programme-monitoring-data-All-2026-05-19_1703"
        ),
    )
)
PROCESSED_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"

METHOD_MAP = {
    "pills": "pill",
    "pill": "pill",
    "condoms": "condom",
    "condom": "condom",
    "injectables": "injectable",
    "injectable": "injectable",
    "implants": "implant",
    "implant": "implant",
    "iucd": "iud",
    "iud": "iud",
    "btl": "permanent",
    "tubal": "permanent",
    "emergency": "emergency_pill",
}


def _normalize_method(raw: str) -> str | None:
    if not raw or raw.strip().upper() in ("N/A", "NONE", ""):
        return None
    key = raw.strip().lower()
    for prefix, slug in METHOD_MAP.items():
        if prefix in key:
            return slug
    return None


def _pct(count: int, total: int) -> str:
    if total <= 0:
        return "0%"
    return f"{round(100 * count / total)}%"


def process_client_services(path: Path) -> dict[str, Any]:
    """Aggregate Client_Service_Statistics.csv."""
    by_county_method: Counter[tuple[str, str]] = Counter()
    by_method: Counter[str] = Counter()
    by_county: Counter[str] = Counter()
    by_age: Counter[str] = Counter()
    by_gender: Counter[str] = Counter()
    new_vs_revisit: Counter[str] = Counter()
    total_rows = 0
    counselled = 0

    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            total_rows += 1
            county = (row.get("county") or "Unknown").strip()
            method_slug = _normalize_method(row.get("methodadopted") or row.get("fp_adopted") or "")
            age = (row.get("client_age") or row.get("client_age2") or "Unknown").strip()
            gender = (row.get("gender") or "Unknown").strip()
            status = (row.get("fpstatus") or "Unknown").strip()

            by_county[county] += 1
            by_age[age] += 1
            by_gender[gender] += 1
            new_vs_revisit[status] += 1
            if (row.get("counseled") or "").strip().lower() == "yes":
                counselled += 1
            if method_slug:
                by_method[method_slug] += 1
                by_county_method[(county, method_slug)] += 1

    method_total = sum(by_method.values()) or 1
    top_methods = [
        {"method": m, "count": c, "share": _pct(c, method_total)}
        for m, c in by_method.most_common(10)
    ]

    counties = []
    for county, _ in by_county.most_common(15):
        county_methods = Counter(
            {m: c for (co, m), c in by_county_method.items() if co == county}
        )
        ct = sum(county_methods.values()) or 1
        counties.append(
            {
                "county": county,
                "visits": by_county[county],
                "top_methods": [
                    {"method": m, "count": c, "share": _pct(c, ct)}
                    for m, c in county_methods.most_common(5)
                ],
            }
        )

    return {
        "source_file": path.name,
        "total_client_visits": total_rows,
        "counselled_yes": counselled,
        "counselled_rate": _pct(counselled, total_rows),
        "top_methods": top_methods,
        "by_gender": dict(by_gender.most_common()),
        "by_age_group": dict(by_age.most_common(10)),
        "fp_status": dict(new_vs_revisit.most_common()),
        "counties": counties,
    }


def process_mobilisation(path: Path) -> dict[str, Any]:
    """Aggregate Mobilisation_Activity_Register.csv."""
    by_county: Counter[str] = Counter()
    by_activity: Counter[str] = Counter()
    topics: Counter[str] = Counter()
    total_reached = 0
    rows = 0

    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            rows += 1
            county = (row.get("county") or "Unknown").strip()
            activity = (row.get("activity") or "Unknown").strip()
            topic = (row.get("discussiontopic") or "").strip().upper()
            by_county[county] += 1
            by_activity[activity] += 1
            if topic and topic not in ("MISSING", "N/A"):
                topics[topic] += 1
            for col in ("maleadult", "maleyouth", "femaleadult", "femaleyouth"):
                try:
                    total_reached += int(row.get(col) or 0)
                except ValueError:
                    pass

    return {
        "source_file": path.name,
        "total_activities": rows,
        "estimated_people_reached": total_reached,
        "top_counties": [{"county": c, "activities": n} for c, n in by_county.most_common(10)],
        "top_activities": [{"activity": a, "count": n} for a, n in by_activity.most_common(8)],
        "top_topics": [{"topic": t, "count": n} for t, n in topics.most_common(15)],
    }


def run(data_dir: Path | None = None) -> Path | None:
    """Run Western Kenya processing; return output path if successful."""
    data_dir = data_dir or DEFAULT_DATA_DIR
    client_csv = data_dir / "Client_Service_Statistics.csv"
    mob_csv = data_dir / "Mobilisation_Activity_Register.csv"

    if not client_csv.exists():
        logger.warning("Western Kenya client CSV not found at %s", client_csv)
        return None

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    payload: dict[str, Any] = {
        "programme": "Reversing the stall in fertility decline — Western Kenya",
        "region": "Western Kenya",
        "country": "Kenya",
        "dataset_folder": str(data_dir.name),
    }

    logger.info("Processing %s ...", client_csv.name)
    payload["client_services"] = process_client_services(client_csv)

    if mob_csv.exists():
        logger.info("Processing %s ...", mob_csv.name)
        payload["mobilisation"] = process_mobilisation(mob_csv)
    else:
        logger.warning("Mobilisation CSV not found: %s", mob_csv)

    # Regional popularity for recommendation engine (Kenya / Western Kenya)
    top = payload["client_services"]["top_methods"]
    total = sum(m["count"] for m in top) or 1
    payload["regional_method_share"] = {
        m["method"]: m["share"] for m in top if m["method"] in ("implant", "iud", "pill", "injectable", "condom")
    }

    out = PROCESSED_DIR / "western_kenya_stats.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info(
        "Western Kenya stats: %s visits, %s counties → %s",
        payload["client_services"]["total_client_visits"],
        len(payload["client_services"]["counties"]),
        out,
    )
    return out


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = run()
    if not result:
        raise SystemExit(1)
