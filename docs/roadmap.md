# Roadmap

## Stage 0: Public scaffold

Goal: organize the public-facing project structure.

Status: in progress. The repository now has README structure, public/private boundary notes, candidate metrics, and toy script scaffolding.

## Stage 1: Minimal synthetic line-scan example

Goal: simulate a line-scan camera over a simple 2D/3D target.

Status: started with `src/toy_line_scan_coverage_demo.py`.

## Stage 2: Coverage metric

Goal: compute coverage ratio, missing coverage, and visibility violations.

Status: started with synthetic coverage ratio and per-row coverage summaries.

## Stage 3: Baseline planner

Goal: implement a naive raster scan or fixed-standoff baseline.

Status: planned.

## Stage 4: Robot-aware planning

Goal: introduce mobile base and manipulator constraints.

Status: planned.

## Stage 5: ROS2/MoveIt integration

Goal: connect planning outputs to a robot simulation pipeline.

Status: planned.

## Stage 6: Uncertainty-aware extension

Goal: evaluate coverage degradation under pose uncertainty.

Status: private/future work.

## Stage 7: Paper-supporting release

Goal: release code after advisor approval and/or publication.

Status: future milestone.
