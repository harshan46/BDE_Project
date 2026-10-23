import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set clean font
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# Create figure with 16:9 widescreen ratio
fig, ax = plt.subplots(figsize=(15.2, 8.4), dpi=300)
ax.set_xlim(0, 15.2)
ax.set_ylim(0, 8.4)
ax.axis('off')

# Clean modern background
fig.patch.set_facecolor('#F8FAFC')
ax.set_facecolor('#F8FAFC')

# -------------------------------------------------------------
# 1. TOP HEADER BANNER
# -------------------------------------------------------------
title_box = patches.FancyBboxPatch(
    (0.6, 7.30), 14.0, 0.85,
    boxstyle="round,pad=0.08,rounding_size=0.15",
    facecolor='#0F172A', edgecolor='none'
)
ax.add_patch(title_box)

ax.text(7.6, 7.82, "OVERALL SYSTEM ARCHITECTURE PIPELINE",
        ha='center', va='center', fontsize=17, fontweight='bold', color='#FFFFFF')
ax.text(7.6, 7.50, "An Integrated Distributed Framework for Lifecycle Classification & Redundancy Mitigation",
        ha='center', va='center', fontsize=11, color='#94A3B8')

# -------------------------------------------------------------
# 2. FOUR STAGES DATA DEFINITION
# -------------------------------------------------------------
stages = [
    {
        "num": "STAGE 1",
        "lead": "Shanmuga Priyan",
        "title": "Data Ingestion &\nPreprocessing",
        "color_header": "#2563EB", # Vibrant Blue
        "color_bg": "#EFF6FF",
        "color_border": "#3B82F6",
        "items": [
            "Raw CLUE-LDS JSON Logs\n(Zenodo Repository: 100K Events)",
            "PySpark Distributed Ingestion\n(Case-Sensitivity Handling Enabled)",
            "Data Cleaning & Imputation\n(Timestamp Parsing to ISO-8601)",
            "Partitioned DataFrame Cache\n(In-Memory Worker Node Distribution)"
        ],
        "output_badge": "Cleaned Event Stream",
        "output_color": "#1D4ED8"
    },
    {
        "num": "STAGE 2",
        "lead": "V Dharani",
        "title": "Feature Engineering &\nGround-Truth Rules",
        "color_header": "#0D9488", # Teal
        "color_bg": "#F0FDFA",
        "color_border": "#14B8A6",
        "items": [
            "Entity Aggregation (groupBy)\n(Aggregates logs by FilePath)",
            "Temporal Feature Vectors:\n- Inactivity Days (Delta-t = T_snap - T_max)\n- Access Frequency (FF = Total Events)\n- Peak File Size (SS in MB)",
            "VectorAssembler (PySpark)\n(Combines features into dense vectors)",
            "IEEE Heuristic Tiering Rules\n(Class 0: Hot | Class 1: Cool | Class 2: ROT)"
        ],
        "output_badge": "Labeled Feature Matrix",
        "output_color": "#0F766E"
    },
    {
        "num": "STAGE 3",
        "lead": "S Harshan",
        "title": "Novel Deep Learning &\nML Classification",
        "color_header": "#7C3AED", # Indigo / Purple
        "color_bg": "#F5F3FF",
        "color_border": "#8B5CF6",
        "items": [
            "80/20 Distributed Data Split\n(Stratified Train/Test Evaluation)",
            "5 Classical ML Baselines:\n- Logistic Reg (81.2%) - SVM (85.9%)\n- Decision Tree (88.4%) - RF (92.8%)\n- Gradient Boosted Trees (94.1%)",
            "PROPOSED NOVEL ARCHITECTURE:\n[NOVEL] Temporal BiLSTM with Multi-Head\n        Attention Mechanism (96.40% Acc)",
            "Multi-Class Model Inference\n(Precision: 0.965 | F1-Score: 0.964)"
        ],
        "output_badge": "Optimal Storage Class (0, 1, 2)",
        "output_color": "#6D28D9"
    },
    {
        "num": "STAGE 4",
        "lead": "Rameshvar S",
        "title": "Redundancy Mitigation &\nStorage Tiering",
        "color_header": "#059669", # Emerald Green
        "color_bg": "#ECFDF5",
        "color_border": "#10B981",
        "items": [
            "Automated Tier Placement:\n- Class 0 -> AWS S3 Standard ($0.023/GB)\n- Class 1 -> AWS S3 IA ($0.0125/GB)\n- Class 2 -> S3 Glacier Deep Archive",
            "Redundancy & ROT Mitigation\n(Identifies stale candidates for cleanup)",
            "Operating Cost Optimization\n(Reclaims >90% Storage Budget)",
            "Analytical Reporting Dashboard\n(Streamlit / Apache Superset UI)"
        ],
        "output_badge": "Cost Savings & Dashboard",
        "output_color": "#047857"
    }
]

# -------------------------------------------------------------
# 3. DRAW 4 CARDS (PIPELINE MODULES)
# -------------------------------------------------------------
card_w = 3.20
card_gap = 0.38
start_x = 0.6
card_y = 1.05
card_h = 5.95

for i, st in enumerate(stages):
    x = start_x + i * (card_w + card_gap)
    
    # Outer Card Box
    card = patches.FancyBboxPatch(
        (x, card_y), card_w, card_h,
        boxstyle="round,pad=0.08,rounding_size=0.16",
        facecolor=st["color_bg"], edgecolor=st["color_border"],
        linewidth=2.2
    )
    ax.add_patch(card)
    
    # Card Header Pill (Badge)
    hdr_box = patches.FancyBboxPatch(
        (x + 0.15, card_y + card_h - 0.74), card_w - 0.3, 0.60,
        boxstyle="round,pad=0.04,rounding_size=0.12",
        facecolor=st["color_header"], edgecolor='none'
    )
    ax.add_patch(hdr_box)
    
    ax.text(x + (card_w / 2), card_y + card_h - 0.36, f"{st['num']}: {st['lead'].upper()}",
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')
    ax.text(x + (card_w / 2), card_y + card_h - 0.58, "Stage Lead Developer",
            ha='center', va='center', fontsize=8.0, color='#E2E8F0')
    
    # Card Title
    ax.text(x + (card_w / 2), card_y + card_h - 1.20, st["title"],
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#0F172A', linespacing=1.2)
    
    # Divider line
    ax.plot([x + 0.3, x + card_w - 0.3], [card_y + card_h - 1.62, card_y + card_h - 1.62],
            color=st["color_border"], linewidth=1.2, linestyle='-')
    
    # Card Content Items
    item_y = card_y + card_h - 1.95
    for item in st["items"]:
        # Bullet box
        bullet = patches.FancyBboxPatch(
            (x + 0.18, item_y - 0.68), card_w - 0.36, 0.76,
            boxstyle="round,pad=0.03,rounding_size=0.09",
            facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.0
        )
        ax.add_patch(bullet)
        
        # Highlight novel DL model in Stage 3
        if "PROPOSED NOVEL" in item:
            bullet.set_facecolor('#FEF3C7')
            bullet.set_edgecolor('#D97706')
            bullet.set_linewidth(1.6)
            ax.text(x + 0.28, item_y - 0.30, item, ha='left', va='center',
                    fontsize=8.2, color='#92400E', fontweight='bold', linespacing=1.25)
        else:
            ax.text(x + 0.28, item_y - 0.30, item, ha='left', va='center',
                    fontsize=8.0, color='#334155', linespacing=1.25)
            
        item_y -= 0.86

    # Bottom Output Badge
    out_box = patches.FancyBboxPatch(
        (x + 0.2, card_y + 0.18), card_w - 0.4, 0.46,
        boxstyle="round,pad=0.04,rounding_size=0.10",
        facecolor=st["output_color"], edgecolor='none'
    )
    ax.add_patch(out_box)
    ax.text(x + (card_w / 2), card_y + 0.41, f"Output: {st['output_badge']}",
            ha='center', va='center', fontsize=8.8, fontweight='bold', color='#FFFFFF')

# -------------------------------------------------------------
# 4. VECTOR DRAWN CONNECTOR ARROWS BETWEEN STAGES
# -------------------------------------------------------------
for i in range(3):
    center_x = start_x + (i + 1) * card_w + i * card_gap + (card_gap / 2)
    center_y = card_y + (card_h / 2) + 0.25
    
    # Draw circular badge
    circle = patches.Circle((center_x, center_y), 0.22,
                            facecolor='#0F172A', edgecolor='#FFFFFF', linewidth=2.0, zorder=5)
    ax.add_patch(circle)
    
    # Draw pure vector right-pointing triangle arrow (no unicode glyph dependency)
    tri_x = [center_x - 0.08, center_x + 0.09, center_x - 0.08]
    tri_y = [center_y + 0.09, center_y, center_y - 0.09]
    tri = patches.Polygon(list(zip(tri_x, tri_y)), facecolor='#FFFFFF', edgecolor='none', zorder=6)
    ax.add_patch(tri)

# -------------------------------------------------------------
# 5. BOTTOM SUMMARY FOOTER
# -------------------------------------------------------------
footer_box = patches.FancyBboxPatch(
    (0.6, 0.18), 14.0, 0.65,
    boxstyle="round,pad=0.08,rounding_size=0.12",
    facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.2
)
ax.add_patch(footer_box)

ax.text(1.2, 0.50, "PIPELINE SUMMARY:", fontsize=9.5, fontweight='bold', color='#0F172A', va='center')

steps = [
    ("100K Raw Events", "#2563EB"),
    ("PySpark Cleaning", "#0D9488"),
    ("Feature Vectors [Delta-t, FF, SS]", "#0F766E"),
    ("Novel BiLSTM-Attention (96.4%)", "#7C3AED"),
    ("Storage Tiering (>90% Cost Reclaimed)", "#059669")
]

x_pos = 3.3
for idx, (label, col_text) in enumerate(steps):
    ax.text(x_pos, 0.50, label, fontsize=8.8, color=col_text, fontweight='bold', va='center')
    x_pos += len(label) * 0.105 + 0.35
    if idx < len(steps) - 1:
        # Draw small arrow
        arr = patches.Polygon(
            [(x_pos - 0.22, 0.54), (x_pos - 0.12, 0.50), (x_pos - 0.22, 0.46)],
            facecolor='#64748B', edgecolor='none'
        )
        ax.add_patch(arr)

plt.tight_layout()

# Save clean version and replace existing version
fig.savefig("system_architecture_diagram_simple.png", dpi=300, bbox_inches='tight')
fig.savefig("system_architecture_diagram.png", dpi=300, bbox_inches='tight')

# Also sync directly to Review 2 folder for Rameshvar/PPT
review2_path = r"C:\Users\harsh\Desktop\Big data\Review 2"
import os, shutil
if os.path.exists(review2_path):
    shutil.copy("system_architecture_diagram_simple.png", os.path.join(review2_path, "system_architecture_diagram_simple.png"))
    shutil.copy("system_architecture_diagram.png", os.path.join(review2_path, "system_architecture_diagram.png"))

plt.close(fig)
print("SUCCESS: Clear and simple system architecture diagram created without any glyph errors!")
