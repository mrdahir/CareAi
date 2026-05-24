"""Smoke-test Gemini and Groq APIs. Run from backend/: python scripts/test_llm_providers.py"""

import asyncio
import os
import sys

# Ensure backend root is on path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv()

from app.services.gemini_service import GeminiService
from app.services.groq_service import GroqService
from app.services.llm_service import get_llm_service


async def main() -> None:
    print("=== Gemini ===")
    gemini = GeminiService()
    text, tokens = await gemini.complete("Reply with exactly: GEMINI_OK")
    print(f"enabled={gemini._enabled} tokens={tokens}")
    print(f"response: {text[:200]}")

    print("\n=== Groq ===")
    groq = GroqService()
    text, tokens = await groq.complete("Reply with exactly: GROQ_OK")
    print(f"enabled={groq._enabled} tokens={tokens}")
    print(f"response: {text[:200]}")

    print("\n=== LLM facade (LLM_PROVIDER) ===")
    llm = get_llm_service()
    text, tokens = await llm.complete("Say hello in one short sentence.")
    print(f"provider={llm.provider} enabled={llm.enabled} tokens={tokens}")
    print(f"response: {text[:200]}")


if __name__ == "__main__":
    asyncio.run(main())
