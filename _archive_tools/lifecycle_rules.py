import pandas as pd
from pathlib import Path

# Dataset location
DATA_FOLDER = Path(
    r"C:\Users\vdhar\Downloads\big-data-lifecycle-classification-main\big-data-lifecycle-classification-main\data\processed"
)

# Load dataset
parquet_file = next(DATA_FOLDER.glob("*.parquet"))
df = pd.read_parquet(parquet_file)

print("\n========== FILE LIFECYCLE CLASSIFICATION ==========")

# Keep records with file paths
file_events = df[df["file_path"].notna()].copy()

# Display available columns
print("\nAvailable dataset columns:")
print(df.columns.tolist())

# Display available event types
print("\nAvailable event types:")
print(file_events["type"].value_counts().to_string())

print("\n===================================================")
print("\n========== TIMESTAMP ANALYSIS ==========")

for column in ["time", "event_time"]:
    print(f"\nColumn: {column}")
    print("Data type:", df[column].dtype)
    print("Missing values:", df[column].isna().sum())
    print("Sample values:")
    print(df[column].dropna().head(5).to_string(index=False))

print("\n========================================")

print("\n========== FILE ACTIVITY PROFILE ==========")

# Convert event_time to datetime
df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")

# Keep records with valid file paths and timestamps
file_events = df[
    df["file_path"].notna() &
    df["event_time"].notna()
].copy()

# Summarize the activity history of each file
file_profile = (
    file_events.groupby("file_path")
    .agg(
        total_events=("type", "count"),
        first_seen=("event_time", "min"),
        last_seen=("event_time", "max"),
        event_types=("type", "nunique")
    )
    .reset_index()
)

# Calculate the observed activity span
file_profile["activity_span_days"] = (
    file_profile["last_seen"] - file_profile["first_seen"]
).dt.total_seconds() / 86400

print("\nTotal unique file paths:", len(file_profile))

print("\nFiles with the most recorded events:")
print(
    file_profile.sort_values("total_events", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\nFiles with the longest observed activity spans:")
print(
    file_profile.sort_values("activity_span_days", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\n============================================")
# Save the file activity profile
OUTPUT_FILE = Path(
    r"C:\Users\vdhar\OneDrive\Desktop\DigitalWasteProject\file_activity_profile.csv"
)

file_profile.to_csv(OUTPUT_FILE, index=False)

print(f"\nFile activity profile saved to:\n{OUTPUT_FILE}")
# ============================================
# LIFECYCLE CLASSIFICATION
# ============================================

print("\n========== LIFECYCLE CLASSIFICATION ==========")

# Count recorded file-access events for each file
access_counts = (
    file_events[file_events["type"] == "file_accessed"]
    .groupby("file_path")
    .size()
    .rename("access_count")
)

# Add access counts to the file activity profile
file_profile = file_profile.merge(
    access_counts,
    on="file_path",
    how="left"
)

file_profile["access_count"] = (
    file_profile["access_count"].fillna(0).astype(int)
)

# Use the latest event in the dataset as the reference time
reference_time = file_events["event_time"].max()

# Calculate days since the last recorded event
file_profile["days_since_last_event"] = (
    reference_time - file_profile["last_seen"]
).dt.total_seconds() / 86400

# Count access events only through the reference time
last_access = (
    file_events[file_events["type"] == "file_accessed"]
    .groupby("file_path")["event_time"]
    .max()
    .rename("last_access")
)

file_profile = file_profile.merge(
    last_access,
    on="file_path",
    how="left"
)

file_profile["days_since_last_access"] = (
    reference_time - file_profile["last_access"]
).dt.total_seconds() / 86400
import time
classification_start = time.perf_counter()
# Apply the documented provisional rules
def classify_file(row):
    inactivity = row["days_since_last_access"]
    accesses = row["access_count"]

    if pd.isna(inactivity) or pd.isna(accesses):
        return "Needs Review"

    if inactivity <= 30 and accesses >= 5:
        return "Class 0 - Active (Hot Tier)"

    if 31 <= inactivity <= 120:
        return "Class 1 - Rarely Accessed (Cool Tier)"

    if inactivity >= 121 and accesses <= 1:
        return "Class 2 - Potentially Obsolete"

    return "Needs Review"

print("\n========== ACCESS COUNT ANALYSIS ==========")

print("\nFiles with zero recorded accesses:")
print((file_profile["access_count"] == 0).sum())

print("\nFiles with 1–4 recorded accesses:")
print(
    file_profile["access_count"].between(1, 4).sum()
)

print("\nFiles with 5 or more recorded accesses:")
print((file_profile["access_count"] >= 5).sum())

print("\n============================================")
file_profile["lifecycle_class"] = file_profile.apply(
    classify_file,
    axis=1
)
classification_time = time.perf_counter() - classification_start

print(f"\nActual classification time: {classification_time:.6f} seconds")
# Display classification results
print("\nFiles in each lifecycle category:")
print(file_profile["lifecycle_class"].value_counts().to_string())

# Save classification results
CLASSIFIED_OUTPUT = Path(
    r"C:\Users\vdhar\OneDrive\Desktop\DigitalWasteProject\classified_file_profile.csv"
)

file_profile.to_csv(CLASSIFIED_OUTPUT, index=False)

print(f"\nClassified file profile saved to:\n{CLASSIFIED_OUTPUT}")
print("\n==============================================")

# ============================================
# FAIRER BASELINE BENCHMARKING
# ============================================

import time

print("\n========== BASELINE BENCHMARKING ==========")

# Prepare the same file profiles for both methods
benchmark_data = file_profile.copy()

# Method 1: Simple baseline
# Assign every file to Needs Review
start_time = time.perf_counter()

baseline_predictions = [
    "Needs Review" for _ in range(len(benchmark_data))
]

baseline_time = time.perf_counter() - start_time

# Method 2: Rule-based classifier
# Apply the actual lifecycle rules to every file
start_time = time.perf_counter()

rule_predictions = benchmark_data.apply(
    classify_file,
    axis=1
).tolist()

rule_time = time.perf_counter() - start_time

# Display class distributions
print("\nBaseline classification:")
print(pd.Series(baseline_predictions).value_counts().to_string())

print("\nRule-based classification:")
print(pd.Series(rule_predictions).value_counts().to_string())

# Display execution times
print("\nExecution Time Comparison:")
print(f"Baseline prediction time: {baseline_time:.6f} seconds")
print(f"Rule-based classification time: {rule_time:.6f} seconds")

# Save benchmark results
benchmark_results = pd.DataFrame({
    "Method": ["Baseline", "Rule-based"],
    "Execution_Time_Seconds": [baseline_time, rule_time],
    "Total_Files": [
        len(benchmark_data),
        len(benchmark_data)
    ]
})

BENCHMARK_OUTPUT = Path(
    r"C:\Users\vdhar\OneDrive\Desktop\DigitalWasteProject\benchmark_results.csv"
)

benchmark_results.to_csv(BENCHMARK_OUTPUT, index=False)

print(f"\nBenchmark results saved to:\n{BENCHMARK_OUTPUT}")
print("\n===========================================")