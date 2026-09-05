import pytest

from src.performance_metrics import summarize_response_times


pytestmark = pytest.mark.performance


def test_response_time_summary_stays_inside_sla(response_time_samples_ms):
    summary = summarize_response_times(response_time_samples_ms)

    assert summary["median_ms"] <= 170
    assert summary["p95_ms"] <= 260


def test_response_time_trend_has_no_large_regression(response_time_samples_ms):
    first_half = response_time_samples_ms[:5]
    second_half = response_time_samples_ms[5:]

    first_summary = summarize_response_times(first_half)
    second_summary = summarize_response_times(second_half)

    assert second_summary["mean_ms"] - first_summary["mean_ms"] < 100
