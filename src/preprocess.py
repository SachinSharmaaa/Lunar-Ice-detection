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

signal_min = df["Signal"].min()
signal_max = df["Signal"].max()

df["Normalized_Signal"] = (
    (df["Signal"] - signal_min)
    / (signal_max - signal_min)
)

print(df[["Signal", "Normalized_Signal"]].head())

df.to_csv(
    "data/processed/normalized_signal.csv",
    index=False
)

print("Saved normalized data")