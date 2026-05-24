"""APHRC-style data processing pipeline (stdlib; no pandas required)."""

import csv
import json
import logging
from collections import Counter
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from western_kenya_pipeline import run as run_western_kenya

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pipeline")

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"

SAMPLE_ROWS = [
    {"age": "22", "region": "Kenya", "method": "implant", "discontinued": "0"},
    {"age": "28", "region": "Kenya", "method": "pill", "discontinued": "1"},
    {"age": "35", "region": "Ethiopia", "method": "iud", "discontinued": "0"},
    {"age": "19", "region": "Kenya", "method": "injectable", "discontinued": "0"},
    {"age": "31", "region": "Tanzania", "method": "implant", "discontinued": "0"},
    {"age": "26", "region": "Kenya", "method": "condom", "discontinued": "1"},
    {"age": "40", "region": "Ethiopia", "method": "implant", "discontinued": "0"},
    {"age": "24", "region": "Kenya", "method": "pill", "discontinued": "1"},
]


def run() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw_file = RAW_DIR / "aphrc_sample.csv"

    if raw_file.exists():
        with open(raw_file, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        logger.info("Loaded %s rows from %s", len(rows), raw_file)
    else:
        with open(raw_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=SAMPLE_ROWS[0].keys())
            writer.writeheader()
            writer.writerows(SAMPLE_ROWS)
        rows = SAMPLE_ROWS
        logger.info("Created sample data at %s", raw_file)

    counter = Counter((r.get("region", ""), r.get("method", "")) for r in rows)
    stats = [
        {"region": k[0], "method": k[1], "count": v}
        for k, v in counter.items()
    ]
    out = PROCESSED_DIR / "contraceptive_stats.json"
    out.write_text(json.dumps({"by_region_method": stats}, indent=2), encoding="utf-8")

    cleaned = PROCESSED_DIR / "cleaned_data.csv"
    if rows:
        with open(cleaned, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    logger.info("Pipeline complete. Stats: %s", out)

    wk = run_western_kenya()
    if wk:
        logger.info("Western Kenya programme stats: %s", wk)


if __name__ == "__main__":
    run()
