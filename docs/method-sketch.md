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

## Current Implementation Status

No public script is currently included in this repository.

Future public examples should be added only after they are intentionally designed, clearly labeled as simplified demos, and checked against the public/private boundary.

## What Is Intentionally Simplified

- Future public examples may use a synthetic target instead of real RGB/hyperspectral data.
- Future public examples may use simplified visibility checks before real sensor physics is published.
- There is no ROS2 execution yet.
- Robot reachability, collision checking, calibration, and uncertainty are not included.
- Unpublished planning logic and private experiment settings are excluded.

## Future Public Additions

- Synthetic 2D surface coverage example.
- RViz marker visualization.
- Baseline greedy viewpoint selector.
- Simple reachability filter.
- Public coverage and scan-quality metrics.
