from __future__ import annotations

import argparse
import csv
import statistics
from pathlib import Path


def analyze(path: Path) -> dict[str, float]:
    with path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    passed = sum(int(row["passed"]) for row in rows)
    failed = sum(int(row["failed"]) for row in rows)
    durations = [float(row["duration_ms"]) for row in rows]
    total = passed + failed

    return {
        "pass_rate": round(passed / total, 4),
        "failure_rate": round(failed / total, 4),
        "mean_duration_ms": round(statistics.mean(durations), 2),
        "median_duration_ms": round(statistics.median(durations), 2),
        "p95_duration_ms": round(statistics.quantiles(durations, n=20)[18], 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze CSV test result metrics.")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()

    for metric, value in analyze(args.csv_path).items():
        print(f"{metric}: {value}")


if __name__ == "__main__":
    main()
