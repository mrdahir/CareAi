#!/usr/bin/env python3
"""
Fill missing sw/am/fr/so keys in knowledge base JSON using Gemini API.
Respects free-tier limits with delays. Requires GEMINI_API_KEY in .env.

Usage:
  python scripts/translate_kb.py
  python scripts/translate_kb.py --lang sw
  python scripts/translate_kb.py --dry-run
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "knowledge_base"
TARGET_LANGS = ("sw", "am", "fr", "so")
DELAY_SEC = 4.0

load_dotenv(ROOT / ".env")
sys.path.insert(0, str(ROOT))

from app.config import get_settings  # noqa: E402


def needs_translation(d: dict[str, str], lang: str) -> bool:
    en = (d.get("en") or "").strip()
    if not en:
        return False
    cur = (d.get(lang) or "").strip()
    return not cur or cur == en


async def translate_one(client: httpx.AsyncClient, text: str, lang: str, model: str, api_key: str) -> str:
    names = {"sw": "Kiswahili", "am": "Amharic", "fr": "French", "so": "Somali"}
    prompt = (
        f"Translate the following reproductive-health education text to {names[lang]}. "
        "Keep medical accuracy. Output ONLY the translation, no quotes or explanation.\n\n"
        f"{text}"
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    body = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"maxOutputTokens": 512}}
    r = await client.post(url, headers={"X-goog-api-key": api_key, "Content-Type": "application/json"}, json=body)
    r.raise_for_status()
    data = r.json()
    parts = (data.get("candidates") or [{}])[0].get("content", {}).get("parts") or []
    return "".join(p.get("text", "") for p in parts).strip()


async def fill_i18n_dict(
    client: httpx.AsyncClient,
    d: dict[str, str],
    langs: tuple[str, ...],
    model: str,
    api_key: str,
    dry_run: bool,
    stats: dict[str, int],
) -> None:
    for lang in langs:
        if lang == "en" or not needs_translation(d, lang):
            continue
        stats["queued"] += 1
        if dry_run:
            print(f"  [dry-run] would translate to {lang}: {(d.get('en') or '')[:60]}...")
            continue
        try:
            d[lang] = await translate_one(client, d["en"], lang, model, api_key)
            stats["done"] += 1
            print(f"  OK {lang}: {d[lang][:80]}...")
        except Exception as exc:
            stats["errors"] += 1
            print(f"  FAIL {lang}: {exc}")
        await asyncio.sleep(DELAY_SEC)


async def process_file(path: Path, langs: tuple[str, ...], model: str, api_key: str, dry_run: bool) -> None:
    print(f"\n=== {path.name} ===")
    data = json.loads(path.read_text(encoding="utf-8"))
    stats = {"queued": 0, "done": 0, "errors": 0}

    async def recurse(obj: Any) -> Any:
        if isinstance(obj, dict):
            if "en" in obj and any(k in obj for k in TARGET_LANGS):
                await fill_i18n_dict(client, obj, langs, model, api_key, dry_run, stats)
                return obj
            out = {}
            for k, v in obj.items():
                out[k] = await recurse(v)
            return out
        if isinstance(obj, list):
            return [await recurse(i) for i in obj]
        return obj

    async with httpx.AsyncClient(timeout=90.0) as client:
        updated = await recurse(data)

    if not dry_run:
        path.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Stats: {stats}")


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", choices=TARGET_LANGS, help="Translate only one language")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--file", choices=["myths", "faqs", "methods", "all"], default="all")
    args = parser.parse_args()

    settings = get_settings()
    if not settings.gemini_enabled and not args.dry_run:
        print("GEMINI_API_KEY not set in backend/.env")
        sys.exit(1)

    langs = (args.lang,) if args.lang else TARGET_LANGS
    files = []
    if args.file in ("myths", "all"):
        files.append(DATA / "common_myths.json")
    if args.file in ("faqs", "all"):
        files.append(DATA / "faqs.json")
    if args.file in ("methods", "all"):
        files.append(DATA / "contraceptive_methods.json")

    for f in files:
        if f.exists():
            await process_file(f, langs, settings.gemini_model, settings.gemini_api_key, args.dry_run)
        else:
            print(f"Skip missing {f}")

    print("\nDone. Re-run: python scripts/load_knowledge_base.py")


if __name__ == "__main__":
    asyncio.run(main())
