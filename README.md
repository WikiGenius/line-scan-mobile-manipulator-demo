# Line-Scan Mobile Manipulator Demo

Public organization repo for future work on line-scan-aware active scanning and coverage planning for mobile manipulators.

This repository is part of a broader PhD research direction on structure-aware planning and control, where robot motion is designed not only to reach a target but also to acquire useful visual or spectral information under physical, geometric, sensing, and uncertainty constraints.

## Purpose

The purpose of this repo is to organize the public-facing structure of the line-scan / RGB-to-hyperspectral active scanning project without exposing unpublished algorithms, real lab data, paper drafts, advisor notes, or private experiment details.

This repo currently contains documentation, scope notes, public/private boundaries, candidate metrics, and placeholders for future public-safe demos. It does not currently contain a runnable planner, synthetic demo script, generated result, mobile-manipulator implementation, or validated line-scan sensor model.

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
| 3D perception | [`nerf-lab`](https://github.com/WikiGenius/nerf-lab) | View synthesis and scene-representation intuition for active perception. |
| Literature map | [`research-reading-map`](https://github.com/WikiGenius/research-reading-map) | Paper taxonomy and public research architecture. |

## Maturity Level

**Current status:** Public research organization repo / early-stage scaffold

This repository is currently intended to show the research direction, repo structure, and development boundary. It does not yet represent a complete research implementation or a validated planner.

### Implemented now

- [x] Repository structure
- [x] README and project organization
- [x] Public/private boundary notes
- [x] Roadmap and candidate metric documentation
- [x] Relationship map to supporting public repos
- [ ] Public-safe baseline script
- [ ] Public-safe synthetic result
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
docs/          project scope, roadmap, terminology, metrics, boundaries, and repo links
src/           reserved for future public-safe source files
experiments/   reserved for future public experiment notes
results/       reserved for future public-safe result artifacts
media/         reserved for future GIFs/screenshots/videos
launch/        reserved for future ROS2 launch files
```

Key files:

- [`docs/project_scope.md`](docs/project_scope.md) - what this repo studies and what is not implemented.
- [`docs/public_private_boundary.md`](docs/public_private_boundary.md) - what stays public vs private.
- [`docs/roadmap.md`](docs/roadmap.md) - staged development plan.
- [`docs/metrics.md`](docs/metrics.md) - candidate metrics.
- [`docs/related-repositories.md`](docs/related-repositories.md) - how the public repos support the research identity.
- [`TODO.md`](TODO.md) - next practical tasks.

## What This Repo Demonstrates Now

This repo currently demonstrates:

- a clean public research scaffold for active scanning,
- the intended role of line-scan-inspired sensing in the mobile manipulation research direction,
- public documentation boundaries for protecting unpublished research,
- a staged roadmap from scaffold to future public-safe demos and post-publication release,
- how supporting public repos connect to planning, control, state estimation, ROS2, MoveIt, and 3D perception.

## Planned Development Roadmap

- **Stage 0: repository scaffold** - organize README, docs, folders, public/private policy, and TODO.
- **Stage 1: public-safe simplified example** - add a clearly labeled synthetic example only after it is intentionally designed and reviewed.
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
- repo organization,
- candidate metrics,
- future public-safe examples,
- non-confidential plots after they are intentionally created,
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

There is currently no runnable planner or demo script in this public repo.

Future public commands will be added only when the corresponding demo is real, intentional, and safe to publish.

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

Any future simplified public examples should be interpreted as portfolio scaffolding unless explicitly described as validated research code.

## Citation / Acknowledgment

This project is motivated by robotics research in active perception, coverage planning, mobile manipulation, inspection, and visual/spectral sensing. Cite any papers, datasets, courses, or libraries used when implementation details are added.

## Rights and Reuse

This repository is shared as a public academic portfolio/scaffold. Unless a separate open-source license is explicitly added, all rights are reserved by the author.

## Related Organization

See [`docs/related-repositories.md`](docs/related-repositories.md) for the public/private organization around this main demo and [`docs/method-sketch.md`](docs/method-sketch.md) for the method sketch.
