def build_log_triage_prompt(logs: str) -> str:
    """Build a repeatable AI prompt for failure analysis.

    EN: The prompt asks for evidence and next steps, not blind conclusions.
    RU: Промпт требует доказательства и следующие шаги, а не слепые выводы.
    """
    return f"""You are assisting a QA automation engineer.
Classify this failure as product bug, test bug, environment issue, data issue, or unknown.
Use only the provided logs.
Return classification, evidence, next diagnostic steps, and retry recommendation.

Logs:
{logs}
"""
