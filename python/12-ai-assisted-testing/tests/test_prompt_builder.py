import pytest

from src.prompt_builder import build_log_triage_prompt


pytestmark = pytest.mark.ai


def test_log_triage_prompt_contains_guardrails_and_evidence_request(failure_log):
    prompt = build_log_triage_prompt(failure_log)

    assert "Use only the provided logs" in prompt
    assert "evidence" in prompt
    assert failure_log in prompt
