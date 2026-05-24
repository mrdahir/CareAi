"""Load knowledge base JSON into database."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.db.database import AsyncSessionLocal, engine
from app.db.init_db import init_db
from app.db.models import ContraceptiveMethod, Myth, KnowledgeBase
from app.services.knowledge_base import get_knowledge_base
from sqlalchemy import select


async def load() -> None:
    await init_db()
    kb = get_knowledge_base()
    async with AsyncSessionLocal() as session:
        for m in kb._methods:
            slug = m["id"]
            existing = await session.execute(
                select(ContraceptiveMethod).where(ContraceptiveMethod.slug == slug)
            )
            if existing.scalar_one_or_none():
                continue
            formatted = kb._format_method(m, "en")
            session.add(
                ContraceptiveMethod(
                    slug=slug,
                    name=formatted["name"],
                    description=formatted["description"],
                    descriptions_i18n=m.get("names", {}),
                    effectiveness_percentage=formatted["effectiveness"],
                    duration=formatted["duration"],
                    side_effects=formatted["side_effects"],
                    contraindications=m.get("contraindications", []),
                    cost_level=formatted["cost"],
                    accessibility=formatted["accessibility"],
                )
            )
        for myth in kb._myths:
            slug = myth["id"]
            existing = await session.execute(select(Myth).where(Myth.myth_slug == slug))
            if existing.scalar_one_or_none():
                continue
            session.add(
                Myth(
                    myth_slug=slug,
                    myth_text=myth.get("myth", {}).get("en", ""),
                    myth_text_i18n=myth.get("myth", {}),
                    fact_text=myth.get("fact", {}).get("en", ""),
                    fact_text_i18n=myth.get("fact", {}),
                    evidence=myth.get("evidence", ""),
                    sources=myth.get("sources", []),
                    severity=myth.get("severity", "medium"),
                    language="en",
                )
            )
        for faq in kb._faqs:
            fid = faq["id"]
            existing = await session.execute(
                select(KnowledgeBase).where(KnowledgeBase.category == f"faq_{fid}")
            )
            if existing.scalars().first():
                continue
            q = faq.get("question", {})
            a = faq.get("answer", {})
            session.add(
                KnowledgeBase(
                    category=faq.get("category", "general"),
                    content=a.get("en", "") if isinstance(a, dict) else str(a),
                    content_i18n={"question": q, "answer": a},
                    source_authority="WHO",
                    language="en",
                    verified_by="CareApp",
                )
            )
        await session.commit()
    print("Knowledge base loaded into database.")


if __name__ == "__main__":
    asyncio.run(load())
