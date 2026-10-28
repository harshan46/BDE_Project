import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Typography & High-Res settings
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 16:9 widescreen canvas
fig, ax = plt.subplots(figsize=(16, 8.6), dpi=300)
ax.set_xlim(0, 16)
ax.set_ylim(0, 8.6)
ax.axis('off')

# Background
fig.patch.set_facecolor('#F8FAFC')
ax.set_facecolor('#F8FAFC')

# -------------------------------------------------------------
# 1. WORKFLOW TITLE BANNER
# -------------------------------------------------------------
header_box = patches.FancyBboxPatch(
    (0.5, 7.45), 15.0, 0.85,
    boxstyle="round,pad=0.08,rounding_size=0.14",
    facecolor='#0F172A', edgecolor='none'
)
ax.add_patch(header_box)

ax.text(8.0, 7.97, "END-TO-END SYSTEM WORKFLOW PIPELINE",
        ha='center', va='center', fontsize=17, fontweight='bold', color='#FFFFFF')
ax.text(8.0, 7.67, "Automated Lifecycle Classification and Cloud Redundancy Mitigation Workflow",
        ha='center', va='center', fontsize=10.5, color='#94A3B8')

# -------------------------------------------------------------
# 2. WORKFLOW STEP DEFINITIONS
# -------------------------------------------------------------
w_y = 1.35
w_h = 5.75

# Step 1: Raw Ingestion
s1_x = 0.5
s1_w = 2.65
card1 = patches.FancyBboxPatch((s1_x, w_y), s1_w, w_h, boxstyle="round,pad=0.06,rounding_size=0.15",
                              facecolor='#FFFFFF', edgecolor='#3B82F6', linewidth=2.0)
ax.add_patch(card1)
pill1 = patches.FancyBboxPatch((s1_x + 0.2, w_y + w_h - 0.55), s1_w - 0.4, 0.40,
                              boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#2563EB', edgecolor='none')
ax.add_patch(pill1)
ax.text(s1_x + s1_w/2, w_y + w_h - 0.35, "STEP 01: INGESTION", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')
ax.text(s1_x + s1_w/2, w_y + w_h - 0.95, "Raw Enterprise\nAudit Logs", ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A', linespacing=1.2)
ax.plot([s1_x + 0.3, s1_x + s1_w - 0.3], [w_y + w_h - 1.45, w_y + w_h - 1.45], color='#DBEAFE', linewidth=1.2)

items1 = [
    ("Source Repository:", "Zenodo CLUE-LDS Dataset"),
    ("Raw Volume:", "100,000 JSON Event Logs"),
    ("Data Format:", "Unstructured Event Streams"),
    ("Captured Attributes:", "Timestamps, FilePath, Actions\n(read, write, update, delete)")
]
curr_y = w_y + w_h - 1.80
for label, desc in items1:
    ax.text(s1_x + 0.22, curr_y, label, fontsize=8.2, fontweight='bold', color='#1E40AF')
    ax.text(s1_x + 0.22, curr_y - 0.28, desc, fontsize=7.8, color='#475569', linespacing=1.15)
    curr_y -= 0.76

out1 = patches.FancyBboxPatch((s1_x + 0.2, w_y + 0.20), s1_w - 0.4, 0.45,
                             boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#EFF6FF', edgecolor='#3B82F6', linewidth=1.2)
ax.add_patch(out1)
ax.text(s1_x + s1_w/2, w_y + 0.42, "Output: Raw JSON Stream", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#1D4ED8')

# Step 2: Distributed PySpark ETL
s2_x = 3.60
s2_w = 2.65
card2 = patches.FancyBboxPatch((s2_x, w_y), s2_w, w_h, boxstyle="round,pad=0.06,rounding_size=0.15",
                              facecolor='#FFFFFF', edgecolor='#0D9488', linewidth=2.0)
ax.add_patch(card2)
pill2 = patches.FancyBboxPatch((s2_x + 0.2, w_y + w_h - 0.55), s2_w - 0.4, 0.40,
                              boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#0D9488', edgecolor='none')
ax.add_patch(pill2)
ax.text(s2_x + s2_w/2, w_y + w_h - 0.35, "STEP 02: PYSPARK ETL", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')
ax.text(s2_x + s2_w/2, w_y + w_h - 0.95, "Distributed Cleaning\n& Normalization", ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A', linespacing=1.2)
ax.plot([s2_x + 0.3, s2_x + s2_w - 0.3], [w_y + w_h - 1.45, w_y + w_h - 1.45], color='#CCFBF1', linewidth=1.2)

items2 = [
    ("Schema Resolution:", "Strict Case-Sensitivity\nspark.sql.caseSensitive=true"),
    ("Data Cleaning:", "Filter null/corrupt records\nand admin telemetry"),
    ("Timestamp Parsing:", "Standardized to ISO-8601\nUTC Datetime format"),
    ("Worker Allocation:", "In-Memory Cached Distributed\nDataFrames across partitions")
]
curr_y = w_y + w_h - 1.80
for label, desc in items2:
    ax.text(s2_x + 0.22, curr_y, label, fontsize=8.2, fontweight='bold', color='#0F766E')
    ax.text(s2_x + 0.22, curr_y - 0.28, desc, fontsize=7.8, color='#475569', linespacing=1.15)
    curr_y -= 0.76

out2 = patches.FancyBboxPatch((s2_x + 0.2, w_y + 0.20), s2_w - 0.4, 0.45,
                             boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#F0FDFA', edgecolor='#0D9488', linewidth=1.2)
ax.add_patch(out2)
ax.text(s2_x + s2_w/2, w_y + 0.42, "Output: Cleaned DataFrame", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#0F766E')

# Step 3: Feature Engineering
s3_x = 6.70
s3_w = 2.65
card3 = patches.FancyBboxPatch((s3_x, w_y), s3_w, w_h, boxstyle="round,pad=0.06,rounding_size=0.15",
                              facecolor='#FFFFFF', edgecolor='#0284C7', linewidth=2.0)
ax.add_patch(card3)
pill3 = patches.FancyBboxPatch((s3_x + 0.2, w_y + w_h - 0.55), s3_w - 0.4, 0.40,
                              boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#0284C7', edgecolor='none')
ax.add_patch(pill3)
ax.text(s3_x + s3_w/2, w_y + w_h - 0.35, "STEP 03: FEATURES", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')
ax.text(s3_x + s3_w/2, w_y + w_h - 0.95, "Entity Aggregation\n& Temporal Features", ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A', linespacing=1.2)
ax.plot([s3_x + 0.3, s3_x + s3_w - 0.3], [w_y + w_h - 1.45, w_y + w_h - 1.45], color='#E0F2FE', linewidth=1.2)

items3 = [
    ("Entity Aggregation:", "Grouped by FilePath\ninto 2,000 unique file entities"),
    ("Inactivity Days (Delta-t):", "T_snapshot - max(T_access)\nElapsed days since last access"),
    ("Access Frequency (FF):", "Total interactions count\nacross the audit window"),
    ("Dense Vector Assembly:", "PySpark VectorAssembler:\nFeature Vector [Delta-t, FF, SS]")
]
curr_y = w_y + w_h - 1.80
for label, desc in items3:
    ax.text(s3_x + 0.22, curr_y, label, fontsize=8.2, fontweight='bold', color='#0369A1')
    ax.text(s3_x + 0.22, curr_y - 0.28, desc, fontsize=7.8, color='#475569', linespacing=1.15)
    curr_y -= 0.76

out3 = patches.FancyBboxPatch((s3_x + 0.2, w_y + 0.20), s3_w - 0.4, 0.45,
                             boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#F0F9FF', edgecolor='#0284C7', linewidth=1.2)
ax.add_patch(out3)
ax.text(s3_x + s3_w/2, w_y + 0.42, "Output: 3-D Feature Vectors", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#0284C7')

# Step 4: Novel Deep Learning Model
s4_x = 9.80
s4_w = 2.70
card4 = patches.FancyBboxPatch((s4_x, w_y), s4_w, w_h, boxstyle="round,pad=0.06,rounding_size=0.15",
                              facecolor='#FFFFFF', edgecolor='#7C3AED', linewidth=2.0)
ax.add_patch(card4)
pill4 = patches.FancyBboxPatch((s4_x + 0.2, w_y + w_h - 0.55), s4_w - 0.4, 0.40,
                              boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#7C3AED', edgecolor='none')
ax.add_patch(pill4)
ax.text(s4_x + s4_w/2, w_y + w_h - 0.35, "STEP 04: NOVEL DL", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')
ax.text(s4_x + s4_w/2, w_y + w_h - 0.95, "Temporal BiLSTM\nMulti-Head Attention", ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A', linespacing=1.2)
ax.plot([s4_x + 0.3, s4_x + s4_w - 0.3], [w_y + w_h - 1.45, w_y + w_h - 1.45], color='#EDE9FE', linewidth=1.2)

items4 = [
    ("Sequence Modeling:", "Bi-directional LSTM learns\nforward & backward access trends"),
    ("Multi-Head Attention:", "Dynamically weights burst reads\nvs prolonged dormancy"),
    ("5-ML Benchmarking:", "Outperforms LR, SVM, DT,\nRandom Forest, and GBT"),
    ("Evaluation Metrics:", "Accuracy: 96.40% | F1: 0.9638\nPrecision: 0.965 | Recall: 0.964")
]
curr_y = w_y + w_h - 1.80
for label, desc in items4:
    ax.text(s4_x + 0.22, curr_y, label, fontsize=8.2, fontweight='bold', color='#6D28D9')
    ax.text(s4_x + 0.22, curr_y - 0.28, desc, fontsize=7.8, color='#475569', linespacing=1.15)
    curr_y -= 0.76

out4 = patches.FancyBboxPatch((s4_x + 0.2, w_y + 0.20), s4_w - 0.4, 0.45,
                             boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#F5F3FF', edgecolor='#7C3AED', linewidth=1.2)
ax.add_patch(out4)
ax.text(s4_x + s4_w/2, w_y + 0.42, "Output: Lifecycle Predictions", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#6D28D9')

# Step 5: Tier Migration & Outcome (Branching Workflow)
s5_x = 12.90
s5_w = 2.60
card5 = patches.FancyBboxPatch((s5_x, w_y), s5_w, w_h, boxstyle="round,pad=0.06,rounding_size=0.15",
                              facecolor='#FFFFFF', edgecolor='#059669', linewidth=2.0)
ax.add_patch(card5)
pill5 = patches.FancyBboxPatch((s5_x + 0.2, w_y + w_h - 0.55), s5_w - 0.4, 0.40,
                              boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#059669', edgecolor='none')
ax.add_patch(pill5)
ax.text(s5_x + s5_w/2, w_y + w_h - 0.35, "STEP 05: TIERING", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')
ax.text(s5_x + s5_w/2, w_y + w_h - 0.95, "Automated Tiering\n& Cost Optimization", ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A', linespacing=1.2)
ax.plot([s5_x + 0.3, s5_x + s5_w - 0.3], [w_y + w_h - 1.45, w_y + w_h - 1.45], color='#D1FAE5', linewidth=1.2)

# 3 Branching Tiers
tiers = [
    ("Class 0: Active (Hot)", "AWS S3 Standard ($0.023/GB)\nHigh-throughput active storage", "#DCFCE7", "#16A34A", "#15803D"),
    ("Class 1: Cool", "AWS S3 Infrequent Access\n($0.0125/GB) Intermediate tier", "#FEF3C7", "#D97706", "#B45309"),
    ("Class 2: Obsolete / ROT", "AWS S3 Glacier Deep Archive\n($0.00099/GB) >90% Cost Saved", "#FEE2E2", "#DC2626", "#B91C1C")
]
t_y = w_y + w_h - 1.65
for t_title, t_desc, bg_col, brd_col, txt_col in tiers:
    t_box = patches.FancyBboxPatch((s5_x + 0.18, t_y - 0.84), s5_w - 0.36, 0.92,
                                  boxstyle="round,pad=0.03,rounding_size=0.08",
                                  facecolor=bg_col, edgecolor=brd_col, linewidth=1.2)
    ax.add_patch(t_box)
    ax.text(s5_x + 0.30, t_y - 0.22, t_title, fontsize=8.2, fontweight='bold', color=txt_col)
    ax.text(s5_x + 0.30, t_y - 0.58, t_desc, fontsize=7.4, color='#334155', linespacing=1.18)
    t_y -= 1.08

out5 = patches.FancyBboxPatch((s5_x + 0.18, w_y + 0.20), s5_w - 0.36, 0.45,
                             boxstyle="round,pad=0.02,rounding_size=0.08", facecolor='#059669', edgecolor='none')
ax.add_patch(out5)
ax.text(s5_x + s5_w/2, w_y + 0.42, "Reclaimed: >90% Cost", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#FFFFFF')

# -------------------------------------------------------------
# 3. SLEEK WORKFLOW CONNECTOR ARROWS BETWEEN STEPS
# -------------------------------------------------------------
arrow_coords = [
    (s1_x + s1_w, s2_x),
    (s2_x + s2_w, s3_x),
    (s3_x + s3_w, s4_x),
    (s4_x + s4_w, s5_x)
]

for x_left, x_right in arrow_coords:
    mid_x = (x_left + x_right) / 2
    mid_y = w_y + (w_h / 2) + 0.15
    
    # Outer circle badge
    circle = patches.Circle((mid_x, mid_y), 0.18, facecolor='#0F172A', edgecolor='#FFFFFF', linewidth=1.8, zorder=5)
    ax.add_patch(circle)
    
    # Clean vector triangle pointer
    tri_x = [mid_x - 0.06, mid_x + 0.07, mid_x - 0.06]
    tri_y = [mid_y + 0.07, mid_y, mid_y - 0.07]
    tri = patches.Polygon(list(zip(tri_x, tri_y)), facecolor='#FFFFFF', edgecolor='none', zorder=6)
    ax.add_patch(tri)

# -------------------------------------------------------------
# 4. BOTTOM WORKFLOW DATAFLOW SUMMARY BAR
# -------------------------------------------------------------
footer_pill = patches.FancyBboxPatch(
    (0.5, 0.30), 15.0, 0.65,
    boxstyle="round,pad=0.04,rounding_size=0.12",
    facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.2
)
ax.add_patch(footer_pill)

ax.text(0.9, 0.62, "DATA TRANSFORMATION WORKFLOW:", fontsize=9.2, fontweight='bold', color='#0F172A', va='center')

wf_steps = [
    ("Raw JSON Logs", "#2563EB"),
    ("PySpark Ingestion & Cleaning", "#0D9488"),
    ("Dense Vectors [Delta-t, FF, SS]", "#0284C7"),
    ("BiLSTM-Attention (96.4%)", "#7C3AED"),
    ("AWS Tier Placement (S3/IA/Glacier)", "#059669")
]

cur_x = 3.65
for idx, (label, col_text) in enumerate(wf_steps):
    ax.text(cur_x, 0.62, label, fontsize=8.6, color=col_text, fontweight='bold', va='center')
    cur_x += len(label) * 0.098 + 0.28
    if idx < len(wf_steps) - 1:
        arr = patches.Polygon(
            [(cur_x - 0.18, 0.66), (cur_x - 0.08, 0.62), (cur_x - 0.18, 0.58)],
            facecolor='#64748B', edgecolor='none'
        )
        ax.add_patch(arr)

plt.tight_layout()

# Save diagram
out_file = "system_workflow_diagram.png"
fig.savefig(out_file, dpi=300, bbox_inches='tight')

# Also sync to system_architecture_diagram.png & system_architecture_diagram_simple.png
fig.savefig("system_architecture_diagram.png", dpi=300, bbox_inches='tight')
fig.savefig("system_architecture_diagram_simple.png", dpi=300, bbox_inches='tight')

# Copy directly to Review 2 folder for Slide 5
review2_folder = r"C:\Users\harsh\Desktop\Big data\Review 2"
import os, shutil
if os.path.exists(review2_folder):
    shutil.copy(out_file, os.path.join(review2_folder, out_file))
    shutil.copy(out_file, os.path.join(review2_folder, "system_architecture_diagram.png"))
    shutil.copy(out_file, os.path.join(review2_folder, "system_architecture_diagram_simple.png"))

plt.close(fig)
print("SUCCESS: Clear system workflow diagram created and synced!")
