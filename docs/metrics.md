# Candidate Metrics

These metrics are candidates for future public demos and private research experiments.

## Coverage Metrics

- **Coverage ratio**: fraction of target cells, points, or surface samples observed at least once.
- **Missing coverage**: target cells or surface regions not observed.
- **Scan redundancy**: number of repeated observations per already-covered target sample.
- **Coverage uniformity**: how evenly scan observations are distributed across the target.

## Planning / Motion Metrics

- **Path length**: total distance traveled by the sensor, end-effector, or mobile base.
- **Number of scan poses**: count of candidate or executed scanning poses.
- **Motion smoothness**: future metric for scan trajectory quality.
- **Computation time**: wall-clock planning or metric-evaluation time.

## Constraint Metrics

- **Visibility violation count**: number of target samples scanned from invalid viewing conditions.
- **Viewing-angle violation count**: number of samples outside acceptable incidence-angle bounds.
- **Collision count**: number of candidate poses or paths rejected due to collision.
- **Reachability failure count**: number of target scan poses that the robot cannot reach.

## Robustness Metrics

- **Robustness under pose noise**: coverage degradation under sampled pose uncertainty.
- **Worst-case missing coverage**: maximum uncovered fraction under uncertainty.
- **Metric variance**: variability across synthetic or repeated trials.

## Current Public Status

These metrics are candidates only. No public metric script is currently included in this repository.

Future public examples should clearly state whether they evaluate synthetic coverage only, robot kinematics, real sensor physics, collision, or pose uncertainty.
