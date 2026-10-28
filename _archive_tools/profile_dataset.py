import pandas as pd
from pathlib import Path

DATA_FOLDER = Path(
    r"C:\Users\vdhar\Downloads\big-data-lifecycle-classification-main\big-data-lifecycle-classification-main\data\processed"
)

OUTPUT_FOLDER = Path(
    r"C:\Users\vdhar\OneDrive\Desktop\DigitalWasteProject"
)

parquet_file = next(DATA_FOLDER.glob("*.parquet"))
df = pd.read_parquet(parquet_file)

print("\n========== FILE EVENT ANALYSIS ==========")

file_events = df[df["file_path"].notna()].copy()

event_counts = file_events["type"].value_counts()
profile = []

for event in sorted(file_events["type"].unique()):
    subset = file_events[file_events["type"] == event]

    profile.append({
        "event_type": event,
        "total_events": len(subset),
        "unique_files": subset["file_path"].nunique()
    })

profile_df = pd.DataFrame(profile)

print("\nEvent counts and unique files:")
print(profile_df.to_string(index=False))

# Save the profiling results
output_file = OUTPUT_FOLDER / "lifecycle_dataset_profile.csv"
profile_df.to_csv(output_file, index=False)

print(f"\nDataset profile saved to:\n{output_file}")
print("\n=========================================")