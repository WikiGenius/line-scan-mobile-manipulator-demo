# Line-Scan Mobile Manipulator Demo

This repository is a public scaffold for organizing future work on line-scan-aware active scanning and coverage planning for mobile manipulators.

It is part of my broader PhD research direction in robotics, control, motion planning, state estimation, and active sensing.

## Purpose

The purpose of this repository is to provide a clean public-facing structure for future non-confidential demos related to line-scan-aware robotic scanning.

This repository is not intended to expose unpublished PhD algorithms, private paper drafts, real lab data, advisor notes, or detailed private gap analysis.

## Relation to My PhD Direction

This repository connects to my research direction through:

- mobile manipulation,
- active sensing,
- motion planning,
- geometric visibility constraints,
- line-scan / one-row RGB proxy sensing for hyperspectral pushbroom acquisition,
- state estimation,
- uncertainty-aware planning,
- control and execution.

## Maturity Level

**Current status:** Public research scaffold / early-stage organization repo.

This repository is intended to organize the public-facing structure of the project and host simplified, non-confidential demos. It does not yet represent a complete research implementation or a validated planner.

### Implemented Now

- [x] Repository structure
- [x] README and project organization
- [x] Public/private boundary documentation
- [ ] Minimal synthetic line-scan demo
- [ ] Coverage plot or GIF
- [ ] Baseline comparison
- [ ] ROS2 / MoveIt integration
- [ ] Paper-supporting implementation

### Planned Later

- Minimal synthetic line-scan example
- Coverage metric computation
- Naive raster-scan baseline
- Mobile manipulator model
- Visibility constraint checks
- ROS2 / MoveIt integration
- Uncertainty-aware experiments
- Paper-supporting implementation after advisor approval or publication

### Intentionally Private

The following materials are intentionally not included in this public repository:

- unpublished research algorithm,
- full problem formulation details,
- private paper drafts,
- advisor and collaborator notes,
- real lab data,
- detailed gap analysis,
- full ablation studies,
- confidential experiment results.

## Current Runnable Artifact

No complete runnable demo is included yet. The next planned step is to add a minimal synthetic line-scan coverage example.

## Roadmap

### Stage 0: Public Scaffold

Organize the public-facing repository structure and explain the project scope.

### Stage 1: Minimal Synthetic Line-Scan Example

Create a simple non-confidential toy example that simulates a scan line over a synthetic surface or grid.

### Stage 2: Coverage Metrics

Compute basic coverage metrics such as covered area, missing coverage, and coverage ratio.

### Stage 3: Baseline Planner

Implement a simple raster-scan or fixed-standoff baseline.

### Stage 4: Robot-Aware Planning

Introduce mobile base and manipulator kinematic constraints.

### Stage 5: ROS2 / MoveIt Integration

Connect planning outputs to a ROS2 / MoveIt-style robot simulation pipeline.

### Stage 6: Uncertainty-Aware Extension

Evaluate the effect of pose uncertainty on scan coverage and visibility.

### Stage 7: Paper-Supporting Release

Release paper-supporting code only after advisor approval, publication, or explicit release decision.

## Candidate Metrics

Future non-confidential demos may report:

- coverage ratio,
- missing coverage,
- scan redundancy,
- path length,
- number of scan poses,
- visibility violation count,
- collision count,
- computation time,
- robustness under pose noise.

## Limitations

This repository is currently an early-stage public scaffold. It does not yet include:

- a complete mobile manipulator model,
- a validated line-scan sensor model,
- real robot experiments,
- full motion planning,
- full state estimation,
- benchmark comparisons,
- paper-level results.

## Rights and Reuse

This repository is shared as a public academic portfolio/scaffold.

Unless a separate open-source license is explicitly added, all rights are reserved by the author.
