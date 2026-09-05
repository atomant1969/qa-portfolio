import pytest

from analyze_test_results import analyze
from data_generator import generate_orders


pytestmark = pytest.mark.utilities


def test_data_generator_is_deterministic():
    first = generate_orders(count=3, seed=7)
    second = generate_orders(count=3, seed=7)

    assert first == second
    assert len(first) == 3


def test_test_result_analyzer_calculates_quality_metrics(metrics_file):
    metrics = analyze(metrics_file)

    assert metrics["pass_rate"] == 0.9575
    assert metrics["failure_rate"] == 0.0425
    assert metrics["p95_duration_ms"] >= metrics["median_duration_ms"]
