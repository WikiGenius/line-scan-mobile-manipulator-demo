# Related Repositories

This repository is the public anchor for structure-aware line-scan / RGB-hyperspectral active scanning with a mobile manipulator.

## Public Research Layers

| Layer | Repo | What belongs there |
|---|---|---|
| Main active scanning demo | [`line-scan-mobile-manipulator-demo`](https://github.com/WikiGenius/line-scan-mobile-manipulator-demo) | Public-safe scanning planner scaffold, coverage metrics, ROS2 demo wiring, synthetic examples, figures, and media. |
| Mobile-manipulator execution | [`ros2-moveit-grasping-demo`](https://github.com/WikiGenius/ros2-moveit-grasping-demo) | MoveIt2 planning, Cartesian motion, gripper control, grasp/retreat execution patterns. |
| ROS2 mobile robotics | [`ros2-mobile-robotics-labs`](https://github.com/WikiGenius/ros2-mobile-robotics-labs) | ROS2 nodes, launch files, URDF, RViz, simulation workflow, and mobile robot basics. |
| Control foundation | [`robotics-control-learning-labs`](https://github.com/WikiGenius/robotics-control-learning-labs) | LQR, observers, state-space modeling, and control baselines. |
| Trajectory tracking | [`wmm-trajectory-tracking`](https://github.com/WikiGenius/wmm-trajectory-tracking) | Whole-body mobile-manipulator tracking experiments and future tracking plots. |
| State estimation | [`GTSAM_SLAM_VISION`](https://github.com/WikiGenius/GTSAM_SLAM_VISION) | Factor-graph visual estimation and SLAM-style optimization experiments. |
| Visual state-estimation scaffold | [`orb_slam_demo`](https://github.com/WikiGenius/orb_slam_demo) | ROS2 scaffold for ORB-SLAM-style visual state-estimation experiments. |
| 3D perception / view synthesis | [`nerf-lab`](https://github.com/WikiGenius/nerf-lab) | NeRF and ray-based intuition for view coverage, scene representation, and active perception. |
| Literature map | [`research-reading-map`](https://github.com/WikiGenius/research-reading-map) | Paper taxonomy, reading path, reproduction ideas, and method relationships. |

## Private Research Layer

Keep the following private until publication or public release is appropriate:

- exact unpublished structure-aware planning algorithms,
- RGB/hyperspectral datasets and calibration details,
- raw experiment logs and ablations,
- paper figures before submission/preprint decisions,
- parameter sweeps and reviewer-response experiments.

## Public Release Pattern

When a private experiment is ready to become public, release a simplified version here:

1. Use a synthetic or non-sensitive scene.
2. Replace private datasets only with approved public-safe examples.
3. Expose baseline planners and metrics first.
4. Keep paper-specific details private until the publication strategy is clear.
5. Add screenshots, GIFs, or plots under `media/` and `results/`.
6. Explain what is simplified in the `Limitations` section.

## Why NeRF Belongs Nearby

`nerf-lab` is not the main research repo, but it supports the perception side of the story. NeRF-style and ray-based methods help reason about viewpoints, coverage, visibility, scene representation, and image formation. That makes it relevant as background evidence for active scanning and visual/spectral perception.
