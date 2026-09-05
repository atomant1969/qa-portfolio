from __future__ import annotations

import argparse
import json
from random import Random


PRODUCTS = [
    "QA Automation Toolkit",
    "Performance Test Pack",
    "API Monitoring Bundle",
    "Regression Suite License",
]


def generate_orders(count: int, seed: int) -> list[dict[str, object]]:
    random = Random(seed)
    return [
        {
            "customer": f"Customer {index:03d}",
            "product": random.choice(PRODUCTS),
            "quantity": random.randint(1, 10),
        }
        for index in range(1, count + 1)
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deterministic order test data.")
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    print(json.dumps(generate_orders(args.count, args.seed), indent=2))


if __name__ == "__main__":
    main()
