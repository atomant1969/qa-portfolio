from pathlib import Path

import pytest


@pytest.fixture
def jmeter_dir() -> Path:
    return Path(__file__).parents[1] / "jmeter"
