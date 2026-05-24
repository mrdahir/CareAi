"""Unit tests for knowledge base service."""

import pytest

from app.services.knowledge_base import KnowledgeBaseService


@pytest.mark.unit
def test_kb_loads_methods_myths_faqs():
    kb = KnowledgeBaseService()
    methods = kb.get_methods("en")
    assert len(methods) >= 1
    assert "name" in methods[0]


@pytest.mark.unit
def test_find_myth():
    kb = KnowledgeBaseService()
    match = kb.find_myth(
        "Family planning causes permanent infertility",
        "en",
    )
    assert match is not None
    assert "fact" in match or "fact_text" in match


@pytest.mark.unit
def test_search_faq():
    kb = KnowledgeBaseService()
    faq = kb.search_faq("What is family planning?", "en")
    assert faq is None or "answer" in faq
