# Method Sketch

This note describes the public-safe structure of the line-scan active scanning demo.

## Goal

Plan robot motion so a mobile manipulator can acquire useful visual or spectral information, not only reach a geometric target.

## Public Demo Abstraction

The public demo should use a simplified scene and synthetic measurements:

1. Define a target line, surface strip, or inspection region.
2. Generate candidate scan poses.
3. Estimate which target samples are visible from each pose.
4. Track cumulative coverage.
5. Filter or rank candidates using simple constraints.
6. Export a coverage summary under `results/`.

## Starter Script

The first public-safe script is:

```bash
python scripts/coverage_metric_demo.py
```

It creates a synthetic 1D target, checks which target samples are visible from a small set of candidate scan poses, and writes:

```text
results/coverage_metric_demo.csv
```

## What Is Intentionally Simplified

- The target is a synthetic line, not a real RGB/hyperspectral scene.
- The sensor model is a toy lateral-window visibility check.
- There is no ROS2 execution yet.
- Robot reachability, collision checking, calibration, and uncertainty are not included.
- Unpublished planning logic and private experiment settings are excluded.

## Future Public Additions

- Synthetic 2D surface coverage example.
- RViz marker visualization.
- Baseline greedy viewpoint selector.
- Simple reachability filter.
- Public coverage and scan-quality metrics.
