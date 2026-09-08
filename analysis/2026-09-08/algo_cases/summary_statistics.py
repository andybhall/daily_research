#!/usr/bin/env python3
"""
Summary Statistics for Algorithmic Contestability Cases Database

This script generates the summary statistics reported in the paper
"Beyond Explanation: A Case for Evidentiary Rights in Algorithmic Accountability"

Usage:
    python summary_statistics.py
"""

import csv
import json
from collections import Counter
from pathlib import Path


def load_cases(filepath: str = None) -> list:
    """Load cases from CSV file."""
    if filepath is None:
        filepath = Path(__file__).parent.parent / "data" / "cases.csv"

    cases = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cases.append(row)
    return cases


def compute_statistics(cases: list) -> dict:
    """Compute summary statistics for the case database."""

    stats = {
        "total_cases": len(cases),
        "by_domain": {},
        "by_access_level": Counter(),
        "by_outcome": Counter(),
        "by_jurisdiction_type": {"US": 0, "International": 0},
        "achieved_rate_by_access": {},
    }

    # Domain-level statistics
    domains = set(c["domain"] for c in cases)
    for domain in sorted(domains):
        domain_cases = [c for c in cases if c["domain"] == domain]
        access_counts = Counter(c["access_level"] for c in domain_cases)
        outcome_counts = Counter(c["outcome"] for c in domain_cases)

        # Calculate achieved rate (excluding ongoing)
        resolved = [c for c in domain_cases if c["outcome"] != "Ongoing"]
        achieved = [c for c in resolved if c["outcome"] == "Achieved"]
        achieved_rate = len(achieved) / len(resolved) * 100 if resolved else 0

        stats["by_domain"][domain] = {
            "count": len(domain_cases),
            "full_access": access_counts.get("Full", 0),
            "partial_access": access_counts.get("Partial", 0),
            "no_access": access_counts.get("None", 0),
            "achieved": outcome_counts.get("Achieved", 0),
            "denied": outcome_counts.get("Denied", 0),
            "ongoing": outcome_counts.get("Ongoing", 0),
            "achieved_rate": round(achieved_rate, 1),
        }

    # Overall access level counts
    stats["by_access_level"] = dict(Counter(c["access_level"] for c in cases))

    # Overall outcome counts
    stats["by_outcome"] = dict(Counter(c["outcome"] for c in cases))

    # Jurisdiction breakdown
    for case in cases:
        jurisdiction = case["jurisdiction"]
        if jurisdiction.startswith("US"):
            stats["by_jurisdiction_type"]["US"] += 1
        else:
            stats["by_jurisdiction_type"]["International"] += 1

    # Achieved rate by access level
    for access in ["Full", "Partial", "None"]:
        access_cases = [c for c in cases if c["access_level"] == access]
        resolved = [c for c in access_cases if c["outcome"] != "Ongoing"]
        achieved = [c for c in resolved if c["outcome"] == "Achieved"]
        rate = len(achieved) / len(resolved) * 100 if resolved else 0
        stats["achieved_rate_by_access"][access] = {
            "total": len(access_cases),
            "resolved": len(resolved),
            "achieved": len(achieved),
            "rate": round(rate, 1),
        }

    return stats


def print_statistics(stats: dict) -> None:
    """Print formatted summary statistics."""

    print("=" * 60)
    print("ALGORITHMIC CONTESTABILITY CASES - SUMMARY STATISTICS")
    print("=" * 60)
    print(f"\nTotal Cases: {stats['total_cases']}")

    print("\n" + "-" * 60)
    print("BY DOMAIN")
    print("-" * 60)
    print(f"{'Domain':<25} {'N':>5} {'Full':>6} {'Part':>6} {'None':>6} {'Rate':>7}")
    print("-" * 60)

    for domain, data in stats["by_domain"].items():
        print(f"{domain:<25} {data['count']:>5} {data['full_access']:>6} "
              f"{data['partial_access']:>6} {data['no_access']:>6} "
              f"{data['achieved_rate']:>6.1f}%")

    print("\n" + "-" * 60)
    print("OVERALL ACCESS LEVELS")
    print("-" * 60)
    for level, count in stats["by_access_level"].items():
        pct = count / stats["total_cases"] * 100
        print(f"{level:<15} {count:>5} ({pct:>5.1f}%)")

    print("\n" + "-" * 60)
    print("OVERALL OUTCOMES")
    print("-" * 60)
    for outcome, count in stats["by_outcome"].items():
        pct = count / stats["total_cases"] * 100
        print(f"{outcome:<15} {count:>5} ({pct:>5.1f}%)")

    print("\n" + "-" * 60)
    print("ACHIEVED RATE BY ACCESS LEVEL")
    print("-" * 60)
    for access, data in stats["achieved_rate_by_access"].items():
        print(f"{access:<15} {data['achieved']:>3}/{data['resolved']:>3} resolved = {data['rate']:>5.1f}%")

    print("\n" + "-" * 60)
    print("JURISDICTION")
    print("-" * 60)
    for jtype, count in stats["by_jurisdiction_type"].items():
        pct = count / stats["total_cases"] * 100
        print(f"{jtype:<15} {count:>5} ({pct:>5.1f}%)")

    print("\n" + "=" * 60)


def main():
    """Main entry point."""
    cases = load_cases()
    stats = compute_statistics(cases)
    print_statistics(stats)

    # Also save as JSON
    output_path = Path(__file__).parent / "summary_statistics.json"
    with open(output_path, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"\nStatistics saved to: {output_path}")


if __name__ == "__main__":
    main()
