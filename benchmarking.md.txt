# Benchmarking and Baseline Evaluation

## 1. Project Title

An Integrated Distributed Framework for Automated Lifecycle Classification
and Redundancy Mitigation in Large-Scale Repositories

## 2. Objective

The objective of this evaluation is to establish a baseline for file lifecycle
classification using file activity events from the processed dataset.

The baseline summarizes event frequencies, unique file paths, and the results
of the initial rule-based classification.

## 3. Dataset Baseline

The processed dataset contains 100,000 records.

The observed event period is approximately July 7–10, 2017.

| Metric | Observed Result |
|---|---:|
| Total records | 100,000 |
| Unique file paths | 7,982 |
| File-access events | 33,389 |
| File-write events | 4,306 |
| File-update events | 3,954 |
| Version-deletion events | 3,673 |
| File-creation events | 352 |
| File-deletion events | 58 |
| Permission-change events | 6 |

## 4. Initial Lifecycle Classification Results

The initial rule-based classification produced the following results.

| Lifecycle Category | Number of Files |
|---|---:|
| Class 0 - Active (Hot Tier) | 535 |
| Class 1 - Rarely Accessed (Cool Tier) | 0 |
| Class 2 - Potentially Obsolete | 0 |
| Needs Review | 7,447 |
| Total | 7,982 |

The active category contains files that satisfy the documented access-count
and inactivity conditions.

The Needs Review category contains files that do not satisfy the current
classification rules.

## 5. Baseline Interpretation

The initial results show that 535 of the 7,982 unique file paths were classified
as Active, while 7,447 were assigned to Needs Review.

No files were classified as Rarely Accessed or Potentially Obsolete.

The short observation period limits the ability to evaluate the 30-day and
121-day inactivity thresholds.

Therefore, these results represent preliminary rule-based classifications
rather than independently validated lifecycle labels.

## 6. Limitations

1. The observation period covers approximately three days.
2. The 30-day and 121-day inactivity thresholds cannot be independently
   validated using this sample alone.
3. Recorded access counts may not represent each file's complete lifetime
   activity.
4. The dataset does not contain a file-size field.
5. Storage savings and redundancy reduction have not yet been measured.
6. No comparative algorithm benchmark has been completed.

## 7. Future Benchmarking Work

The following evaluations remain to be performed:

1. Compare the rule-based classifier with a justified baseline method.
2. Evaluate classification consistency and suitable performance metrics.
3. Investigate redundancy using an appropriate duplicate-detection method.
4. Measure storage savings only if reliable file-size and redundancy data
   become available.
5. Evaluate distributed processing performance if the framework is implemented
   using distributed tools.

## 8. Conclusion

This baseline evaluation establishes the observed file-event distribution
and initial lifecycle classification results.

Further evaluation using a longer observation period and suitable comparison
methods is required before drawing conclusions about classification
effectiveness, redundancy mitigation, or storage-cost reduction.
### Classification Execution Time

The rule-based classification step took approximately
0.044904 seconds in one observed execution.

This measurement covers the application of the classification
rules to the prepared file profiles. It excludes dataset loading
and earlier feature preparation. Execution time may vary across runs
and hardware configurations.

## 9. Comparative Execution-Time Experiment

The baseline method assigns every file profile to the Needs Review
category. The rule-based method applies the documented lifecycle
classification rules to each prepared file profile.

| Method | Execution Time (seconds) | Files Processed |
|---|---:|---:|
| Baseline | 0.000303 | 7,982 |
| Rule-based | 0.043297 | 7,982 |

These measurements represent one execution and may vary with hardware
and system conditions.

The methods perform different amounts of work. Therefore, their
execution times should not be interpreted as a definitive performance
comparison. The baseline is a simple reference method rather than an
equivalent classification algorithm.

Classification accuracy has not been established because independently
verified ground-truth labels are unavailable.
## 10. Access Count Distribution Analysis

The 7,982 unique file paths were grouped according to their
recorded file-access counts.

| Access Count Group | Number of Files |
|---|---:|
| Zero recorded accesses | 4,103 |
| 1–4 recorded accesses | 3,344 |
| 5 or more recorded accesses | 535 |
| Total | 7,982 |

The results show that 535 files meet the minimum access-count
condition for the Active category.

The remaining files require further evaluation under the
lifecycle rules. A file with no recorded access events must not
automatically be considered obsolete.

Because the available dataset covers approximately three days,
the access counts may not represent complete lifetime activity.
Longer-term historical data is required to validate the inactivity
thresholds.

## 11. Preliminary Inactivity Threshold Analysis

A threshold-distribution experiment was conducted using
the classified file profile containing 7,982 unique files.

The number of files exceeding different inactivity
thresholds was calculated.

| Inactivity Threshold | Files Exceeding Threshold |
|---|---:|
| 1 day | 769 |
| 2 days | 559 |
| 3 days | 38 |
| 7 days | 0 |
| 14 days | 0 |
| 30 days | 0 |
| 60 days | 0 |
| 90 days | 0 |
| 121 days | 0 |

The results show that the number of files exceeding the
inactivity threshold decreases as the threshold increases.

The dataset covers approximately three days of recorded
activity. Consequently, it does not provide sufficient
observation time to validate long-term inactivity
thresholds such as 30 or 121 days.

Furthermore, the absence of recorded access events does
not establish that a file is obsolete.

Therefore, this experiment provides preliminary
descriptive evidence about the observed dataset rather
than a definitive evaluation of classification accuracy.

## 12. Classification Sensitivity Analysis

A preliminary classification sensitivity experiment was
conducted on 7,982 unique file profiles using inactivity
thresholds of 1, 2, 3, 7, 30, and 121 days.

| Threshold (Days) | Active | Potentially Obsolete | Needs Review |
|---:|---:|---:|---:|
| 1 | 523 | 731 | 6728 |
| 2 | 523 | 521 | 6938 |
| 3 | 531 | 21 | 7430 |
| 7 | 535 | 0 | 7447 |
| 30 | 535 | 0 | 7447 |
| 121 | 535 | 0 | 7447 |

The results show that the number of files classified as
potentially obsolete decreases as the inactivity threshold
increases. At thresholds of seven days and above, no files
were classified as potentially obsolete under the simplified
experimental rules.

These findings indicate that classification outcomes are
sensitive to the selected inactivity threshold.

However, the experiment uses simplified rules and does not
reproduce every category and condition in the original
lifecycle classifier. The dataset also covers only
approximately three days of recorded activity.

Therefore, these results are preliminary and do not
establish the accuracy of the original classifier or prove
that any file is genuinely obsolete.

## 13. Obsolete Threshold Sensitivity Analysis

A preliminary sensitivity experiment was conducted using
7,982 unique file profiles. The obsolete threshold was
varied while the Active and Cool Tier rules were kept fixed.

| Obsolete Threshold (Days) | Active | Cool Tier | Potentially Obsolete | Needs Review |
|---:|---:|---:|---:|---:|
| 1 | 535 | 0 | 731 | 6716 |
| 2 | 535 | 0 | 521 | 6926 |
| 3 | 535 | 0 | 21 | 7426 |
| 7 | 535 | 0 | 0 | 7447 |
| 30 | 535 | 0 | 0 | 7447 |
| 121 | 535 | 0 | 0 | 7447 |

The results show that the number of files classified as
potentially obsolete decreases as the tested threshold
increases. No files were classified as potentially
obsolete at thresholds of seven days or more.

The dataset contains approximately three days of recorded
activity. Consequently, it cannot validate long-term
inactivity thresholds or establish whether files are
genuinely obsolete.

This experiment uses modified classification rules and
should be interpreted as preliminary sensitivity analysis,
not as a direct evaluation of the original classifier.
Independent ground-truth labels are unavailable, so
classification accuracy cannot be established.

## 14. Comparative Evaluation of Existing Approaches

Different approaches can be used for file lifecycle classification
and storage management. The following comparison summarizes their
general characteristics and the approach implemented in this project.

| Approach | Main Idea | Advantages | Limitations |
|---|---|---|---|
| Manual File Management | Users decide which files to retain or remove | Simple to implement | Time-consuming and dependent on user decisions |
| Rule-Based Classification | Uses predefined thresholds and file activity information | Simple, transparent, and easy to implement | Results depend on selected rules and thresholds |
| Machine Learning-Based Classification | Learns patterns from labelled historical data | Can learn more complex patterns | Requires suitable training data and reliable labels |
| Storage Lifecycle Management | Moves data between storage tiers according to policies | Can support efficient storage utilization and cost management | Requires appropriate policies and reliable activity information |

### Evaluation of the Proposed Approach

The project implements a rule-based file lifecycle classification
approach using recorded file activity and access counts.

Its main advantage is interpretability: the classification rules
are explicit and can be inspected or modified easily.

The current implementation classified 535 files as Active (Hot Tier)
and 7,447 files as Needs Review out of 7,982 unique files.

The dataset covers approximately three days of recorded activity.
Therefore, the experiment cannot validate long-term inactivity
thresholds or establish whether files are genuinely obsolete.

The baseline experiment assigns every file to Needs Review.
Although execution times were measured, this baseline does not
provide a meaningful comparison of classification accuracy.

Independent ground-truth labels are unavailable. Consequently,
classification accuracy and superiority over machine learning
methods have not been established.

The proposed approach should therefore be considered a preliminary,
interpretable classification framework that requires further
validation using longer-term activity records and independently
verified labels.
