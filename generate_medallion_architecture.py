import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil

# Typography & High-Res settings
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# Canvas dimensions (Portrait layout strictly matching user's reference image)
fig, ax = plt.subplots(figsize=(10.4, 13.8), dpi=300)
ax.set_xlim(0, 10.4)
ax.set_ylim(0, 13.8)
ax.axis('off')

# Background color
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

# Geometric & Layout Constants
XC = 4.6       # Main vertical axis center
XL = 2.7       # Left column center
XR = 6.5       # Right column center
CW = 7.2       # Main container width (x: 1.0 -> 8.2)

def draw_arrow(start_x, start_y, end_x, end_y, color='#0284C7', lw=1.8):
    ax.annotate(
        '', xy=(end_x, end_y), xytext=(start_x, start_y),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=14)
    )

def draw_side_pill(box_right, box_center_y, pill_text, pill_color='#FFF7ED', border_color='#EA580C', text_color='#C2410C', pw=1.40, ph=0.42):
    # Dotted line from container to pill
    ax.plot([box_right, box_right + 0.30], [box_center_y, box_center_y],
            color=border_color, linestyle=':', linewidth=2.0)
    # Side pill
    px = box_right + 0.30
    py = box_center_y - ph / 2
    side_pill = patches.FancyBboxPatch(
        (px, py), pw, ph,
        boxstyle="round,pad=0.04,rounding_size=0.12",
        facecolor=pill_color, edgecolor=border_color, linewidth=1.6
    )
    ax.add_patch(side_pill)
    ax.text(px + pw / 2, box_center_y, pill_text, ha='center', va='center',
            fontsize=9.2, fontweight='bold', color=text_color)

# -------------------------------------------------------------
# 1. TOP TITLE BANNER (Dark Blue Pill)
# -------------------------------------------------------------
title_box = patches.FancyBboxPatch(
    (0.5, 12.90), 9.4, 0.64,
    boxstyle="round,pad=0.06,rounding_size=0.14",
    facecolor='#034EA2', edgecolor='none'
)
ax.add_patch(title_box)
ax.text(5.2, 13.22, "Novel Distributed Lifecycle Classification & Redundancy Mitigation Architecture",
        ha='center', va='center', fontsize=12.0, fontweight='bold', color='#FFFFFF')

# -------------------------------------------------------------
# 2. RAW SOURCES HEADER BOX
# -------------------------------------------------------------
raw_hdr = patches.FancyBboxPatch(
    (XC - 2.0, 12.05), 4.0, 0.48,
    boxstyle="round,pad=0.04,rounding_size=0.12",
    facecolor='#EBF4FB', edgecolor='#0284C7', linewidth=1.8
)
ax.add_patch(raw_hdr)
ax.text(XC, 12.29, "RAW SOURCES", ha='center', va='center',
        fontsize=11.5, fontweight='bold', color='#034EA2')

# Downward fork connector from RAW SOURCES into the two input boxes
ax.plot([XC, XC], [12.05, 11.75], color='#0284C7', linewidth=1.8)
ax.plot([XL, XR], [11.75, 11.75], color='#0284C7', linewidth=1.8)
draw_arrow(XL, 11.75, XL, 11.45, color='#0284C7', lw=1.8)
draw_arrow(XR, 11.75, XR, 11.45, color='#0284C7', lw=1.8)

# -------------------------------------------------------------
# 3. LEVEL 1: TWO RAW INPUT BOXES
# -------------------------------------------------------------
# Left Box: CLUE-LDS Enterprise Logs
box1_left = patches.FancyBboxPatch(
    (1.0, 10.55), 3.4, 0.90,
    boxstyle="round,pad=0.04,rounding_size=0.12",
    facecolor='#EFF8FF', edgecolor='#0284C7', linewidth=1.8
)
ax.add_patch(box1_left)
ax.text(XL, 11.10, "CLUE-LDS Enterprise Logs", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#034EA2')
ax.text(XL, 10.78, "(100,000 JSON records)", ha='center', va='center', fontsize=9.2, color='#334155')

# Right Box: Repository Audit Metadata
box1_right = patches.FancyBboxPatch(
    (4.8, 10.55), 3.4, 0.90,
    boxstyle="round,pad=0.04,rounding_size=0.12",
    facecolor='#EFF8FF', edgecolor='#0284C7', linewidth=1.8
)
ax.add_patch(box1_right)
ax.text(XR, 11.10, "Repository Audit Metadata", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#034EA2')
ax.text(XR, 10.78, "(FilePath, Timestamp, Operations)", ha='center', va='center', fontsize=9.2, color='#334155')

# Convergence connector from Two Boxes into Bronze Layer
ax.plot([XL, XL], [10.55, 10.25], color='#0284C7', linewidth=1.8)
ax.plot([XR, XR], [10.55, 10.25], color='#0284C7', linewidth=1.8)
ax.plot([XL, XR], [10.25, 10.25], color='#0284C7', linewidth=1.8)
draw_arrow(XC, 10.25, XC, 9.78, color='#0284C7', lw=1.8)

# -------------------------------------------------------------
# 4. LEVEL 2: BRONZE LAYER (Orange Medallion Container)
# -------------------------------------------------------------
bronze_box = patches.FancyBboxPatch(
    (1.0, 8.65), CW, 1.10,
    boxstyle="round,pad=0.06,rounding_size=0.14",
    facecolor='#FFF7ED', edgecolor='#EA580C', linewidth=2.0
)
ax.add_patch(bronze_box)

# Bronze Layer Top Tab Pill (Centered at x=XC)
bronze_tab = patches.FancyBboxPatch(
    (XC - 0.95, 9.55), 1.9, 0.38,
    boxstyle="round,pad=0.02,rounding_size=0.10",
    facecolor='#C2410C', edgecolor='none'
)
ax.add_patch(bronze_tab)
ax.text(XC, 9.74, "Bronze Layer", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')

# Inner Ingestion Box
inner_bronze = patches.FancyBboxPatch(
    (1.35, 8.82), 6.5, 0.65,
    boxstyle="round,pad=0.04,rounding_size=0.10",
    facecolor='#FFFFFF', edgecolor='#FB923C', linewidth=1.5
)
ax.add_patch(inner_bronze)
ax.text(XC, 9.24, "Apache Spark & HDFS (Ingestion)", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0F172A')
ax.text(XC, 8.98, "Multi-partition RDD streaming landing • Case-sensitive schema resolution", ha='center', va='center', fontsize=8.2, color='#475569')

# Side Ingest Pill
draw_side_pill(8.2, 9.20, "Ingest", pill_color='#FFF7ED', border_color='#EA580C', text_color='#C2410C')

# Arrow pointing down to Silver Layer
draw_arrow(XC, 8.65, XC, 8.10, color='#0284C7')

# -------------------------------------------------------------
# 5. LEVEL 3: SILVER LAYER (Blue Medallion Container)
# -------------------------------------------------------------
silver_box = patches.FancyBboxPatch(
    (1.0, 6.00), CW, 2.05,
    boxstyle="round,pad=0.06,rounding_size=0.14",
    facecolor='#F0F9FF', edgecolor='#0284C7', linewidth=2.0
)
ax.add_patch(silver_box)

# Silver Layer Top Tab Pill
silver_tab = patches.FancyBboxPatch(
    (XC - 0.95, 7.85), 1.9, 0.38,
    boxstyle="round,pad=0.02,rounding_size=0.10",
    facecolor='#034EA2', edgecolor='none'
)
ax.add_patch(silver_tab)
ax.text(XC, 8.04, "Silver Layer", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')

# Silver Box 1: PySpark Preprocessing
inner_silver1 = patches.FancyBboxPatch(
    (1.35, 7.02), 6.5, 0.72,
    boxstyle="round,pad=0.04,rounding_size=0.10",
    facecolor='#FFFFFF', edgecolor='#38BDF8', linewidth=1.5
)
ax.add_patch(inner_silver1)
ax.text(XC, 7.48, "PySpark Preprocessing", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#034EA2')
ax.text(XC, 7.20, "Cleaning  •  Standardization  •  UTC Timestamp Parsing  •  Missing Value Imputation", ha='center', va='center', fontsize=8.2, color='#334155')

# Silver Box 2: Entity Aggregation & Temporal Windowing
inner_silver2 = patches.FancyBboxPatch(
    (1.35, 6.18), 6.5, 0.68,
    boxstyle="round,pad=0.04,rounding_size=0.10",
    facecolor='#FFFFFF', edgecolor='#38BDF8', linewidth=1.5
)
ax.add_patch(inner_silver2)
ax.text(XC, 6.62, "Entity Aggregation & Temporal Join", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#034EA2')
ax.text(XC, 6.35, "(groupBy FilePath  •  2,000 File Entities  •  Inactivity Window Delta-t Calculation)", ha='center', va='center', fontsize=8.2, color='#475569')

# Side Load & Process Pill
draw_side_pill(8.2, 7.02, "Load & Process", pill_color='#EFF6FF', border_color='#0284C7', text_color='#034EA2')

# Arrow pointing down to Gold Layer
draw_arrow(XC, 6.00, XC, 5.42, color='#0284C7')

# -------------------------------------------------------------
# 6. LEVEL 4: GOLD LAYER (Gold Medallion Container)
# -------------------------------------------------------------
gold_box = patches.FancyBboxPatch(
    (1.0, 4.05), CW, 1.32,
    boxstyle="round,pad=0.06,rounding_size=0.14",
    facecolor='#FEFCE8', edgecolor='#EAB308', linewidth=2.0
)
ax.add_patch(gold_box)

# Gold Layer Top Tab Pill
gold_tab = patches.FancyBboxPatch(
    (XC - 0.95, 5.18), 1.9, 0.38,
    boxstyle="round,pad=0.02,rounding_size=0.10",
    facecolor='#CA8A04', edgecolor='none'
)
ax.add_patch(gold_tab)
ax.text(XC, 5.37, "Gold Layer", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')

# Gold Box 1 (Left): Temporal Feature Extraction
inner_gold1 = patches.FancyBboxPatch(
    (1.35, 4.22), 3.10, 0.86,
    boxstyle="round,pad=0.04,rounding_size=0.10",
    facecolor='#FFFFFF', edgecolor='#FACC15', linewidth=1.5
)
ax.add_patch(inner_gold1)
ax.text(2.90, 4.82, "Temporal Feature Store", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#854D0E')
ax.text(2.90, 4.56, "Store lifecycle degradation features", ha='center', va='center', fontsize=8.0, color='#475569')
ax.text(2.90, 4.36, "(Recency Delta-t, Frequency, File Size)", ha='center', va='center', fontsize=7.5, color='#64748B')

# Gold Box 2 (Right): IEEE Ground-Truth Heuristics
inner_gold2 = patches.FancyBboxPatch(
    (4.75, 4.22), 3.10, 0.86,
    boxstyle="round,pad=0.04,rounding_size=0.10",
    facecolor='#FFFFFF', edgecolor='#FACC15', linewidth=1.5
)
ax.add_patch(inner_gold2)
ax.text(6.30, 4.82, "Ground-Truth Heuristics", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#854D0E')
ax.text(6.30, 4.56, "IEEE Digital Waste Boundary Rules", ha='center', va='center', fontsize=8.0, color='#475569')
ax.text(6.30, 4.36, "(Hot Active, Cool Inactive, ROT Obsolete)", ha='center', va='center', fontsize=7.5, color='#64748B')

# Arrow pointing down to Fused Dataset
draw_arrow(XC, 4.05, XC, 3.58, color='#0284C7')

# -------------------------------------------------------------
# 7. LEVEL 5: UNIFIED LIFECYCLE DATASET (Pink Pill)
# -------------------------------------------------------------
fused_pill = patches.FancyBboxPatch(
    (XC - 2.9, 3.12), 5.8, 0.44,
    boxstyle="round,pad=0.04,rounding_size=0.12",
    facecolor='#FCE7F3', edgecolor='#EC4899', linewidth=1.8
)
ax.add_patch(fused_pill)
ax.text(XC, 3.34, "Fused Enterprise Repository Lifecycle ML Dataset",
        ha='center', va='center', fontsize=10.2, fontweight='bold', color='#9D174D')

# Arrow pointing down to ML Pipeline
draw_arrow(XC, 3.12, XC, 2.68, color='#0284C7')

# -------------------------------------------------------------
# 8. LEVEL 6: ML & EVALUATION PIPELINE (Blue Outline Box)
# -------------------------------------------------------------
ml_box = patches.FancyBboxPatch(
    (1.0, 1.45), CW, 1.20,
    boxstyle="round,pad=0.06,rounding_size=0.14",
    facecolor='#EFF6FF', edgecolor='#0284C7', linewidth=1.8
)
ax.add_patch(ml_box)

ax.text(XC, 2.42, "Distributed ML Benchmarking & Novel Deep Learning Pipeline",
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#034EA2')
ax.text(XC, 2.14, "• Temporal Stratified Split (80% Train, 20% Evaluation) across Spark Partitions",
        ha='center', va='center', fontsize=8.3, color='#334155')
ax.text(XC, 1.90, "• 5 Classical ML Baselines: Logistic Regression, SVM, Decision Tree, Random Forest, GBT",
        ha='center', va='center', fontsize=8.3, color='#334155')
ax.text(XC, 1.64, "• Proposed Architecture: Temporal BiLSTM with Multi-Head Attention (96.40% Accuracy, F1: 0.9638)",
        ha='center', va='center', fontsize=8.5, fontweight='bold', color='#6D28D9')

# Two branching arrows pointing down to Final Targets
draw_arrow(XL, 1.45, XL, 1.02, color='#0284C7')
draw_arrow(XR, 1.45, XR, 1.02, color='#0284C7')

# -------------------------------------------------------------
# 9. LEVEL 7: FINAL TARGET OUTPUTS (Two Bottom Boxes)
# -------------------------------------------------------------
# Left: Automated Storage Tiering
out_left = patches.FancyBboxPatch(
    (1.0, 0.22), 3.4, 0.78,
    boxstyle="round,pad=0.04,rounding_size=0.12",
    facecolor='#E0F2F1', edgecolor='#00897B', linewidth=1.8
)
ax.add_patch(out_left)
ax.text(XL, 0.75, "Automated Storage Tiering", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#004D40')
ax.text(XL, 0.50, "S3 Standard  •  S3 Infrequent Access  •  Glacier", ha='center', va='center', fontsize=8.0, color='#00695C')
ax.text(XL, 0.33, "(Hot, Cool, Obsolete Policy Enforcement)", ha='center', va='center', fontsize=7.2, color='#455A64')

# Right: Storage Reclamation & Dashboard
out_right = patches.FancyBboxPatch(
    (4.8, 0.22), 3.4, 0.78,
    boxstyle="round,pad=0.04,rounding_size=0.12",
    facecolor='#E0F2F1', edgecolor='#00897B', linewidth=1.8
)
ax.add_patch(out_right)
ax.text(XR, 0.75, "Digital Waste & Cost Reclamation", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#004D40')
ax.text(XR, 0.50, ">90% Inactive Data Storage Optimized", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#00695C')
ax.text(XR, 0.33, "(Real-Time Redundancy Mitigation Telemetry)", ha='center', va='center', fontsize=7.2, color='#455A64')

plt.tight_layout()

# Save diagram
out_png = "system_medallion_architecture.png"
fig.savefig(out_png, dpi=300, bbox_inches='tight')

# Also sync to system_architecture_diagram.png and Review 2 folder
fig.savefig("system_architecture_diagram.png", dpi=300, bbox_inches='tight')

review2_folder = r"C:\Users\harsh\Desktop\Big data\Review 2"
if os.path.exists(review2_folder):
    shutil.copy(out_png, os.path.join(review2_folder, out_png))
    shutil.copy(out_png, os.path.join(review2_folder, "system_architecture_diagram.png"))

plt.close(fig)
print("SUCCESS: Exact medallion-style architecture diagram generated and synced!")
