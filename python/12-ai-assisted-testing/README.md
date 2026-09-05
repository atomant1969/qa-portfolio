# AI-Assisted QA Automation Workflows

This folder documents AI workflows that can be used safely in QA automation without treating AI output as automatically correct.

## Use Cases

| Workflow | Input | Output | Human validation |
| --- | --- | --- | --- |
| Test idea generation | User story or acceptance criteria | Candidate test scenarios | QA reviews risk, removes duplicates, adds missing edge cases |
| Log triage | Sanitized logs and failure messages | Probable failure category and next checks | Engineer confirms with source logs and system state |
| Bug report drafting | Reproduction notes and screenshots | Structured bug report draft | QA verifies actual/expected behavior |
| Test data generation | Domain rules and constraints | JSON/CSV examples | Automated schema validation and manual spot check |
| Regression impact analysis | Changed files and release notes | Suggested test subset | QA compares against known risk areas |

## Example Prompt: Log Triage

```text
You are assisting a QA automation engineer.
Classify this failure as product bug, test bug, environment issue, data issue, or unknown.
Use only the provided logs.
Return:
1. classification
2. evidence
3. next diagnostic steps
4. whether the test should be retried

Logs:
<paste sanitized logs here>
```

## Example Prompt: Test Design

```text
Given this acceptance criterion, generate positive, negative, boundary, and data validation test ideas.
Do not invent requirements.
Flag assumptions separately.

Acceptance criterion:
<paste requirement here>
```

## Automation Principles

- Do not send secrets, customer data, or private logs to external AI tools.
- Keep prompts versioned when they become part of a repeatable process.
- Treat generated tests as drafts until reviewed.
- Prefer AI for acceleration: summarizing logs, creating drafts, and exploring edge cases.
- Keep deterministic automation in code, not in prompt-only workflows.
