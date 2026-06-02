# Project Scope

## What This Project Studies

This project studies future public-facing work on line-scan-aware active scanning and coverage planning for mobile manipulators.

The target research direction is robot motion that actively acquires useful visual or spectral information while respecting:

- line-scan / pushbroom-like sensing geometry,
- coverage and visibility constraints,
- mobile base and manipulator kinematics,
- collision and reachability limits,
- state-estimation and pose uncertainty,
- real-time planning/control requirements.

## What Is Currently Public

The public repository currently includes:

- project organization,
- README and documentation,
- candidate metrics,
- public/private boundary notes,
- related-repository organization.

## What Is Intentionally Private

The following should remain private until advisor approval, publication, or sanitized release:

- full unpublished planning method,
- real RGB/hyperspectral lab data,
- calibration and experiment details,
- paper drafts,
- advisor/collaborator notes,
- detailed gap analysis,
- full ablation studies,
- confidential experiment results.

## What Is Not Yet Implemented

This repository does not yet include:

- a tested line-scan sensor model,
- a complete mobile-manipulator planner,
- ROS2/MoveIt integration,
- real robot or lab-data experiments,
- collision checking,
- uncertainty-aware planning,
- benchmark comparisons.

## What Would Count As Success

Public success milestones:

1. A minimal public-safe line-scan example runs from a clean checkout.
2. Coverage metrics are computed and saved.
3. A naive baseline planner is added.
4. Public plots/GIFs show coverage behavior on synthetic data.
5. ROS2 simulation scaffolding connects planned scan poses to robot motion.
6. Post-publication code exposes enough to reproduce the paper without leaking private material too early.
