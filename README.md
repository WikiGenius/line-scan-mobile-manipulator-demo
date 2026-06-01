# Line-Scan Mobile Manipulator Demo

## Overview
This repository is a public scaffold for a line-scan-aware active scanning demo with a mobile manipulator. The project is intended to show how a robot can plan scanning viewpoints while considering visibility, coverage, and task constraints.

The current repository is intentionally lightweight. It documents the planned public structure and will be expanded with source code, launch files, results, and media as the demo matures.

## Research/Engineering Motivation
Line-scan and inspection tasks appear in robotics applications such as surface inspection, industrial metrology, mobile manipulation, and active perception. A mobile manipulator must reason about where to move, how to orient the sensor, and how to maintain coverage while respecting robot reachability and visibility constraints.

This repository is designed to become a clean public demo for that planning problem without exposing unpublished experiment details.

## Features
- Public project structure for a ROS 2 mobile manipulation demo.
- Planned line-scan-aware viewpoint and coverage planning workflow.
- Planned integration points for mobile base motion, manipulator motion, and sensor visibility checks.
- Documentation-first organization for future reproducible experiments.

## Method
The planned method decomposes active scanning into a small set of engineering modules:

1. Represent the target surface or inspection region.
2. Generate candidate scanning viewpoints or trajectories.
3. Check visibility and coverage constraints.
4. Filter candidates using robot reachability and motion constraints.
5. Execute or simulate the selected scan plan with a mobile manipulator.
6. Log coverage and planning metrics for comparison.

Detailed algorithms and unpublished experiment settings will be added only when they are ready for public release.

## Installation
This is currently a scaffold repository. Once ROS 2 source files are added, the intended workflow is:

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
Planned launch command after the first runnable demo is added:

```bash
ros2 launch line_scan_mobile_manipulator_demo demo.launch.py
```

Until launch files are added, use this repository as a public project outline and documentation scaffold.

## Results
Results will be added under `results/` and public demo media under `media/`.

Planned artifacts:

- Coverage plots.
- Viewpoint-selection visualizations.
- RViz screenshots or GIFs.
- Scan trajectory and constraint summaries.

## Limitations
- The public repository currently contains scaffolding, not a complete runnable demo.
- Sensor, robot, and environment models are not yet included.
- The public method will be simplified compared with any unpublished research experiments.

## Roadmap
- [ ] Add baseline scanning planner.
- [ ] Add visibility and coverage metrics.
- [ ] Add ROS 2 launch workflow.
- [ ] Add experiment logs and public demo media.
- [ ] Add paper/report link when available.

## Citation / Acknowledgment
This project is motivated by robotics research in active perception, coverage planning, mobile manipulation, and inspection. Cite any papers, datasets, or libraries used when implementation details are added.
