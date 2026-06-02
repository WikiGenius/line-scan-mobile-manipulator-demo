"""Toy line-scan coverage demo on a synthetic grid.

This script demonstrates coverage accumulation from scan lines over a small
synthetic target. It is not a mobile-manipulator planner and does not model real
line-scan or hyperspectral sensor physics.
"""

from __future__ import annotations

import csv
from pathlib import Path


GRID_WIDTH = 36
GRID_HEIGHT = 18
SCAN_ROWS = [2, 5, 8, 11, 14]
SCAN_HALF_WIDTH = 1


def build_coverage_grid() -> list[list[int]]:
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for scan_row in SCAN_ROWS:
        for row in range(max(0, scan_row - SCAN_HALF_WIDTH), min(GRID_HEIGHT, scan_row + SCAN_HALF_WIDTH + 1)):
            for col in range(GRID_WIDTH):
                grid[row][col] += 1
    return grid


def coverage_ratio(grid: list[list[int]]) -> float:
    total = GRID_WIDTH * GRID_HEIGHT
    covered = sum(1 for row in grid for value in row if value > 0)
    return covered / total


def write_csv(grid: list[list[int]], output_path: Path) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["row", "covered_cells", "mean_observation_count"])
        for row_idx, row in enumerate(grid):
            covered = sum(1 for value in row if value > 0)
            mean_count = sum(row) / len(row)
            writer.writerow([row_idx, covered, round(mean_count, 3)])


def color_for_count(count: int) -> str:
    if count == 0:
        return "#f8fafc"
    if count == 1:
        return "#93c5fd"
    if count == 2:
        return "#3b82f6"
    return "#1d4ed8"


def write_svg(grid: list[list[int]], output_path: Path) -> None:
    cell = 18
    margin = 36
    width = GRID_WIDTH * cell + margin * 2
    height = GRID_HEIGHT * cell + margin * 2 + 42
    ratio = coverage_ratio(grid)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{margin}" y="24" font-family="Arial, sans-serif" font-size="16" fill="#0f172a">Toy line-scan coverage demo</text>',
        f'<text x="{margin}" y="46" font-family="Arial, sans-serif" font-size="12" fill="#475569">Synthetic grid coverage ratio: {ratio:.3f}</text>',
    ]

    for row_idx, row in enumerate(grid):
        for col_idx, count in enumerate(row):
            x = margin + col_idx * cell
            y = margin + 30 + row_idx * cell
            lines.append(
                f'<rect x="{x}" y="{y}" width="{cell - 1}" height="{cell - 1}" '
                f'fill="{color_for_count(count)}" stroke="#cbd5e1" stroke-width="0.5"/>'
            )

    legend_y = margin + 30 + GRID_HEIGHT * cell + 24
    legend = [(0, "not covered"), (1, "covered once"), (2, "covered twice")]
    for idx, (count, label) in enumerate(legend):
        x = margin + idx * 150
        lines.append(f'<rect x="{x}" y="{legend_y}" width="16" height="16" fill="{color_for_count(count)}" stroke="#cbd5e1"/>')
        lines.append(f'<text x="{x + 24}" y="{legend_y + 13}" font-family="Arial, sans-serif" font-size="12" fill="#334155">{label}</text>')

    lines.append("</svg>")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    figures_dir = repo_root / "results" / "figures"
    tables_dir = repo_root / "results" / "tables"
    figures_dir.mkdir(parents=True, exist_ok=True)
    tables_dir.mkdir(parents=True, exist_ok=True)

    grid = build_coverage_grid()
    ratio = coverage_ratio(grid)
    write_csv(grid, tables_dir / "toy_line_scan_coverage.csv")
    write_svg(grid, figures_dir / "toy_line_scan_coverage.svg")

    print(f"Synthetic grid: {GRID_WIDTH} x {GRID_HEIGHT}")
    print(f"Scan rows: {SCAN_ROWS}")
    print(f"Coverage ratio: {ratio:.3f}")
    print("Wrote results/tables/toy_line_scan_coverage.csv")
    print("Wrote results/figures/toy_line_scan_coverage.svg")


if __name__ == "__main__":
    main()
