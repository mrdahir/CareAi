"""Claude API wrapper — DISABLED (kept for easy revert).

Active providers: Gemini and Groq via app.services.llm_service.get_llm_service().
"""

# --- Original Claude implementation (commented for revert) ---
#
# import asyncio
# from typing import AsyncGenerator, List, Optional
#
# from app.config import get_settings
# from app.logging_config import get_logger
# from app.services.prompts import CHATBOT_SYSTEM, FAQ_SYSTEM, MYTH_BUSTER_SYSTEM
#
# logger = get_logger("claude")
#
# MAX_RETRIES = 3
#
#
# class ClaudeService:
#     """Anthropic Claude client with retry and graceful degradation."""
#
#     def __init__(self) -> None:
#         self.settings = get_settings()
#         self._client = None
#         if self.settings.claude_enabled:
#             try:
#                 import anthropic
#
#                 self._client = anthropic.Anthropic(api_key=self.settings.claude_api_key)
#             except Exception as exc:
#                 logger.warning("claude_init_failed", error=str(exc))
#
#     async def complete(
#         self,
#         user_message: str,
#         system: str = CHATBOT_SYSTEM,
#         context: str = "",
#         max_tokens: int = 800,
#     ) -> tuple[str, int]:
#         """Return (response_text, tokens_used)."""
#         if not self._client:
#             return self._fallback_response(user_message, context), 0
#
#         prompt = user_message
#         if context:
#             prompt = f"Knowledge base context:\n{context}\n\nUser question: {user_message}"
#
#         for attempt in range(MAX_RETRIES):
#             try:
#                 response = await asyncio.to_thread(
#                     self._client.messages.create,
#                     model=self.settings.claude_model,
#                     max_tokens=max_tokens,
#                     system=system,
#                     messages=[{"role": "user", "content": prompt}],
#                 )
#                 text = response.content[0].text if response.content else ""
#                 tokens = (
#                     getattr(response.usage, "input_tokens", 0)
#                     + getattr(response.usage, "output_tokens", 0)
#                 )
#                 return text, tokens
#             except Exception as exc:
#                 logger.warning("claude_request_failed", attempt=attempt + 1, error=str(exc))
#                 if attempt == MAX_RETRIES - 1:
#                     return self._fallback_response(user_message, context), 0
#                 await asyncio.sleep(2**attempt)
#         return self._fallback_response(user_message, context), 0
#
#     async def stream_chat(
#         self, user_message: str, context: str = ""
#     ) -> AsyncGenerator[str, None]:
#         """Stream tokens; falls back to chunked static text."""
#         text, _ = await self.complete(user_message, context=context)
#         words = text.split()
#         for i, word in enumerate(words):
#             yield word + (" " if i < len(words) - 1 else "")
#             await asyncio.sleep(0.02)
#
#     def _fallback_response(self, user_message: str, context: str) -> str:
#         disclaimer = (
#             "\n\n*I am not a doctor. Please consult a healthcare provider for personal medical advice.*"
#         )
#         if context:
#             return (
#                 f"Based on verified health information:\n\n{context}\n\n"
#                 f"Regarding your question: I encourage speaking with a clinic provider "
#                 f"for guidance tailored to your situation.{disclaimer}"
#             )
#         return (
#             "Thank you for your question. CareApp provides general reproductive health "
#             "education. For personalized advice, please visit a nearby health facility."
#             + disclaimer
#         )
#
#     @classmethod
#     def test(cls) -> bool:
#         service = cls()
#         return service.settings.claude_enabled and service._client is not None
#
#
# def get_claude_service() -> ClaudeService:
#     return ClaudeService()
