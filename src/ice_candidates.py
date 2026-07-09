import pandas as pd

file_path = "data/raw/CH2O_09337_DFRS_DS95_2021_272_00_57/calibrated/ch2o_frs_calibrated_01_21272001904.csv"

df = pd.read_csv(file_path, header=None)

df.columns = [
    "Day",
    "Time",
    "Frequency",
    "Value_1",
    "Value_2",
    "Signal"
]

# Top 5% strongest signals
threshold = df["Signal"].quantile(0.95)

ice_candidates = df[df["Signal"] >= threshold]

print("Threshold:", threshold)
print("Number of candidates:", len(ice_candidates))

print("\nTop 20 Candidates:")
print(ice_candidates.head(20))

ice_candidates.to_csv(
    "data/processed/ice_candidates.csv",
    index=False
)

print("\nSaved: data/processed/ice_candidates.csv")