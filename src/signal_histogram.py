import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure(figsize=(10,5))
plt.hist(df["Signal"], bins=50)

plt.title("Signal Distribution")
plt.xlabel("Signal")
plt.ylabel("Count")

plt.grid(True)
plt.show()