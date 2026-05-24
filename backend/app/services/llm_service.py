"""Unified LLM facade — routes to Gemini or Groq via LLM_PROVIDER."""

from typing import AsyncGenerator, Literal

from app.config import get_settings
from app.logging_config import get_logger
from app.services.gemini_service import GeminiService
from app.services.groq_service import GroqService
from app.services.prompts import CHATBOT_SYSTEM
from app.utils.language_detection import language_instruction

# Claude (revert): from app.services.claude_service import get_claude_service

logger = get_logger("llm")

ProviderName = Literal["gemini", "groq"]


class LLMService:
    """Provider-agnostic LLM client matching the former ClaudeService interface."""

    def __init__(self) -> None:
        self.settings = get_settings()
        provider = self.settings.llm_provider_normalized
        if provider == "groq":
            self._backend = GroqService()
            self._provider: ProviderName = "groq"
        else:
            self._backend = GeminiService()
            self._provider = "gemini"

    @property
    def provider(self) -> ProviderName:
        return self._provider

    @property
    def enabled(self) -> bool:
        if self._provider == "groq":
            return self.settings.groq_enabled
        return self.settings.gemini_enabled

    async def complete(
        self,
        user_message: str,
        system: str = CHATBOT_SYSTEM,
        context: str = "",
        max_tokens: int = 800,
        language: str = "en",
    ) -> tuple[str, int]:
        full_system = system + language_instruction(language)
        return await self._backend.complete(
            user_message,
            system=full_system,
            context=context,
            max_tokens=max_tokens,
        )

    async def stream_chat(
        self,
        user_message: str,
        context: str = "",
        language: str = "en",
    ) -> AsyncGenerator[str, None]:
        """Stream tokens; falls back to chunked static text."""
        import asyncio

        text, _ = await self.complete(
            user_message, context=context, language=language
        )
        words = text.split()
        for i, word in enumerate(words):
            yield word + (" " if i < len(words) - 1 else "")
            await asyncio.sleep(0.02)

    @classmethod
    def test(cls) -> bool:
        service = cls()
        return service.enabled


def get_llm_service() -> LLMService:
    return LLMService()
