import pytest


pytestmark = pytest.mark.documentation


def test_test_plan_contains_scope_and_risks(project_root):
    test_plan = (project_root / "test-plan.md").read_text(encoding="utf-8")

    assert "## Scope" in test_plan
    assert "## Risks" in test_plan


def test_bug_report_contains_reproduction_and_expected_result(project_root):
    bug_report = (project_root / "bug-report.md").read_text(encoding="utf-8")

    assert "## Steps To Reproduce" in bug_report
    assert "## Expected Result" in bug_report
