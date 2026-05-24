"""Google Gemini API wrapper (generateContent)."""

import asyncio

import httpx

from app.config import get_settings
from app.logging_config import get_logger
from app.services.llm_fallback import fallback_response

logger = get_logger("gemini")

MAX_RETRIES = 3
GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/models"


class GeminiService:
    """Gemini REST client with retry and graceful degradation."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self._enabled = self.settings.gemini_enabled

    def _url(self) -> str:
        model = self.settings.gemini_model
        return f"{GEMINI_BASE}/{model}:generateContent"

    def _headers(self) -> dict[str, str]:
        return {
            "Content-Type": "application/json",
            "X-goog-api-key": self.settings.gemini_api_key,
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
        body: dict = {
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": max_tokens},
        }
        if system:
            body["systemInstruction"] = {"parts": [{"text": system}]}
        return body

    def _parse_response(self, data: dict) -> tuple[str, int]:
        candidates = data.get("candidates") or []
        text = ""
        if candidates:
            parts = candidates[0].get("content", {}).get("parts") or []
            text = "".join(p.get("text", "") for p in parts if isinstance(p, dict))
        usage = data.get("usageMetadata") or {}
        tokens = int(usage.get("totalTokenCount") or 0)
        return text, tokens

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
                        self._url(),
                        headers=self._headers(),
                        json=body,
                    )
                    response.raise_for_status()
                    text, tokens = self._parse_response(response.json())
                    if text:
                        return text, tokens
                    logger.warning("gemini_empty_response", attempt=attempt + 1)
            except Exception as exc:
                logger.warning(
                    "gemini_request_failed", attempt=attempt + 1, error=str(exc)
                )
            if attempt < MAX_RETRIES - 1:
                await asyncio.sleep(2**attempt)

        return fallback_response(user_message, context), 0

    @classmethod
    def test(cls) -> bool:
        return cls()._enabled
