from pathlib import Path

import pytest


@pytest.fixture
def workflow_path() -> Path:
    return Path(__file__).parents[1] / "workflows" / "python-tests.yml"
