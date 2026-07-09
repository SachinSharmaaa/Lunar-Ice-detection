import pandas as pd

df = pd.read_csv(
    "data/processed/normalized_signal.csv"
)

df["Ice_Probability"] = (
    df["Normalized_Signal"] * 100
)

top_ice = df.sort_values(
    "Ice_Probability",
    ascending=False
)

print(
    top_ice[
        ["Time", "Signal", "Ice_Probability"]
    ].head(20)
)

top_ice.to_csv(
    "data/processed/ice_probability.csv",
    index=False
)