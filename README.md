# An Integrated Distributed Framework for Automated Lifecycle Classification and Redundancy Mitigation in Large-Scale Repositories

**Course:** 21CSC314P – Big Data Essentials  
**Department:** Department of Networking and Communications | School of Computing  
**Institution:** SRM Institute of Science and Technology  
**Faculty Guide:** Dr. Shanmuganathan V (Assistant Professor)

---

## 👥 Team Members & Roles

| S.No | Registration No. | Student Name | Technical Role |
| :---: | :---: | :--- | :--- |
| 1 | RA2411031010008 | **Shanmuga Priyan P** | Data Ingestion & Distributed Preprocessing |
| 2 | RA2411031010012 | **V Dharani** | Literature Benchmarking & Ground-Truth Heuristics |
| 3 | RA2411031010013 | **S Harshan** | Big Data Feature Engineering, 5-ML Benchmarking & Novel Deep Learning Architecture |
| 4 | RA2411031010030 | **Rameshvar S** | Redundancy Mitigation Engine & Dashboard Assembly |

---

## 📌 1. Preprocessing Pipeline & Results (Slide 6 & 7)

Enterprise cloud activity logs (Zenodo CLUE-LDS dataset) were preprocessed through distributed PySpark ingestion, removing corrupt attributes and aggregating unstructured events into file entities:

| Preprocessing Stage / Attribute | Raw State (CLUE-LDS Ingestion) | Cleaned / Processed State | Methodology & Action |
| :--- | :--- | :--- | :--- |
| **Total Event Records** | 100,000 JSON log entries | 2,000 Aggregated File Entities | Aggregated by unique repository `FilePath` |
| **Missing / Null File Paths** | 54,262 records without path | 0 (100% Validated) | Filtered non-file administrative telemetry |
| **Timestamp Normalization** | Unparsed ISO-8601 strings | Standardized Datetime / UNIX | Parsed to compute temporal recency ($\Delta t$) |
| **Feature Representation** | Unstructured text parameters | 3-D Dense Vectors $[\Delta t, FF, SS]$ | VectorAssembler feature scaling |
| **Lifecycle Class Target** | Unlabeled streaming logs | Multi-class (Hot: 32%, Cool: 44%, ROT: 24%) | Applied IEEE ground-truth heuristic rules |

---

## 🧠 2. Novel Proposed Deep Learning Architecture (Slide 8)

### **Temporal BiLSTM with Multi-Head Attention Mechanism (`BiLSTM-Attention`)**
While classical ML relies solely on static scalar sums, enterprise file access exhibits sequential dependencies (burst writes, periodic cron updates, gradual dormancy decay). Our proposed architecture captures both forward temporal decay and backward interaction recurrence:

$$\vec{h}_t = \text{LSTM}_{fwd}(x_t, \vec{h}_{t-1}), \quad \overleftarrow{h}_t = \text{LSTM}_{bwd}(x_t, \overleftarrow{h}_{t+1})$$
$$H_t = [\vec{h}_t \,\|\, \overleftarrow{h}_t]$$
$$\alpha_t = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V, \quad c = \sum_{t} \alpha_t H_t$$
$$\hat{y} = \text{softmax}(W_c c + b_c)$$

* **Forward/Backward BiLSTM:** Learns bi-directional temporal access trends.
* **Multi-Head Self-Attention:** Dynamically focuses on burst activity vs prolonged dormancy periods.
* **Output Classification:** 3-way softmax determining storage tiers (Hot, Cool, Obsolete/ROT).

---

## 📊 3. Benchmarking: Proposed Novel Deep Learning vs 5 Classical ML Baselines (Slide 10)

| Category | Evaluated Algorithm / Model | Accuracy (%) | Precision | Recall | F1-Score | Training Time (s) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| Classical ML | **Logistic Regression** | 81.20% | 0.8125 | 0.8120 | 0.8112 | 3.84 s |
| Classical ML | **Support Vector Machine (Linear/RBF SVM)** | 85.90% | 0.8598 | 0.8590 | 0.8584 | 4.12 s |
| Classical ML | **Decision Tree Classifier ($d=8$)** | 88.40% | 0.8847 | 0.8840 | 0.8839 | 2.15 s |
| Classical ML | **Distributed Random Forest (50 Trees)** | 92.80% | 0.9285 | 0.9280 | 0.9279 | 6.45 s |
| Classical ML | **Gradient Boosted Trees (GBT / XGBoost)** | 94.10% | 0.9416 | 0.9410 | 0.9408 | 14.72 s |
| **Proposed Novel DL** | **Proposed Novel Temporal BiLSTM-Attention** | **96.40%** | **0.9648** | **0.9640** | **0.9638** | **18.30 s** |

### Key Benchmark Insights:
1. **Deep Learning Superiority (+2.30% to +15.20% gain):** The Novel BiLSTM-Attention model outperforms the strongest boosting ensemble (GBT at 94.10%) and all tree/linear baselines.
2. **Attention Weighting:** The multi-head attention mechanism effectively filters out sporadic single-access noise that trips up classical decision trees.

---

## 🖼️ 4. Visual Deliverables

- **`preprocessing_distribution.png`**: Inactivity day distribution ($\Delta t$) and balanced 3-class target breakdown.
- **`confusion_matrix.png`**: Multi-class confusion matrix verifying **96.40% accuracy** for the Proposed Novel Deep Learning model.
- **`model_comparison.png`**: Comparative accuracy bar chart evaluating the Novel Deep Learning model against all 5 ML baselines.

---

## 🚀 5. How to Run

```bash
# 1. Run the benchmarking and visualization pipeline
python update_dl_pipeline.py

# 2. Open the complete Jupyter / Colab Notebook
jupyter notebook lifecycle_classification.ipynb
```
