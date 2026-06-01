"""Toy coverage metric for line-scan-inspired active scanning.

This script is public-safe and synthetic. It does not implement unpublished
planning logic; it only demonstrates the kind of coverage bookkeeping that a
future ROS2 scanning demo can report.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path


def target_points(count: int = 41) -> list[tuple[float, float]]:
    return [(i / (count - 1), 0.0) for i in range(count)]


def candidate_viewpoints() -> list[tuple[float, float, float]]:
    # (x, y, yaw). The sensor looks toward negative y in this toy setup.
    return [(-0.05, 0.35, -math.pi / 2), (0.25, 0.35, -math.pi / 2), (0.55, 0.35, -math.pi / 2), (0.85, 0.35, -math.pi / 2)]


def visible_points(viewpoint: tuple[float, float, float], points: list[tuple[float, float]], half_width: float = 0.18) -> set[int]:
    vx, vy, _ = viewpoint
    visible: set[int] = set()
    for idx, (px, py) in enumerate(points):
        lateral_error = abs(px - vx)
        forward_distance = vy - py
        if forward_distance > 0 and lateral_error <= half_width:
            visible.add(idx)
    return visible


def main() -> None:
    points = target_points()
    viewpoints = candidate_viewpoints()
    covered: set[int] = set()
    rows: list[dict[str, object]] = []

    for scan_id, viewpoint in enumerate(viewpoints, start=1):
        visible = visible_points(viewpoint, points)
        new_points = visible - covered
        covered |= visible
        rows.append(
            {
                "scan_id": scan_id,
                "viewpoint_x": viewpoint[0],
                "viewpoint_y": viewpoint[1],
                "visible_points": len(visible),
                "new_points": len(new_points),
                "cumulative_coverage_ratio": round(len(covered) / len(points), 4),
            }
        )

    repo_root = Path(__file__).resolve().parents[1]
    results_dir = repo_root / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "coverage_metric_demo.csv"

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Target points: {len(points)}")
    print(f"Candidate scans: {len(viewpoints)}")
    print(f"Final coverage ratio: {len(covered) / len(points):.3f}")
    print("Wrote results/coverage_metric_demo.csv")


if __name__ == "__main__":
    main()
