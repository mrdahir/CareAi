"""Myth-busting and FAQ services."""

from app.models.myth_models import (
    ContraceptiveMethodOut,
    ContraceptivesListResponse,
    FAQRequest,
    FAQResponse,
    MythCheckRequest,
    MythCheckResponse,
)
# from app.services.claude_service import get_claude_service
from app.services.llm_service import get_llm_service
from app.services.knowledge_base import get_knowledge_base
from app.services.prompts import FAQ_SYSTEM, MYTH_BUSTER_SYSTEM


class MythService:
    def __init__(self) -> None:
        self.kb = get_knowledge_base()
        self.llm = get_llm_service()

    async def check_myth(self, req: MythCheckRequest) -> MythCheckResponse:
        match = self.kb.find_myth(req.statement, req.language)
        if match:
            return MythCheckResponse(
                is_myth=True,
                severity=match.get("severity", "medium"),
                myth=match["myth"],
                fact=match["fact"],
                evidence=match["evidence"],
                sources=match.get("sources", []),
                similar_myths=match.get("similar", []),
                confidence=0.95,
            )

        context = self.kb.get_context_snippet(req.statement, req.language)
        ai_text, _ = await self.llm.complete(
            f"Is this statement a myth? Statement: {req.statement}\n"
            f"Respond with fact-check in 2-3 sentences.",
            system=MYTH_BUSTER_SYSTEM,
            context=context,
            language=req.language,
        )
        return MythCheckResponse(
            is_myth=False,
            severity="low",
            myth=req.statement,
            fact=ai_text,
            evidence="No exact match in myth database; general guidance provided.",
            sources=["CareApp_Knowledge_Base"],
            similar_myths=[],
            confidence=0.7,
        )

    async def answer_faq(self, req: FAQRequest) -> FAQResponse:
        faq = self.kb.search_faq(req.question, req.language, req.category)
        if faq:
            return FAQResponse(
                question=faq["question"],
                answer=faq["answer"],
                related_faqs=faq.get("related", []),
                sources=faq.get("sources", ["WHO"]),
            )
        context = self.kb.get_context_snippet(req.question, req.language)
        answer, _ = await self.llm.complete(
            req.question,
            system=FAQ_SYSTEM,
            context=context,
            language=req.language,
        )
        return FAQResponse(
            question=req.question,
            answer=answer,
            related_faqs=[],
            sources=["CareApp_Knowledge_Base", "WHO"],
        )

    def list_contraceptives(
        self, language: str = "en", category: str | None = None
    ) -> ContraceptivesListResponse:
        methods = self.kb.get_methods(language, category)
        return ContraceptivesListResponse(
            methods=[
                ContraceptiveMethodOut(
                    id=m["id"],
                    name=m["name"],
                    description=m["description"],
                    effectiveness=m["effectiveness"],
                    duration=m["duration"],
                    side_effects=m["side_effects"],
                    accessibility=m["accessibility"],
                    cost=m["cost"],
                )
                for m in methods
            ]
        )
