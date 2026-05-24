"""Shared fallback responses when no LLM provider is configured."""


def fallback_response(user_message: str, context: str) -> str:
    disclaimer = (
        "\n\n*I am not a doctor. Please consult a healthcare provider for personal medical advice.*"
    )
    if context:
        return (
            f"Based on verified health information:\n\n{context}\n\n"
            f"Regarding your question: I encourage speaking with a clinic provider "
            f"for guidance tailored to your situation.{disclaimer}"
        )
    return (
        "Thank you for your question. CareApp provides general reproductive health "
        "education. For personalized advice, please visit a nearby health facility."
        + disclaimer
    )
