"""Simple language detection for supported African languages."""

import re
from typing import Tuple

SUPPORTED = {"en", "sw", "am", "fr", "so"}

SWAHILI_MARKERS = {"na", "ya", "kwa", "ni", "hii", "kupanga", "uzazi"}
FRENCH_MARKERS = {"le", "la", "les", "est", "une", "contraception", "pour"}
SOMALI_MARKERS = {"waxaa", "iyo", "ka", "waa"}


def detect_language(text: str, hint: str | None = None) -> str:
    """Detect language from text; fall back to hint or English."""
    if hint and hint in SUPPORTED:
        return hint
    lower = text.lower()
    words = set(re.findall(r"\b\w+\b", lower))
    if words & SWAHILI_MARKERS:
        return "sw"
    if words & FRENCH_MARKERS:
        return "fr"
    if words & SOMALI_MARKERS:
        return "so"
    if re.search(r"[\u1200-\u137F]", text):
        return "am"
    return "en"


def pick_i18n(data: dict, lang: str, fallback: str = "en") -> str:
    """Pick localized string from multilingual dict."""
    if isinstance(data, str):
        return data
    if not isinstance(data, dict):
        return str(data)
    return data.get(lang) or data.get(fallback) or next(iter(data.values()), "")


LANGUAGE_NAMES: dict[str, str] = {
    "en": "English",
    "sw": "Kiswahili",
    "am": "Amharic",
    "fr": "French",
    "so": "Somali",
}


def language_instruction(lang: str) -> str:
    """Append to system prompt so Gemini/Groq reply in the user's language."""
    code = lang if lang in SUPPORTED else "en"
    name = LANGUAGE_NAMES.get(code, "English")
    return (
        f"\n\nLANGUAGE RULE: You MUST write your entire response in {name} "
        f"(ISO code: {code}). Do not use English unless quoting a source name."
    )


def get_follow_up_suggestions(lang: str) -> list[str]:
    """Localized chat follow-up chips."""
    suggestions: dict[str, list[str]] = {
        "en": [
            "Tell me about side effects",
            "Which method is most effective?",
            "Is this safe while breastfeeding?",
        ],
        "sw": [
            "Niambie kuhusu madhara",
            "Ni njia gani bora zaidi?",
            "Je, ni salama wakati wa kunyonyesha?",
        ],
        "am": [
            "ስለ የጎን ተጽዕኖዎች ይንገሩኝ",
            "በጣም ውጤታማ ዘዴ የቱ ነው?",
            "በማጥባት ጊዜ ደህንነቱ የተጠበቀ ነው?",
        ],
        "fr": [
            "Parlez-moi des effets secondaires",
            "Quelle méthode est la plus efficace?",
            "Est-ce sûr pendant l'allaitement?",
        ],
        "so": [
            "Ii sheeg waxyeellada",
            "Habkee ayaa ugu waxtarka badan?",
            "Ma ammaan baa inta la naasnuujinayo?",
        ],
    }
    return suggestions.get(lang if lang in SUPPORTED else "en", suggestions["en"])
