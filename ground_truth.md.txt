# Ground-Truth Heuristics

## Project
An Integrated Distributed Framework for Automated Lifecycle Classification
and Redundancy Mitigation in Large-Scale Repositories

## 1. Purpose

This document describes the heuristic approach used to assign preliminary
lifecycle labels to files based on their recorded activity.

The labels are generated using predefined rules and are not independently
verified ground-truth labels.

## 2. Features Used

- file_path: Identifies a file in the processed dataset.
- access_count: Number of recorded file-access events for the file.
- last_access: Timestamp of the last recorded file-access event.
- days_since_last_access: Time between the last recorded access and the
  reference timestamp.

## 3. Reference Timestamp

The latest valid event timestamp in the processed dataset is used as the
reference timestamp for calculating inactivity.

The dataset covers approximately July 7–10, 2017.

## 4. Classification Rules

### Class 0: Active (Hot Tier)

Conditions:
- Days since last access <= 30.
- Access count >= 5.

### Class 1: Rarely Accessed (Cool Tier)

Condition:
- Days since last access is between 31 and 120 days, inclusive.

### Class 2: Potentially Obsolete

Conditions:
- Days since last access >= 121.
- Access count <= 1.

This label indicates a candidate for further review, not permission to delete.

### Needs Review

Files that do not satisfy any of the three classification rules are assigned
to Needs Review.

Files without a recorded access timestamp require special attention because
their last access cannot be established from the available sample.

## 5. Initial Results

The initial classification produced:

- Active: 535 files.
- Rarely Accessed: 0 files.
- Potentially Obsolete: 0 files.
- Needs Review: 7,447 files.
- Total unique file paths: 7,982.

## 6. Limitations

1. The observation period is approximately three days.
2. The 30-day and 121-day thresholds cannot be independently validated using
   this sample alone.
3. Recorded access counts may not represent complete lifetime activity.
4. The heuristic labels are not independent ground truth.
5. No file-size field is available in the processed dataset.
6. A file without recorded access events is not necessarily obsolete.

## 7. Future Validation

Future evaluation should use a longer observation period or independently
verified lifecycle labels.

Classification performance should be evaluated using suitable metrics when
reliable reference labels become available.

Potentially obsolete files must undergo additional checks before archival
or deletion.