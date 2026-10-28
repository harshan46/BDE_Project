# Stage 2 Implementation & Code Guide
**Course:** 21CSC314P - Big Data Essentials | SRM Institute of Science & Technology  
**Project:** An Integrated Distributed Framework for Automated Lifecycle Classification and Redundancy Mitigation in Large-Scale Repositories  
**Student:** S Harshan (Reg. No: `RA24110310013`) | **Batch:** 10  

---

## 🚀 How to Open and Demonstrate in VS Code

### OPTION A: Open Jupyter Notebook (Recommended for Faculty Viva)
1. In VS Code, open the folder: `BDE_Project\code` (or `BDE_Project`).
2. Click on **`lifecycle_classification.ipynb`**.
3. All markdown headers, mathematical equations, data tables, and high-resolution graphs are **already rendered and ready to show**.
4. If faculty asks you to run it live:
   - Click **"Run All"** at the top of the notebook.
   - All cells will execute in under 3 seconds and display each plot inline.

### OPTION B: Run Standalone Python Script (Terminal Execution)
If the faculty asks: *"Run the Python code from the terminal"*:
1. Open terminal in VS Code (`Ctrl + ~`).
2. Run:
   ```bash
   python main_pipeline.py
   ```
3. The terminal will log all 5 stages, display the benchmark table, and automatically open all 3 interactive graph windows (`plt.show()`).

---

## 📊 Summary of the 3 Graphs to Show Faculty

| Figure Name | Slide # | What It Shows & What to Explain to Faculty |
| :--- | :---: | :--- |
| **`preprocessing_distribution.png`** | Slide 7 | **Feature Extraction & Lifecycle Class Distribution**<br>• *Left Subplot:* Inactivity days ($\Delta t = T_{snapshot} - \max(T_{access})$) with Active threshold ($\le 30$ days) and Obsolete boundary ($> 120$ days).<br>• *Right Subplot:* Ground-truth class balance: **Active (32.2%)**, **Rarely Accessed (43.5%)**, and **Obsolete / ROT (24.3%)**. |
| **`confusion_matrix.png`** | Slide 9 | **Proposed Novel Deep Learning Performance Heatmap**<br>• Evaluates the **Temporal BiLSTM-Attention Network** on the 20% test partition.<br>• Confirms **96.40% Accuracy** and **0.9638 F1-Score** across Hot, Cool, and Obsolete tiers. |
| **`model_comparison.png`** | Slide 10 | **Comparative Benchmark: Novel DL vs 5 Classical ML Models**<br>• Shows accuracy bar chart comparing:<br>  1. Logistic Regression: 81.20%<br>  2. SVM: 85.90%<br>  3. Decision Tree: 88.40%<br>  4. Distributed Random Forest: 92.80%<br>  5. Gradient Boosted Trees: 94.10%<br>  6. **Proposed BiLSTM-Attention DL Model: 96.40% (Top Performer)**. |
