from __future__ import annotations

import statistics


def percentile(values: list[float], percentile_rank: int) -> float:
    """Calculate a nearest-rank percentile.

    EN: Small deterministic implementation for portfolio tests.
    RU: Небольшая детерминированная реализация для портфолио-тестов.
    """
    if not values:
        raise ValueError("Cannot calculate percentile for an empty list")

    ordered = sorted(values)
    index = max(0, round((percentile_rank / 100) * len(ordered) + 0.5) - 1)
    return ordered[min(index, len(ordered) - 1)]


def summarize_response_times(values: list[float]) -> dict[str, float]:
    return {
        "mean_ms": round(statistics.mean(values), 2),
        "median_ms": round(statistics.median(values), 2),
        "p95_ms": percentile(values, 95),
    }
