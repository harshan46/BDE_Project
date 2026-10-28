import matplotlib.pyplot as plt
import matplotlib.patches as patches

# High-quality typography settings
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 16:9 clean widescreen layout
fig, ax = plt.subplots(figsize=(14.5, 6.5), dpi=300)
ax.set_xlim(0, 14.5)
ax.set_ylim(0, 6.5)
ax.axis('off')

# Clean white background
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

# -------------------------------------------------------------
# 1. CLEAN TITLE (NO NAMES)
# -------------------------------------------------------------
ax.text(7.25, 5.95, "SYSTEM ARCHITECTURE PIPELINE",
        ha='center', va='center', fontsize=18, fontweight='bold', color='#0F172A')
ax.text(7.25, 5.58, "Automated Lifecycle Classification and Cloud Redundancy Mitigation",
        ha='center', va='center', fontsize=11.5, color='#64748B')

# -------------------------------------------------------------
# 2. FOUR CLEAN PIPELINE BLOCKS (NO NAMES, HIGH READABILITY)
# -------------------------------------------------------------
stages = [
    {
        "step": "STAGE 1",
        "title": "Data Ingestion &\nPreprocessing",
        "color_top": "#2563EB",  # Blue
        "color_bg": "#F8FAFC",
        "color_border": "#93C5FD",
        "lines": [
            "Raw CLUE-LDS JSON Logs",
            "PySpark Distributed Ingestion",
            "Schema Collision Handling",
            "Timestamp Normalization"
        ],
        "badge": "Cleaned File Logs",
        "badge_color": "#1D4ED8"
    },
    {
        "step": "STAGE 2",
        "title": "Feature Engineering &\nGround Truth",
        "color_top": "#0D9488",  # Teal
        "color_bg": "#F8FAFC",
        "color_border": "#99F6E4",
        "lines": [
            "File-Level Entity Aggregation",
            "Temporal Features (Delta-t, FF, SS)",
            "PySpark VectorAssembler",
            "IEEE Heuristic Tiering Rules"
        ],
        "badge": "Feature Vectors [3-D]",
        "badge_color": "#0F766E"
    },
    {
        "step": "STAGE 3",
        "title": "Novel Deep Learning\nClassification",
        "color_top": "#7C3AED",  # Purple
        "color_bg": "#F8FAFC",
        "color_border": "#C4B5FD",
        "lines": [
            "80/20 Distributed Data Split",
            "5 Classical ML Baselines (LR, DT, RF, GBT)",
            "Proposed Novel BiLSTM-Attention",
            "Accuracy: 96.40% | F1: 0.9638"
        ],
        "badge": "Lifecycle Prediction",
        "badge_color": "#6D28D9"
    },
    {
        "step": "STAGE 4",
        "title": "Storage Tiering &\nCost Optimization",
        "color_top": "#059669",  # Green
        "color_bg": "#F8FAFC",
        "color_border": "#A7F3D0",
        "lines": [
            "Hot Tier -> AWS S3 Standard",
            "Cool Tier -> S3 Infrequent Access",
            "Obsolete (ROT) -> S3 Glacier",
            ">90% Cloud Storage Reclaimed"
        ],
        "badge": "Optimized Storage",
        "badge_color": "#047857"
    }
]

box_w = 3.0
box_h = 3.8
start_x = 0.55
gap = 0.55
box_y = 1.25

for i, s in enumerate(stages):
    bx = start_x + i * (box_w + gap)
    
    # Clean main card container
    card = patches.FancyBboxPatch(
        (bx, box_y), box_w, box_h,
        boxstyle="round,pad=0.06,rounding_size=0.14",
        facecolor=s["color_bg"], edgecolor=s["color_border"],
        linewidth=1.8
    )
    ax.add_patch(card)
    
    # Top Stage Header Pill
    pill = patches.FancyBboxPatch(
        (bx + 0.5, box_y + box_h - 0.38), box_w - 1.0, 0.38,
        boxstyle="round,pad=0.03,rounding_size=0.08",
        facecolor=s["color_top"], edgecolor='none'
    )
    ax.add_patch(pill)
    ax.text(bx + (box_w / 2), box_y + box_h - 0.19, s["step"],
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')
    
    # Stage Title
    ax.text(bx + (box_w / 2), box_y + box_h - 0.82, s["title"],
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0F172A', linespacing=1.2)
    
    # Subtle separator
    ax.plot([bx + 0.35, bx + box_w - 0.35], [box_y + box_h - 1.22, box_y + box_h - 1.22],
            color='#E2E8F0', linewidth=1.2)
    
    # Simple Bullet Points
    ly = box_y + box_h - 1.55
    for line in s["lines"]:
        # Bullet marker
        ax.plot(bx + 0.32, ly, marker='o', markersize=4, color=s["color_top"])
        
        # Highlight novel DL model in stage 3
        if "Proposed Novel" in line:
            ax.text(bx + 0.46, ly, line, ha='left', va='center',
                    fontsize=8.5, color='#6D28D9', fontweight='bold')
        elif "96.40%" in line or ">90%" in line:
            ax.text(bx + 0.46, ly, line, ha='left', va='center',
                    fontsize=8.5, color='#047857', fontweight='bold')
        else:
            ax.text(bx + 0.46, ly, line, ha='left', va='center',
                    fontsize=8.5, color='#334155')
        ly -= 0.44

    # Bottom Output Badge
    badge_box = patches.FancyBboxPatch(
        (bx + 0.3, box_y + 0.22), box_w - 0.6, 0.40,
        boxstyle="round,pad=0.03,rounding_size=0.08",
        facecolor=s["badge_color"], edgecolor='none'
    )
    ax.add_patch(badge_box)
    ax.text(bx + (box_w / 2), box_y + 0.42, s["badge"],
            ha='center', va='center', fontsize=8.8, fontweight='bold', color='#FFFFFF')

# -------------------------------------------------------------
# 3. SLEEK CONNECTOR ARROWS BETWEEN STAGES
# -------------------------------------------------------------
for i in range(3):
    cx = start_x + (i + 1) * box_w + i * gap + (gap / 2)
    cy = box_y + (box_h / 2)
    
    # Draw simple clean circle with triangle arrow
    c = patches.Circle((cx, cy), 0.20, facecolor='#0F172A', edgecolor='#FFFFFF', linewidth=1.5, zorder=5)
    ax.add_patch(c)
    
    tri = patches.Polygon(
        [(cx - 0.06, cy + 0.08), (cx + 0.08, cy), (cx - 0.06, cy - 0.08)],
        facecolor='#FFFFFF', edgecolor='none', zorder=6
    )
    ax.add_patch(tri)

# -------------------------------------------------------------
# 4. BOTTOM PIPELINE SUMMARY BAR
# -------------------------------------------------------------
footer_pill = patches.FancyBboxPatch(
    (0.55, 0.25), 13.4, 0.55,
    boxstyle="round,pad=0.04,rounding_size=0.10",
    facecolor='#F1F5F9', edgecolor='#CBD5E1', linewidth=1.0
)
ax.add_patch(footer_pill)

ax.text(7.25, 0.52, "Raw Event Stream  ->  Distributed Cleaning  ->  Feature Extraction  ->  BiLSTM-Attention (96.4%)  ->  Cost-Optimized Cloud Tiers",
        ha='center', va='center', fontsize=9.2, fontweight='bold', color='#334155')

plt.tight_layout()

# Save image
out_png = "system_architecture_diagram_simple.png"
fig.savefig(out_png, dpi=300, bbox_inches='tight')
fig.savefig("system_architecture_diagram.png", dpi=300, bbox_inches='tight')

# Sync to Review 2 folder for PPT
review2_path = r"C:\Users\harsh\Desktop\Big data\Review 2"
import os, shutil
if os.path.exists(review2_path):
    shutil.copy(out_png, os.path.join(review2_path, "system_architecture_diagram_simple.png"))
    shutil.copy(out_png, os.path.join(review2_path, "system_architecture_diagram.png"))

plt.close(fig)
print("SUCCESS: Ultra-simple architecture diagram generated without names!")
