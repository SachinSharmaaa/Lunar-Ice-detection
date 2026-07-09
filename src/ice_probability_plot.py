import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/ice_probability.csv"
)

plt.figure(figsize=(12,5))

plt.plot(
    df["Ice_Probability"]
)

plt.title("Ice Probability Score")
plt.xlabel("Sample")
plt.ylabel("Probability")

plt.grid(True)

plt.show()