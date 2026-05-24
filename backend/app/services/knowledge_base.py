"""Load and query structured knowledge base JSON files."""

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from app.logging_config import get_logger
from app.utils.language_detection import pick_i18n

logger = get_logger("knowledge_base")

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "knowledge_base"


class KnowledgeBaseService:
    """In-memory knowledge base backed by JSON files."""

    def __init__(self) -> None:
        self._methods: List[Dict[str, Any]] = []
        self._myths: List[Dict[str, Any]] = []
        self._faqs: List[Dict[str, Any]] = []
        self._load_all()

    def _load_json(self, filename: str) -> Any:
        path = DATA_DIR / filename
        if not path.exists():
            logger.warning("knowledge_file_missing", file=str(path))
            return {}
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def _load_all(self) -> None:
        methods_data = self._load_json("contraceptive_methods.json")
        self._methods = methods_data.get("methods", [])
        myths_data = self._load_json("common_myths.json")
        self._myths = myths_data.get("myths", [])
        faqs_data = self._load_json("faqs.json")
        self._faqs = faqs_data.get("faqs", [])
        logger.info(
            "knowledge_base_loaded",
            methods=len(self._methods),
            myths=len(self._myths),
            faqs=len(self._faqs),
        )

    def get_methods(
        self, language: str = "en", category: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        results = []
        for m in self._methods:
            if category and m.get("duration_category") != category:
                continue
            results.append(self._format_method(m, language))
        return results

    def get_method_by_id(self, method_id: str, language: str = "en") -> Optional[Dict[str, Any]]:
        for m in self._methods:
            if m.get("id") == method_id:
                return self._format_method(m, language)
        return None

    def _format_method(self, m: Dict[str, Any], language: str) -> Dict[str, Any]:
        names = m.get("names", {})
        desc = m.get("descriptions", m.get("description", {}))
        if isinstance(desc, str):
            description = desc
        else:
            description = pick_i18n(desc, language)
        side = m.get("side_effects", {})
        common = side.get("common", []) if isinstance(side, dict) else side
        side_list = []
        for item in common[:5]:
            if isinstance(item, dict):
                side_list.append(pick_i18n(item, language))
            else:
                side_list.append(str(item))
        return {
            "id": m.get("id"),
            "name": pick_i18n(names, language) if names else m.get("id", ""),
            "description": description,
            "effectiveness": m.get("effectiveness", 0),
            "duration": m.get("duration", ""),
            "duration_category": m.get("duration_category", "long_term"),
            "side_effects": side_list,
            "accessibility": m.get("accessibility", "clinic_only"),
            "cost": m.get("cost", "low"),
            "contraindications": m.get("contraindications", []),
            "reversible": m.get("reversible", True),
            "best_for": m.get("best_for", []),
            "sources": m.get("sources", []),
        }

    def find_myth(self, statement: str, language: str = "en") -> Optional[Dict[str, Any]]:
        statement_lower = statement.lower().strip()
        best: Optional[Dict[str, Any]] = None
        best_score = 0
        for myth in self._myths:
            myth_texts = myth.get("myth", {})
            if isinstance(myth_texts, dict):
                for text in myth_texts.values():
                    score = self._similarity(statement_lower, text.lower())
                    if score > best_score:
                        best_score = score
                        best = myth
            elif isinstance(myth_texts, str):
                score = self._similarity(statement_lower, myth_texts.lower())
                if score > best_score:
                    best_score = score
                    best = myth
        if best_score >= 0.35:
            return self._format_myth(best, language)
        return None

    def _similarity(self, a: str, b: str) -> float:
        words_a = set(a.split())
        words_b = set(b.split())
        if not words_a or not words_b:
            return 0.0
        return len(words_a & words_b) / max(len(words_a), len(words_b))

    def _format_myth(self, myth: Dict[str, Any], language: str) -> Dict[str, Any]:
        return {
            "id": myth.get("id"),
            "myth": pick_i18n(myth.get("myth", {}), language),
            "fact": pick_i18n(myth.get("fact", {}), language),
            "evidence": myth.get("evidence", ""),
            "severity": myth.get("severity", "medium"),
            "sources": myth.get("sources", []),
            "similar": [
                pick_i18n(m.get("myth", {}), language)
                for m in self._myths[:5]
                if m.get("id") != myth.get("id")
            ][:3],
        }

    def search_faq(
        self, question: str, language: str = "en", category: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        q_lower = question.lower()
        best: Optional[Dict[str, Any]] = None
        best_score = 0.0
        for faq in self._faqs:
            if category and faq.get("category") != category:
                continue
            fq = pick_i18n(faq.get("question", {}), language).lower()
            score = self._similarity(q_lower, fq)
            if score > best_score:
                best_score = score
                best = faq
        if best and best_score >= 0.2:
            return {
                "question": pick_i18n(best.get("question", {}), language),
                "answer": pick_i18n(best.get("answer", {}), language),
                "category": best.get("category", "general"),
                "sources": best.get("sources", []),
                "related": [
                    pick_i18n(f.get("question", {}), language)
                    for f in self._faqs
                    if f.get("id") != best.get("id")
                    and f.get("category") == best.get("category")
                ][:3],
            }
        return None

    def get_context_snippet(self, query: str, language: str = "en", limit: int = 3) -> str:
        """Build context string for Claude from KB."""
        parts: List[str] = []
        method = None
        for m in self._methods:
            name = pick_i18n(m.get("names", {}), language).lower()
            if any(w in query.lower() for w in name.split() if len(w) > 3):
                method = self._format_method(m, language)
                break
        if method:
            parts.append(
                f"Method: {method['name']}, effectiveness {method['effectiveness']}%, "
                f"duration {method['duration']}."
            )
        myth = self.find_myth(query, language)
        if myth:
            parts.append(f"Related fact: {myth['fact']}")
        faq = self.search_faq(query, language)
        if faq:
            parts.append(f"FAQ: {faq['answer'][:300]}")
        return "\n".join(parts[:limit])


@lru_cache
def get_knowledge_base() -> KnowledgeBaseService:
    return KnowledgeBaseService()
