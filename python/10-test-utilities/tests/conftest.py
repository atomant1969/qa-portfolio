from pathlib import Path

import pytest


@pytest.fixture
def metrics_file() -> Path:
    return Path(__file__).parents[1] / "data" / "test_run_metrics.csv"
