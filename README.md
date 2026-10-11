# An Integrated Distributed Framework for Automated Lifecycle Classification and Redundancy Mitigation in Large-Scale Repositories

**Course:** 21CSC314P – Big Data Essentials  
**Department:** Department of Networking and Communications | School of Computing  
**Institution:** SRM Institute of Science and Technology  
**Faculty Guide:** Dr. Shanmuganathan V (Assistant Professor)

---

## 👥 Team Members

| S.No | Registration No. | Student Name | Technical Role |
| :---: | :---: | :--- | :--- |
| 1 | RA2411031010008 | **Shanmuga Priyan P** | Data Ingestion & Distributed Preprocessing |
| 2 | RA2411031010012 | **V Dharani** | Literature Benchmarking & Ground-Truth Heuristics |
| 3 | RA2411031010013 | **S Harshan** | Big Data Feature Engineering & Distributed ML (Spark MLlib) |
| 4 | RA2411031010030 | **Rameshvar S** | Redundancy Mitigation Engine & Dashboard Assembly |

---

## 📌 Project Overview
Large enterprise cloud storage repositories suffer from explosive data growth, redundant copies, and obsolete/stale files (ROT - Redundant, Obsolete, Trivial data). This framework provides an end-to-end distributed Big Data pipeline that:
1. Ingests raw cloud entity activity logs (Zenodo CLUE-LDS dataset).
2. Profiles and aggregates event streams into file-level entity profiles.
3. Performs temporal feature engineering (Inactivity Days $\Delta t$, Access Frequency $FF$, File Size $SS$).
4. Classifies repository files into three dynamic lifecycle storage tiers using a **Distributed Apache Spark MLlib Random Forest Classifier**:
   - **Class 0: Active (Hot Tier)** – Inactivity $\le 30$ days and access frequency $\ge 5$.
   - **Class 1: Rarely Accessed (Cool Tier)** – Inactivity between 31 and 120 days.
   - **Class 2: Potentially Obsolete / ROT (Archive Tier)** – Inactivity $> 120$ days or access frequency $\le 2$.
5. Automates tier migration policies (e.g., AWS S3 Standard $\to$ S3 Infrequent Access $\to$ S3 Glacier Deep Archive) to reclaim storage costs.

---

## 🔬 Distributed ML Architecture & Results (Stage 2 Lead: S Harshan)

### Mathematical Formulation
$$\hat{C}_{rf}(x) = \text{argmax}_{k \in \{0, 1, 2\}} \sum_{b=1}^{B} I(C_b(x) = k)$$
- **Ensemble Size:** 50 Distributed Decision Trees ($B=50$)
- **Tree Depth:** Maximum depth of 10 ($d_{\text{max}}=10$)
- **Distributed Evaluation:** 80/20 train-test split across Apache Spark partitions

### Performance Comparison

| Model | Accuracy (%) | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| Logistic Regression | 81.20% | 0.8125 | 0.8120 | 0.8112 |
| Decision Tree ($d_{\text{max}}=8$) | 88.40% | 0.8847 | 0.8840 | 0.8839 |
| Gradient Boosted Trees (GBT) | 91.50% | 0.9156 | 0.9150 | 0.9148 |
| **Proposed Distributed Random Forest** | **93.70%** | **0.9378** | **0.9370** | **0.9370** |

---

## 📊 Visual Deliverables

- **`preprocessing_distribution.png`**: Inactivity day distribution and lifecycle class balance.
- **`confusion_matrix.png`**: Multi-class confusion matrix verifying 93.7% classification accuracy.
- **`model_comparison.png`**: Comparative accuracy benchmark across distributed ML algorithms.

---

## 🚀 How to Run

### Requirements
```bash
pip install pyspark pandas numpy matplotlib seaborn
```

### Run the Pipeline
```bash
python harshan_ml_pipeline.py
```

Or open and run the Jupyter Notebook:
```bash
jupyter notebook lifecycle_classification.ipynb
```
