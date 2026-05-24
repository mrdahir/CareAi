"""Groq Cloud API wrapper (OpenAI-compatible chat completions)."""

import asyncio

import httpx

from app.config import get_settings
from app.logging_config import get_logger
from app.services.llm_fallback import fallback_response

logger = get_logger("groq")

MAX_RETRIES = 3
GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"


class GroqService:
    """Groq chat completions client with retry and graceful degradation."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self._enabled = self.settings.groq_enabled

    def _headers(self) -> dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.settings.groq_api_key}",
        }

    def _build_body(
        self,
        user_message: str,
        system: str,
        context: str,
        max_tokens: int,
    ) -> dict:
        prompt = user_message
        if context:
            prompt = (
                f"Knowledge base context:\n{context}\n\nUser question: {user_message}"
            )
        messages: list[dict[str, str]] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        return {
            "model": self.settings.groq_model,
            "messages": messages,
            "max_tokens": max_tokens,
        }

    def _parse_response(self, data: dict) -> tuple[str, int]:
        choices = data.get("choices") or []
        text = ""
        if choices:
            text = (choices[0].get("message") or {}).get("content") or ""
        usage = data.get("usage") or {}
        tokens = int(usage.get("total_tokens") or 0)
        return text.strip(), tokens

    async def complete(
        self,
        user_message: str,
        system: str = "",
        context: str = "",
        max_tokens: int = 800,
    ) -> tuple[str, int]:
        if not self._enabled:
            return fallback_response(user_message, context), 0

        body = self._build_body(user_message, system, context, max_tokens)

        for attempt in range(MAX_RETRIES):
            try:
                async with httpx.AsyncClient(timeout=60.0) as client:
                    response = await client.post(
                        GROQ_CHAT_URL,
                        headers=self._headers(),
                        json=body,
                    )
                    response.raise_for_status()
                    text, tokens = self._parse_response(response.json())
                    if text:
                        return text, tokens
                    logger.warning("groq_empty_response", attempt=attempt + 1)
            except Exception as exc:
                logger.warning(
                    "groq_request_failed", attempt=attempt + 1, error=str(exc)
                )
            if attempt < MAX_RETRIES - 1:
                await asyncio.sleep(2**attempt)

        return fallback_response(user_message, context), 0

    @classmethod
    def test(cls) -> bool:
        return cls()._enabled
