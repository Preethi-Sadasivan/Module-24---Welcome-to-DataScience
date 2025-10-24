# Weather Data Visualization using NumPy, Pandas, Matplotlib, and Seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1️⃣ Load the dataset
# -------------------------------

# You can replace this path with your actual weather data CSV file
# For demo purposes, we'll create a small sample dataset
data = {
    "Date": pd.date_range(start="2025-01-01", periods=10),
    "Temperature (°C)": [22, 25, 20, 19, 23, 27, 26, 21, 24, 28],
    "Humidity (%)": [60, 55, 65, 70, 62, 58, 63, 68, 60, 57],
    "Wind Speed (km/h)": [12, 10, 8, 15, 9, 14, 11, 13, 10, 16],
    "Rainfall (mm)": [0, 5, 0, 10, 0, 2, 0, 8, 0, 15]
}

df = pd.DataFrame(data)

# -------------------------------
# 2️⃣ Basic info and statistics
# -------------------------------
print("Basic Information:")
print(df.info(), "\n")

print("Summary Statistics:")
print(df.describe(), "\n")

# Calculate mean temperature using NumPy
mean_temp = np.mean(df["Temperature (°C)"])
print(f"Average Temperature: {mean_temp:.2f} °C\n")

# -------------------------------
# 3️⃣ Data Visualization
# -------------------------------

# Set Seaborn style
sns.set(style="whitegrid", palette="coolwarm")

# 📈 Line plot – Temperature over time
plt.figure(figsize=(8,4))
sns.lineplot(x="Date", y="Temperature (°C)", data=df, marker="o")
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# 📊 Bar plot – Average humidity per day
plt.figure(figsize=(8,4))
sns.barplot(x="Date", y="Humidity (%)", data=df)
plt.title("Daily Humidity Levels")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ☔ Scatter plot – Temperature vs. Rainfall
plt.figure(figsize=(6,4))
sns.scatterplot(x="Temperature (°C)", y="Rainfall (mm)", data=df, color="purple", s=100)
plt.title("Temperature vs Rainfall")
plt.tight_layout()
plt.show()

# 🔥 Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Weather Parameters")
plt.tight_layout()
plt.show()
