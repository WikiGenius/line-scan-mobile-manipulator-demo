# Line-Scan Mobile Manipulator Demo

Public scaffold for organizing future work on line-scan-aware active scanning and coverage planning for mobile manipulators.

## Purpose

This repository organizes the public-facing structure of a line-scan / one-row RGB active-scanning project without exposing unpublished algorithms, real lab data, paper drafts, advisor notes, or private experiment details.

It currently contains documentation, scope notes, public/private boundaries, candidate metrics, and folders for future public-safe demos. It does not currently contain a runnable planner, generated result, mobile-manipulator implementation, or tested line-scan sensor model.

## Relation to My PhD Direction

My PhD research focuses on structure-aware planning, state estimation, and active sensing for mobile manipulation. This repo connects to that direction through:

- mobile manipulation for inspection and scanning tasks,
- active sensing where motion is planned to acquire useful visual or spectral information,
- motion planning under physical and geometric constraints,
- geometric visibility constraints for scan quality,
- line-scan / one-row RGB sensing as a public proxy for hyperspectral pushbroom acquisition,
- state-estimation links through pose uncertainty and visual SLAM,
- control links through scan trajectory execution and base-arm coordination.

Related public repos:

| Layer | Related repo | Role |
|---|---|---|
| Mobile manipulation execution | [`ros2-moveit-grasping-demo`](https://github.com/WikiGenius/ros2-moveit-grasping-demo) | Perception-guided grasping and MoveIt2 execution evidence. |
| ROS2 systems | [`ros2-mobile-robotics-labs`](https://github.com/WikiGenius/ros2-mobile-robotics-labs) | ROS2 scaffold for future mobile robotics labs. |
| Control | [`robotics-control-learning-labs`](https://github.com/WikiGenius/robotics-control-learning-labs) | State-space control, LQR, observers, and tracking foundations. |
| State estimation | [`GTSAM_SLAM_VISION`](https://github.com/WikiGenius/GTSAM_SLAM_VISION) | Factor-graph visual estimation and SLAM-style experiments. |
| 3D perception | [`nerf-lab`](https://github.com/WikiGenius/nerf-lab) | View synthesis and scene-representation intuition for active perception. |
| Literature map | [`research-reading-map`](https://github.com/WikiGenius/research-reading-map) | Public reading map and research architecture. |

## Maturity Level

**Current status:** Public research scaffold / early-stage organization repo

This repository is intended to organize the public-facing structure of the project and host simplified, non-confidential demos. It does not yet represent a complete research implementation or a tested planner.

## Implemented Now

- [x] Repository structure
- [x] README and project organization
- [x] Public/private boundary documentation
- [x] Roadmap and candidate metric documentation
- [x] Relationship map to supporting public repos
- [ ] Minimal synthetic line-scan demo
- [ ] Coverage plot or GIF
- [ ] Baseline comparison
- [ ] ROS2/MoveIt integration
- [ ] Paper-supporting implementation

## Planned Later

- Minimal synthetic line-scan example.
- Coverage metric computation.
- Naive raster-scan baseline.
- Mobile manipulator model.
- Visibility constraint checks.
- ROS2/MoveIt integration.
- Uncertainty-aware experiments.
- Paper-supporting implementation after advisor approval.

## Intentionally Private

- Unpublished research algorithm.
- Full problem formulation details.
- Private paper drafts.
- Advisor/collaborator notes.
- Real lab data.
- Detailed gap analysis.
- Full ablation studies.
- Confidential experiment results.

## Current Runnable Artifact

No complete runnable demo is included yet. The next planned step is to add a minimal synthetic line-scan coverage example.

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

- [`docs/project_scope.md`](docs/project_scope.md): what this repo studies and what is not implemented.
- [`docs/public_private_boundary.md`](docs/public_private_boundary.md): what stays public vs private.
- [`docs/roadmap.md`](docs/roadmap.md): staged development plan.
- [`docs/metrics.md`](docs/metrics.md): candidate metrics.
- [`docs/terminology.md`](docs/terminology.md): terms used in the project.
- [`docs/related-repositories.md`](docs/related-repositories.md): how public repos support the research identity.
- [`TODO.md`](TODO.md): next practical tasks.

## Roadmap

1. Public scaffold.
2. Minimal synthetic line-scan example.
3. Coverage metrics.
4. Baseline planner.
5. Robot-aware planning.
6. ROS2/MoveIt integration.
7. Uncertainty-aware extension.
8. Paper-supporting release after advisor approval/publication.

## Public / Private Boundary

Public here:

- high-level explanations,
- repository organization,
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

## Limitations

This repository does not yet include:

- a complete mobile manipulator model,
- a tested line-scan sensor model,
- real robot experiments,
- full motion planning,
- full state estimation,
- benchmark comparisons,
- paper-level results.

## Citation / Acknowledgment

This project is motivated by robotics research in active perception, coverage planning, mobile manipulation, inspection, and visual/spectral sensing. Cite any papers, datasets, courses, or libraries used when implementation details are added.

## Rights and Reuse

This repository is shared as a public academic portfolio/scaffold. Unless a separate open-source license is explicitly added, all rights are reserved by the author.
