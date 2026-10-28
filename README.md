# An Integrated Distributed Framework for Automated Lifecycle Classification and Redundancy Mitigation in Large-Scale Repositories

**Course:** 21CSC314P - Big Data Essentials | SRM Institute of Science and Technology  
**Lead Author:** S Harshan (Reg. No: `RA24110310013`) | **Batch:** 10  
**Faculty Guide:** Dr. Shanmuganathan V (Assistant Professor)  

---

## 📁 Repository Directory Structure

```plaintext
BDE_Project/
├── code/                             # 🚀 DEDICATED CODING & IMPLEMENTATION PART (OPEN IN VS CODE)
│   ├── lifecycle_classification.ipynb  # Interactive Jupyter Notebook with all 3 graphs rendered inline
│   ├── main_pipeline.py              # Standalone Python pipeline (run live to show interactive plots)
│   ├── requirements.txt              # Environment dependencies (NumPy, Pandas, Seaborn, Matplotlib)
│   └── README.md                     # Code execution instructions & Viva reference
├── results/                          # 📊 EVALUATION RESULTS & PUBLICATION-READY VISUALS (300 DPI)
│   ├── preprocessing_distribution.png# Slide 7: Inactivity distribution and class balance
│   ├── confusion_matrix.png          # Slide 9: 96.40% Accuracy heatmap for Proposed DL model
│   ├── model_comparison.png          # Slide 10: Novel DL vs 5 ML baselines comparison chart
│   ├── model_evaluation_metrics.csv  # Full benchmarking comparison table
│   └── preprocessing_results_table.csv # Ingestion & feature engineering audit table
├── diagrams/                         # 🏗️ SYSTEM ARCHITECTURE & WORKFLOW DIAGRAMS
│   ├── system_architecture_diagram.png # 4-Tier Medallion Architecture (Bronze/Silver/Gold)
│   ├── system_workflow_diagram.png   # End-to-end distributed system workflow pipeline
│   ├── generate_medallion_architecture.py # Generator script for Medallion architecture
│   └── generate_workflow_diagram.py  # Generator script for Workflow architecture
├── data/                             # 💾 DATASETS & REPOSITORY LOG PROFILES
│   ├── clue.json                     # Raw enterprise streaming event log (14.86 GB, ignored in git)
│   ├── classified_file_profile.csv   # Aggregated entity activity profiles
│   ├── file_activity_profile.csv     # File activity logs
│   └── *.csv                         # Benchmark and sensitivity analysis profiles
├── docs/                             # 📑 PROJECT DOCUMENTATION & RESEARCH NOTES
│   ├── literature_review.md          # Comprehensive literature review
│   ├── lifecycle_rules.md            # IEEE Big Data tiering heuristic rules
│   ├── ground_truth.md               # Storage tier boundary definitions
│   └── benchmarking.md               # Baseline algorithm comparison notes
└── _archive_tools/                   # 📦 ARCHIVED UTILITIES & ONE-OFF GENERATION SCRIPTS
```

---

## ⚡ Quick Start: Implementation Part for Faculty Evaluation

### Option 1: Jupyter Notebook (Recommended)
Open VS Code, navigate to `code/` (or project root), and open:
```plaintext
lifecycle_classification.ipynb
```
All outputs and the 3 deliverable graphs are **already rendered**! To re-run live in front of faculty, simply click **"Run All"**.

### Option 2: Python Script (Terminal Execution)
In the VS Code terminal:
```bash
cd code
python main_pipeline.py
```
This logs all pipeline stages, prints the performance table, and pops up all 3 graphs interactively.
