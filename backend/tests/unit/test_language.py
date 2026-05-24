"""Language helper tests."""

import pytest

from app.utils.language_detection import (
    get_follow_up_suggestions,
    language_instruction,
)


@pytest.mark.unit
def test_language_instruction_sw():
    text = language_instruction("sw")
    assert "Kiswahili" in text
    assert "sw" in text


@pytest.mark.unit
def test_follow_ups_localized():
    en = get_follow_up_suggestions("en")
    sw = get_follow_up_suggestions("sw")
    assert en != sw
    assert len(sw) >= 2
