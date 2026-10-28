\# Lifecycle Classification Rules



\## Project

An Integrated Distributed Framework for Automated Lifecycle Classification and Redundancy Mitigation in Large-Scale Repositories



\## Purpose

These rules classify files into lifecycle categories based on inactivity and access frequency. The thresholds are provisional and require validation before operational use.



\## Class 0: Active (Hot Tier)

Conditions:

\- Inactivity is less than or equal to 30 days.

\- Access count is greater than or equal to 5.



Purpose:

Identify files that are frequently accessed and may benefit from fast storage.



\## Class 1: Rarely Accessed (Cool Tier)

Condition:

\- Inactivity is between 31 and 120 days, inclusive.



Purpose:

Identify files that have not been accessed recently and may be suitable for a lower-cost storage tier.



\## Class 2: Potentially Obsolete (Archive/Purge)

Conditions:

\- Inactivity is greater than or equal to 121 days.

\- Access count is less than or equal to 1.



Purpose:

Flag files for further review as potential archival or cleanup candidates.



Important:

This category does not mean a file is safe to delete. Manual review and appropriate safeguards are required before any deletion.



\## Additional Category: Needs Review

Files that do not satisfy any of the three rules are assigned to Needs Review.



This includes records with missing or unsuitable feature values.



\## Dataset Findings

The processed sample contains:

\- 100,000 records.

\- 33,389 file-access events.

\- 3,879 unique files with recorded access events.

\- 1,514 files with fewer than two recorded accesses.

\- 535 files with at least five recorded accesses.



The observed event period is approximately July 7–10, 2017.



\## Limitations

1\. The available sample covers only approximately three days.

2\. The sample cannot independently validate the 30-day and 121-day inactivity thresholds.

3\. The access counts represent recorded events in the available sample, not necessarily each file's complete lifetime activity.

4\. The dataset does not contain a file-size field.

5\. The thresholds are provisional and must be evaluated before operational use.



\## Handoff to Stage 2

The classification function is implemented in lifecycle\_rules.py.



The Stage 2 developer should:

1\. Aggregate file activity using the processed dataset.

2\. Calculate access frequency and days since last access.

3\. Apply these lifecycle rules consistently.

4\. Evaluate the resulting labels and document limitations.

5\. Avoid claiming independent validation when labels are generated from the same heuristic rules.

