# Line-Scan Mobile Manipulator Demo

## Overview
This repository is the main public scaffold for a line-scan-aware active scanning demo with a mobile manipulator. The project is intended to show how a robot can plan scanning viewpoints while considering visibility, coverage, sensing geometry, robot reachability, and task constraints.

The repository now includes a small synthetic coverage-metric starter script. Unpublished algorithms, datasets, and exact experiment settings should remain private until they are ready for release.

## Repository Role
This is the public portfolio anchor for the research direction: structure-aware planning and control for mobile manipulation.

It should eventually connect these layers:

| Layer | Related repo | Role |
|---|---|---|
| Mobile manipulation execution | [`ros2-moveit-grasping-demo`](https://github.com/WikiGenius/ros2-moveit-grasping-demo) | MoveIt2 planning, Cartesian approach, gripper control, grasping, and retreat motion. |
| ROS2 mobile robotics | [`ros2-mobile-robotics-labs`](https://github.com/WikiGenius/ros2-mobile-robotics-labs) | ROS2 nodes, launch files, URDF/RViz, and simulation learning labs. |
| Control foundation | [`robotics-control-learning-labs`](https://github.com/WikiGenius/robotics-control-learning-labs) | State-space, LQR, observers, and reproducible control examples. |
| Trajectory tracking | [`wmm-trajectory-tracking`](https://github.com/WikiGenius/wmm-trajectory-tracking) | Whole-body mobile-manipulator tracking support. |
| State estimation | [`GTSAM_SLAM_VISION`](https://github.com/WikiGenius/GTSAM_SLAM_VISION) | Factor-graph visual SLAM and pose-estimation experiments. |
| Visual representation | [`nerf-lab`](https://github.com/WikiGenius/nerf-lab) | NeRF / view-synthesis intuition for viewpoint coverage and 3D perception. |
| Literature map | [`research-reading-map`](https://github.com/WikiGenius/research-reading-map) | Paper taxonomy and research roadmap for active perception, coverage, estimation, and control. |

## Research/Engineering Motivation
Line-scan and inspection tasks appear in robotics applications such as surface inspection, industrial metrology, agricultural scanning, mobile manipulation, and active perception. A mobile manipulator must reason about where to move, how to orient the sensor, and how to maintain coverage while respecting robot reachability and visibility constraints.

The larger research question is how robot motion can be designed not only to reach a target, but also to acquire useful visual or spectral information under physical, geometric, sensing, and uncertainty constraints.

This repository is designed to become a clean public demo for that planning problem without exposing unpublished experiment details.

## Features
- Public project structure for a ROS 2 mobile manipulation demo.
- Synthetic starter script for cumulative coverage bookkeeping.
- Planned line-scan-aware viewpoint and coverage planning workflow.
- Planned integration points for mobile base motion, manipulator motion, and sensor visibility checks.
- Planned links to state estimation, control, and 3D perception support repositories.
- Documentation-first organization for future reproducible experiments.

## Method
The planned method decomposes active scanning into a small set of engineering modules:

1. Represent the target surface or inspection region.
2. Generate candidate scanning viewpoints or trajectories.
3. Check visibility, viewing angle, and coverage constraints.
4. Filter candidates using robot reachability and motion constraints.
5. Execute or simulate the selected scan plan with a mobile manipulator.
6. Log coverage, tracking, and planning metrics for comparison.

The current toy script only demonstrates step 3 and cumulative coverage bookkeeping on synthetic data. Detailed algorithms and unpublished experiment settings will be added only when they are ready for public release.

## Installation
For the starter Python script:

```bash
git clone https://github.com/WikiGenius/line-scan-mobile-manipulator-demo.git
cd line-scan-mobile-manipulator-demo
python scripts/coverage_metric_demo.py
```

Once ROS 2 source files are added, the intended workflow is:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/WikiGenius/line-scan-mobile-manipulator-demo.git
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select line_scan_mobile_manipulator_demo
source install/setup.bash
```

## Run
Run the current toy coverage metric:

```bash
python scripts/coverage_metric_demo.py
```

Planned launch command after the first ROS2 demo is added:

```bash
ros2 launch line_scan_mobile_manipulator_demo demo.launch.py
```

## Results
The starter script writes:

```text
results/coverage_metric_demo.csv
```

Future results will be added under `results/` and public demo media under `media/`.

Planned artifacts:

- Coverage plots.
- Viewpoint-selection visualizations.
- RViz screenshots or GIFs.
- Scan trajectory and constraint summaries.
- Tracking and estimation summary metrics.

## Limitations
- The current script is a synthetic coverage bookkeeping example, not a complete planner.
- Sensor, robot, and environment models are not yet included.
- The public method will be simplified compared with any unpublished research experiments.
- Private datasets, paper-specific ablations, and exact unpublished algorithm details are intentionally excluded.

## Roadmap
- [x] Add synthetic coverage-metric starter script.
- [ ] Add baseline scanning planner.
- [ ] Add visibility and coverage metrics.
- [ ] Add ROS 2 launch workflow.
- [ ] Add a synthetic scan target or simple public scene.
- [ ] Add experiment logs and public demo media.
- [ ] Add paper/report link when available.

## Citation / Acknowledgment
This project is motivated by robotics research in active perception, coverage planning, mobile manipulation, inspection, and visual/spectral sensing. Cite any papers, datasets, or libraries used when implementation details are added.

## Related Organization
See [`docs/related-repositories.md`](docs/related-repositories.md) for the public/private organization around this main demo and [`docs/method-sketch.md`](docs/method-sketch.md) for the starter method sketch.
