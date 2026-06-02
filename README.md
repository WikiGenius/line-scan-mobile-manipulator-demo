# Line-Scan Mobile Manipulator Demo

Public scaffold for organizing future work on line-scan-aware active scanning and coverage planning for mobile manipulators.

This repository is part of a broader PhD research workflow on structure-aware planning and control, where robot motion is designed not only to reach a target but also to acquire useful visual or spectral information under physical, geometric, sensing, and uncertainty constraints.

## Purpose

The purpose of this repo is to keep the public-facing structure of the line-scan / RGB-to-hyperspectral active scanning project organized without exposing unpublished algorithms, real lab data, paper drafts, advisor notes, or private experiment details.

It currently hosts scaffold files, documentation, and small synthetic toy examples. It does not yet contain a complete mobile-manipulator planner or validated line-scan sensor model.

## Relation to My PhD Direction

This repo connects to my PhD direction through:

- mobile manipulation for inspection and scanning tasks,
- structure-aware planning under visibility and coverage constraints,
- line-scan / one-row RGB sensing as a public proxy for hyperspectral pushbroom acquisition,
- future geometric, kinematic, collision, and uncertainty constraints,
- state-estimation and control links through supporting repos,
- eventual ROS2 / MoveIt integration for robot simulation and execution.

Related public repos:

| Layer | Related repo | Role |
|---|---|---|
| Mobile manipulation execution | [`ros2-moveit-grasping-demo`](https://github.com/WikiGenius/ros2-moveit-grasping-demo) | Perception-guided grasping and MoveIt2 execution evidence. |
| ROS2 systems | [`ros2-mobile-robotics-labs`](https://github.com/WikiGenius/ros2-mobile-robotics-labs) | ROS2 launch, nodes, simulation, and mobile robotics foundations. |
| Control | [`robotics-control-learning-labs`](https://github.com/WikiGenius/robotics-control-learning-labs) | LQR, observers, state-space control, and tracking foundations. |
| State estimation | [`GTSAM_SLAM_VISION`](https://github.com/WikiGenius/GTSAM_SLAM_VISION) | Factor-graph visual estimation and SLAM-style experiments. |
| 3D perception | [`nerf-lab`](https://github.com/WikiGenius/nerf-lab) | Ray/view-synthesis intuition for active perception. |
| Literature map | [`research-reading-map`](https://github.com/WikiGenius/research-reading-map) | Paper taxonomy and public research architecture. |

## Maturity Level

**Current status:** Public research scaffold / early-stage organization repo

This repository is currently intended to organize the public-facing structure of the project and host simplified, non-confidential demos. It does not yet represent a complete research implementation or a validated planner.

### Implemented now

- [x] Repository structure
- [x] README and project organization
- [x] Public/private boundary notes
- [x] Roadmap and candidate metric documentation
- [x] Minimal toy coverage scripts using synthetic data
- [x] CSV output from toy coverage examples
- [x] Dependency-free SVG toy coverage plot
- [ ] Baseline planner
- [ ] ROS2/MoveIt integration
- [ ] Robot-aware reachability/collision checks
- [ ] Benchmark comparison
- [ ] Paper-supporting implementation

### Not included publicly

- Unpublished research algorithm
- Private paper draft
- Advisor/collaborator notes
- Real lab data
- Full ablation studies
- Confidential experiment results
- Full hyperspectral/RGB scanning pipeline

## Current Contents

```text
docs/          project scope, roadmap, terminology, metrics, and boundaries
src/           public-safe toy line-scan coverage demo
scripts/       simple coverage-metric starter script
experiments/   future public experiment notes
results/       generated toy outputs and future result artifacts
media/         future GIFs/screenshots/videos
launch/        future ROS2 launch files
```

Key files:

- [`src/toy_line_scan_coverage_demo.py`](src/toy_line_scan_coverage_demo.py) - synthetic grid/scan-line coverage demo.
- [`scripts/coverage_metric_demo.py`](scripts/coverage_metric_demo.py) - small cumulative coverage bookkeeping script.
- [`docs/project_scope.md`](docs/project_scope.md) - what this repo studies and what is not implemented.
- [`docs/public_private_boundary.md`](docs/public_private_boundary.md) - what stays public vs private.
- [`docs/roadmap.md`](docs/roadmap.md) - staged development plan.
- [`docs/metrics.md`](docs/metrics.md) - candidate metrics.
- [`TODO.md`](TODO.md) - next practical tasks.

## What This Repo Demonstrates Now

This repo currently demonstrates:

- a clean public research scaffold for active scanning,
- a toy coverage bookkeeping pattern on synthetic data,
- a dependency-free toy SVG plot showing accumulated scan-line coverage,
- public documentation boundaries for protecting unpublished research,
- a staged roadmap from scaffold to post-publication release.

The toy scripts are only intended to demonstrate the idea of accumulating coverage from scan lines over a synthetic grid. They are not mobile-manipulator planners and do not model real sensor physics.

## Planned Development Roadmap

- **Stage 0: repository scaffold** - organize README, docs, folders, public/private policy, and TODO.
- **Stage 1: toy synthetic example** - simulate line coverage over a simple synthetic grid.
- **Stage 2: metric computation** - compute coverage ratio, missing coverage, redundancy, and visibility violations.
- **Stage 3: baseline planner** - add naive raster scan or fixed-standoff baseline.
- **Stage 4: ROS2/MoveIt integration** - connect planning outputs to a robot simulation pipeline.
- **Stage 5: experiment logging and plots** - save metrics, plots, and public-safe logs.
- **Stage 6: paper-supporting private implementation** - keep full method, real data, and ablations private.
- **Stage 7: post-publication public release** - publish sanitized code/results after advisor approval and/or publication.

See [`docs/roadmap.md`](docs/roadmap.md) for the staged roadmap.

## Public / Private Boundary

Public here:

- simplified explanations,
- synthetic toy data,
- starter scripts,
- candidate metrics,
- non-confidential plots,
- public roadmap and limitations.

Private elsewhere:

- full unpublished method,
- paper drafts,
- real RGB/hyperspectral lab data,
- advisor/collaborator notes,
- detailed gap analysis,
- full ablation studies,
- collaboration records.

See [`docs/public_private_boundary.md`](docs/public_private_boundary.md).

## How to Run

Run the toy scan-line coverage demo:

```bash
python src/toy_line_scan_coverage_demo.py
```

It writes:

```text
results/tables/toy_line_scan_coverage.csv
results/figures/toy_line_scan_coverage.svg
```

Run the simpler cumulative coverage metric script:

```bash
python scripts/coverage_metric_demo.py
```

It writes:

```text
results/coverage_metric_demo.csv
```

No complete ROS2/mobile-manipulator demo is included yet. The next planned step is to add a minimal baseline scan planner over a synthetic target.

## Expected Future Outputs

Future public artifacts may include:

- coverage plots,
- scan-line GIFs,
- RViz screenshots,
- experiment logs,
- benchmark tables,
- candidate metric summaries,
- technical report after review,
- paper links only after advisor approval and/or publication.

## Limitations

This repository is currently an early-stage public scaffold. It does not yet include:

- a complete robot model,
- a validated line-scan sensor model,
- real robot experiments,
- full mobile-manipulator motion planning,
- full state estimation,
- collision checking or reachability analysis,
- benchmark comparisons,
- paper-level results.

The current toy scripts use synthetic geometry only and should not be interpreted as a validated research method.

## Citation / Acknowledgment

This project is motivated by robotics research in active perception, coverage planning, mobile manipulation, inspection, and visual/spectral sensing. Cite any papers, datasets, or libraries used when implementation details are added.

## Rights and Reuse

This repository is shared as a public academic portfolio/scaffold. Unless a separate open-source license is explicitly added, all rights are reserved by the author.

## Related Organization

See [`docs/related-repositories.md`](docs/related-repositories.md) for the public/private organization around this main demo and [`docs/method-sketch.md`](docs/method-sketch.md) for the starter method sketch.
