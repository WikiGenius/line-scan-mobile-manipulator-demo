# Terminology

## Active Scanning

Planning robot motion to acquire useful sensor information, not only to reach a target pose.

## Line-Scan Sensing

A sensing mode where information is collected along a narrow line or row at each instant. Hyperspectral pushbroom cameras are a motivating example, but this public repo uses simplified RGB/line-scan proxies.

## Pushbroom Acquisition

A scanning process where a sensor collects one spatial line at a time while motion sweeps the line across the target.

## Coverage

The fraction of a target region that has been observed by the scan.

## Visibility Constraint

A geometric rule that determines whether the sensor can see a target sample from a candidate pose.

## Scan Pose

A robot, camera, or end-effector pose from which a line or region of the target may be observed.

## Baseline Planner

A simple comparison method such as raster scanning, fixed-standoff scanning, or a greedy coverage heuristic.

## Public Scaffold

An early repository that organizes safe public structure and documentation before full research code is ready to release.
