# Line-Scan Mobile Manipulator Demo

An early application scaffold for line-scan-aware motion planning and surface coverage. **No complete runnable demo or validated planner is included yet.**

## Place in the research

The broader research studies [perception-aware motion planning across robot platforms and sensing modalities](https://github.com/WikiGenius). This repository explores one possible application: moving a sensor to acquire useful surface observations.

RGB-D and hyperspectral sensing are initial interests. A mobile manipulator is a candidate platform for this example, not a restriction on the overall research.

A line-scan proxy can help study acquisition geometry and motion-dependent sampling. It does not, by itself, validate hyperspectral image formation or spectral measurement quality.

## Planned first experiment

1. Define a synthetic surface and an explicit scan-line observation model.
2. Implement a fixed raster-scan baseline.
3. Measure coverage, missed area, overlap, and motion cost.
4. Add sensing constraints and compare the outcome under the same conditions.
5. Introduce robot feasibility and pose uncertainty in separate, documented extensions.

Visibility, viewing angle, standoff, speed, and sampling requirements must be defined for the selected sensor and task. Proposed metrics are not results.

## Supporting projects

| Project | Potential contribution |
| --- | --- |
| [WMM planning and tracking](https://github.com/WikiGenius/wmm-planning-and-tracking) | Coordinated motion generation and tracking |
| [Screw Theory Toolkit](https://github.com/WikiGenius/RoboticScrewTheoryToolkit) | Kinematic calculations |
| [Husky image capture](https://github.com/WikiGenius/husky-gazebo-image-capture) | Image and pose data-collection patterns |
| [GTSAM SLAM Vision](https://github.com/WikiGenius/GTSAM_SLAM_VISION) | Estimation experiments |
| [Research reading map](https://github.com/WikiGenius/research-reading-map) | Reading categories and comparison questions |

These components are not integrated into this scaffold. Hardware experiments, benchmark comparisons, and publication results remain future work.

## Sharing

Public examples should be self-contained and use shareable data. Confidential datasets, collaborator feedback, and unpublished manuscripts remain private until approved for release. No open-source license has been assigned to this scaffold.
