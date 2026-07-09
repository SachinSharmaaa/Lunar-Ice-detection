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

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns)


import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/raw/CH2O_09337_DFRS_DS95_2021_272_00_57/calibrated/ch2o_frs_calibrated_01_21272001904.csv"

df = pd.read_csv(file_path, header=None)

signal = df.iloc[:, -1]

plt.figure(figsize=(10,5))
plt.plot(signal)
plt.title("DFSAR Signal")
plt.xlabel("Sample")
plt.ylabel("Signal Strength")
plt.show()
print("\nSignal Statistics:")
print(df["Signal"].describe())


