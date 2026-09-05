import pytest
import yaml


pytestmark = pytest.mark.cicd


def test_python_workflow_runs_tests_after_installing_dependencies(workflow_path):
    workflow = yaml.safe_load(workflow_path.read_text(encoding="utf-8"))
    steps = workflow["jobs"]["test"]["steps"]
    step_names = [step["name"] for step in steps]

    assert "Install dependencies" in step_names
    assert "Run tests" in step_names
    assert step_names.index("Install dependencies") < step_names.index("Run tests")
