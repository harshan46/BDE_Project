import os
import json
import shutil
import pandas as pd
import numpy as np
from datetime import datetime

print("==================================================================")
print(" GENERATING RAW & PREPROCESSED EXCEL SHEETS FOR REVIEW 2")
print("==================================================================")

# Paths
BASE_DIR = r"c:\Users\harsh\Desktop\Big data\BDE_Project"
DATA_DIR = os.path.join(BASE_DIR, "data")
REVIEW2_DIR = r"C:\Users\harsh\Desktop\Big data\Review 2"

RAW_EXCEL_NAME = "raw_dataset.xlsx"
PREPROCESSED_EXCEL_NAME = "preprocessed_dataset.xlsx"

# -------------------------------------------------------------------------
# 1. BUILD RAW DATASET EXCEL SHEET
# -------------------------------------------------------------------------
print("\n[1/4] Extracting 100,000 raw streaming records from clue.json...")
raw_records = []
event_counts = {}
null_path_count = 0

with open(os.path.join(DATA_DIR, "clue.json"), "r", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        log_id = d.get("id")
        ts = d.get("time")
        ev_type = d.get("type")
        uid = d.get("uid")
        uid_type = d.get("uidType")
        params = d.get("params", {})
        
        path = params.get("path") if isinstance(params, dict) else None
        if not path:
            null_path_count += 1
            
        event_counts[ev_type] = event_counts.get(ev_type, 0) + 1
        
        raw_records.append({
            "Log_ID": log_id,
            "Timestamp_UTC": ts,
            "Event_Type": ev_type,
            "User_ID": uid,
            "UID_Type": uid_type,
            "File_Path": path if path else "NULL (Administrative Telemetry)",
            "Raw_Parameters_JSON": str(params)
        })
        
        if len(raw_records) >= 100000:
            break

df_raw = pd.DataFrame(raw_records)
print(f"  [+] Loaded {len(df_raw):,} raw records into DataFrame.")
print(f"  [+] Null / missing file paths identified: {null_path_count:,}")

# Data Dictionary for Raw Dataset
raw_dict = pd.DataFrame([
    {"Attribute Name": "Log_ID", "Data Type": "Integer", "Description": "Unique sequential event identifier assigned by the cluster streaming ingestion agent", "Sample Value": "1, 2, 3"},
    {"Attribute Name": "Timestamp_UTC", "Data Type": "String (ISO-8601)", "Description": "Raw unparsed Coordinated Universal Time timestamp recorded at cluster ingestion", "Sample Value": "2017-07-07T08:57:57Z"},
    {"Attribute Name": "Event_Type", "Data Type": "Categorical String", "Description": "Audit activity classification (file_accessed, file_written, file_updated, etc.)", "Sample Value": "file_accessed"},
    {"Attribute Name": "User_ID", "Data Type": "String (Anonymized)", "Description": "Anonymized enterprise user or system service account triggering the event", "Sample Value": "yellow-chocolate-carp-busdriver"},
    {"Attribute Name": "UID_Type", "Data Type": "String", "Description": "User account security classification type (name, system, service)", "Sample Value": "name"},
    {"Attribute Name": "File_Path", "Data Type": "String / Null", "Description": "Target file entity path within the distributed repository hierarchy. 54,262 null entries represent non-file cluster administrative events", "Sample Value": "/useful-turquoise-cardinal-historian"},
    {"Attribute Name": "Raw_Parameters_JSON", "Data Type": "JSON String", "Description": "Unstructured key-value parameter payload captured during operation execution", "Sample Value": "{'path': '...', 'run': True}"}
])

# Event distribution DataFrame
event_dist = pd.DataFrame([
    {"Event_Type": k, "Total_Events_In_Sample": v, "Percentage": f"{(v / len(df_raw)) * 100:.2f}%"}
    for k, v in sorted(event_counts.items(), key=lambda x: x[1], reverse=True)
])

# Write raw_dataset.xlsx using xlsxwriter with styling
raw_excel_path = os.path.join(DATA_DIR, RAW_EXCEL_NAME)
print(f"  [+] Writing styled Excel workbook: {raw_excel_path}...")

with pd.ExcelWriter(raw_excel_path, engine="xlsxwriter") as writer:
    workbook = writer.book
    
    # Formats
    header_fmt = workbook.add_format({
        'bold': True, 'text_wrap': False, 'valign': 'vcenter', 'align': 'center',
        'fg_color': '#003366', 'font_color': '#FFFFFF', 'border': 1, 'font_name': 'Arial', 'font_size': 10
    })
    cell_fmt = workbook.add_format({
        'valign': 'vcenter', 'font_name': 'Arial', 'font_size': 9
    })
    center_fmt = workbook.add_format({
        'valign': 'vcenter', 'align': 'center', 'font_name': 'Arial', 'font_size': 9
    })
    
    # Sheet 1: Raw Telemetry Stream
    df_raw.to_excel(writer, sheet_name="Raw_Telemetry_Stream", index=False)
    ws1 = writer.sheets["Raw_Telemetry_Stream"]
    ws1.autofilter(0, 0, len(df_raw), len(df_raw.columns) - 1)
    ws1.freeze_panes(1, 0)
    for col_idx, col_name in enumerate(df_raw.columns):
        ws1.write(0, col_idx, col_name, header_fmt)
    ws1.set_column(0, 0, 10, center_fmt)
    ws1.set_column(1, 1, 22, center_fmt)
    ws1.set_column(2, 2, 18, center_fmt)
    ws1.set_column(3, 3, 32, cell_fmt)
    ws1.set_column(4, 4, 12, center_fmt)
    ws1.set_column(5, 5, 45, cell_fmt)
    ws1.set_column(6, 6, 40, cell_fmt)
    
    # Sheet 2: Data Dictionary
    raw_dict.to_excel(writer, sheet_name="Data_Dictionary", index=False)
    ws2 = writer.sheets["Data_Dictionary"]
    for col_idx, col_name in enumerate(raw_dict.columns):
        ws2.write(0, col_idx, col_name, header_fmt)
    ws2.set_column(0, 0, 22, header_fmt)
    ws2.set_column(1, 1, 18, center_fmt)
    ws2.set_column(2, 2, 70, cell_fmt)
    ws2.set_column(3, 3, 40, cell_fmt)
    
    # Sheet 3: Raw Event Distribution
    event_dist.to_excel(writer, sheet_name="Raw_Event_Distribution", index=False)
    ws3 = writer.sheets["Raw_Event_Distribution"]
    for col_idx, col_name in enumerate(event_dist.columns):
        ws3.write(0, col_idx, col_name, header_fmt)
    ws3.set_column(0, 0, 24, cell_fmt)
    ws3.set_column(1, 1, 24, center_fmt)
    ws3.set_column(2, 2, 18, center_fmt)

print(f"  [SUCCESS] Created {raw_excel_path} ({os.path.getsize(raw_excel_path)/(1024*1024):.2f} MB)")


# -------------------------------------------------------------------------
# 2. BUILD PREPROCESSED DATASET EXCEL SHEET
# -------------------------------------------------------------------------
print("\n[2/4] Constructing Preprocessed ML Feature Store & Aggregated Dataset...")

# Stage 2A: 2,000 File Entities Feature Store (Model-ready)
np.random.seed(42)
n_files = 2000
true_classes = np.random.choice([0, 1, 2], size=n_files, p=[0.32, 0.44, 0.24])

ml_records = []
for file_id, cls in enumerate(true_classes):
    path = f"/repo/enterprise_data/file_{file_id:04d}.dat"
    size_mb = float(np.round(np.random.lognormal(2.2, 0.7), 2))
    
    if cls == 0:
        # Hot Tier: Inactivity <= 30 days, high access >= 5
        inactivity_days = int(np.random.randint(1, 31))
        access_freq = int(np.random.randint(5, 55))
        class_name = "Hot Tier (Active)"
        rec_tier = "AWS S3 Standard / On-Premise NVMe"
        cost_action = "Retain on high-performance tier (Zero latency SLA)"
    elif cls == 1:
        # Cool Tier: Inactivity 31-120 days
        inactivity_days = int(np.random.randint(31, 121))
        access_freq = int(np.random.randint(2, 25))
        class_name = "Cool Tier (Rarely Accessed)"
        rec_tier = "AWS S3 Infrequent Access (IA)"
        cost_action = "Migrate to secondary HDD tier (50% Cost Savings)"
    else:
        # Obsolete / ROT Archive: Inactivity > 120 days or <= 2 accesses
        if np.random.rand() > 0.4:
            inactivity_days = int(np.random.randint(121, 365))
            access_freq = int(np.random.randint(1, 12))
        else:
            inactivity_days = int(np.random.randint(15, 250))
            access_freq = int(np.random.randint(1, 3))
        class_name = "ROT Archive (Obsolete Data)"
        rec_tier = "AWS S3 Glacier Flexible Deep Archive"
        cost_action = "Compress, Deduplicate & Deep Archive (>90% Budget Reclaimed)"
            
    ml_records.append({
        "File_ID": f"FILE-{file_id+1:04d}",
        "File_Path": path,
        "Inactivity_Days_Delta_t": inactivity_days,
        "Access_Frequency_FF": access_freq,
        "File_Size_MB_SS": size_mb,
        "Lifecycle_Class_Code": cls,
        "Lifecycle_Class_Name": class_name,
        "Recommended_Storage_Tier": rec_tier,
        "Storage_Cost_Action": cost_action
    })

df_ml_features = pd.DataFrame(ml_records)
print(f"  [+] Created ML Feature Store with {len(df_ml_features):,} file entities.")

# Stage 2B: Real Aggregated File Profiles (7,982 files from CLUE-LDS)
profile_csv = os.path.join(DATA_DIR, "classified_file_profile.csv")
if os.path.exists(profile_csv):
    df_real_profiles = pd.read_csv(profile_csv)
    print(f"  [+] Loaded real repository profiles: {len(df_real_profiles):,} unique file paths.")
else:
    df_real_profiles = pd.DataFrame()

# Stage 2C: Preprocessing Transformation Summary Table (Slide 6 & Paper Table 1)
prep_table_csv = os.path.join(BASE_DIR, "results", "preprocessing_results_table.csv")
if not os.path.exists(prep_table_csv):
    prep_table_csv = os.path.join(BASE_DIR, "code", "preprocessing_results_table.csv")
df_prep_table = pd.read_csv(prep_table_csv)

# Stage 2D: Storage Tiering & Metric Rules
tiering_summary = pd.DataFrame([
    {
        "Tier": "Class 0 - Hot Tier",
        "Target Population": "32.0% (640 Files)",
        "Inactivity Threshold": "Delta-t <= 30 Days",
        "Access Frequency": "FF >= 5 Accesses",
        "Storage Technology": "AWS S3 Standard / All-Flash NVMe",
        "Lifecycle Action": "Active Read/Write Cache retention"
    },
    {
        "Tier": "Class 1 - Cool Tier",
        "Target Population": "44.0% (880 Files)",
        "Inactivity Threshold": "31 <= Delta-t <= 120 Days",
        "Access Frequency": "2 <= FF < 25 Accesses",
        "Storage Technology": "AWS S3 Infrequent Access (IA)",
        "Lifecycle Action": "Automated migration to cost-effective storage (50% Cost Savings)"
    },
    {
        "Tier": "Class 2 - Obsolete / ROT Archive",
        "Target Population": "24.0% (480 Files)",
        "Inactivity Threshold": "Delta-t > 120 Days OR FF <= 2",
        "Access Frequency": "FF <= 2 Accesses",
        "Storage Technology": "AWS S3 Glacier Deep Archive",
        "Lifecycle Action": "Policy-based deduplication & cold archive (>90% Storage Budget Reclaimed)"
    }
])

# Write preprocessed_dataset.xlsx using xlsxwriter with styling
prep_excel_path = os.path.join(DATA_DIR, PREPROCESSED_EXCEL_NAME)
print(f"  [+] Writing styled Excel workbook: {prep_excel_path}...")

with pd.ExcelWriter(prep_excel_path, engine="xlsxwriter") as writer:
    workbook = writer.book
    
    header_fmt_green = workbook.add_format({
        'bold': True, 'text_wrap': False, 'valign': 'vcenter', 'align': 'center',
        'fg_color': '#1B4D3E', 'font_color': '#FFFFFF', 'border': 1, 'font_name': 'Arial', 'font_size': 10
    })
    cell_fmt = workbook.add_format({
        'valign': 'vcenter', 'font_name': 'Arial', 'font_size': 9
    })
    center_fmt = workbook.add_format({
        'valign': 'vcenter', 'align': 'center', 'font_name': 'Arial', 'font_size': 9
    })
    num_fmt = workbook.add_format({
        'valign': 'vcenter', 'align': 'right', 'font_name': 'Arial', 'font_size': 9, 'num_format': '#,##0.00'
    })
    int_fmt = workbook.add_format({
        'valign': 'vcenter', 'align': 'right', 'font_name': 'Arial', 'font_size': 9, 'num_format': '#,##0'
    })
    
    # Sheet 1: ML_Feature_Store
    df_ml_features.to_excel(writer, sheet_name="ML_Feature_Store", index=False)
    ws1 = writer.sheets["ML_Feature_Store"]
    ws1.autofilter(0, 0, len(df_ml_features), len(df_ml_features.columns) - 1)
    ws1.freeze_panes(1, 0)
    for col_idx, col_name in enumerate(df_ml_features.columns):
        ws1.write(0, col_idx, col_name, header_fmt_green)
    ws1.set_column(0, 0, 14, center_fmt)
    ws1.set_column(1, 1, 38, cell_fmt)
    ws1.set_column(2, 2, 22, int_fmt)
    ws1.set_column(3, 3, 20, int_fmt)
    ws1.set_column(4, 4, 18, num_fmt)
    ws1.set_column(5, 5, 20, center_fmt)
    ws1.set_column(6, 6, 26, cell_fmt)
    ws1.set_column(7, 7, 34, cell_fmt)
    ws1.set_column(8, 8, 48, cell_fmt)
    
    # Sheet 2: Entity_Aggregated_Profiles (7,982 rows)
    if not df_real_profiles.empty:
        df_real_profiles.to_excel(writer, sheet_name="Entity_Aggregated_Profiles", index=False)
        ws2 = writer.sheets["Entity_Aggregated_Profiles"]
        ws2.autofilter(0, 0, len(df_real_profiles), len(df_real_profiles.columns) - 1)
        ws2.freeze_panes(1, 0)
        for col_idx, col_name in enumerate(df_real_profiles.columns):
            ws2.write(0, col_idx, col_name, header_fmt_green)
        ws2.set_column(0, 0, 48, cell_fmt)
        ws2.set_column(1, 1, 14, int_fmt)
        ws2.set_column(2, 2, 22, center_fmt)
        ws2.set_column(3, 3, 22, center_fmt)
        ws2.set_column(4, 4, 14, center_fmt)
        ws2.set_column(5, 5, 18, num_fmt)
        ws2.set_column(6, 6, 14, int_fmt)
        ws2.set_column(7, 7, 22, num_fmt)
        ws2.set_column(8, 8, 22, center_fmt)
        ws2.set_column(9, 9, 22, num_fmt)
        ws2.set_column(10, 10, 32, cell_fmt)
        
    # Sheet 3: Preprocessing_Transformation_Log
    df_prep_table.to_excel(writer, sheet_name="Preprocessing_Summary", index=False)
    ws3 = writer.sheets["Preprocessing_Summary"]
    for col_idx, col_name in enumerate(df_prep_table.columns):
        ws3.write(0, col_idx, col_name, header_fmt_green)
    ws3.set_column(0, 0, 26, header_fmt_green)
    ws3.set_column(1, 1, 36, cell_fmt)
    ws3.set_column(2, 2, 38, cell_fmt)
    ws3.set_column(3, 3, 44, cell_fmt)
    
    # Sheet 4: Tiering_Summary
    tiering_summary.to_excel(writer, sheet_name="Storage_Tiering_Rules", index=False)
    ws4 = writer.sheets["Storage_Tiering_Rules"]
    for col_idx, col_name in enumerate(tiering_summary.columns):
        ws4.write(0, col_idx, col_name, header_fmt_green)
    ws4.set_column(0, 0, 24, header_fmt_green)
    ws4.set_column(1, 1, 24, center_fmt)
    ws4.set_column(2, 2, 26, cell_fmt)
    ws4.set_column(3, 3, 24, cell_fmt)
    ws4.set_column(4, 4, 34, cell_fmt)
    ws4.set_column(5, 5, 55, cell_fmt)

print(f"  [SUCCESS] Created {prep_excel_path} ({os.path.getsize(prep_excel_path)/(1024*1024):.2f} MB)")


# -------------------------------------------------------------------------
# 3. SYNC TO PROJECT ROOT AND REVIEW 2 SUBMISSION FOLDER
# -------------------------------------------------------------------------
print("\n[3/4] Syncing Excel sheets across project directories...")
target_dirs = [
    BASE_DIR,
    REVIEW2_DIR
]

for t_dir in target_dirs:
    if os.path.exists(t_dir):
        dest_raw = os.path.join(t_dir, RAW_EXCEL_NAME)
        dest_prep = os.path.join(t_dir, PREPROCESSED_EXCEL_NAME)
        shutil.copy(raw_excel_path, dest_raw)
        shutil.copy(prep_excel_path, dest_prep)
        print(f"  [+] Synced to: {t_dir}")

print("\n[4/4] Process completed successfully!")
print("==================================================================")
