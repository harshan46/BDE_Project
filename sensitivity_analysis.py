import pandas as pd

df = pd.read_csv("classified_file_profile.csv")

obsolete_thresholds = [1, 2, 3, 7, 30, 121]
results = []

for threshold in obsolete_thresholds:

    labels = []

    for _, row in df.iterrows():
        inactivity = row["days_since_last_access"]
        accesses = row["access_count"]

        if pd.isna(inactivity) or pd.isna(accesses):
            label = "Needs Review"

        elif inactivity <= 30 and accesses >= 5:
            label = "Active (Hot Tier)"

        elif 31 <= inactivity <= 120:
            label = "Rarely Accessed (Cool Tier)"

        elif inactivity >= threshold and accesses <= 1:
            label = "Potentially Obsolete"

        else:
            label = "Needs Review"

        labels.append(label)

    counts = pd.Series(labels).value_counts()

    results.append({
        "Obsolete_Threshold_Days": threshold,
        "Active_Hot_Tier": counts.get("Active (Hot Tier)", 0),
        "Rarely_Accessed_Cool_Tier": counts.get(
            "Rarely Accessed (Cool Tier)", 0
        ),
        "Potentially_Obsolete": counts.get(
            "Potentially Obsolete", 0
        ),
        "Needs_Review": counts.get("Needs Review", 0),
        "Total_Files": len(labels)
    })

results_df = pd.DataFrame(results)

print("\nOBSOLETE THRESHOLD SENSITIVITY ANALYSIS")
print(results_df.to_string(index=False))

results_df.to_csv(
    "classification_sensitivity_results.csv",
    index=False
)

print("\nSaved: classification_sensitivity_results.csv")