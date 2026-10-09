import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Task 1: 
df = pd.read_csv("heart.csv")
print(df.shape)
print(df.head())

cols = ["age", "chol", "trestbps", "thalach"]
data = df[cols]
print(data.describe())

# Task 2: 
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
for ax, c in zip(axes.ravel(), cols):
    ax.hist(data[c], bins=20, edgecolor="black")
    ax.set_title(c)
    ax.set_xlabel(c)
    ax.set_ylabel("count")
plt.tight_layout()
plt.savefig("distributions.png")
plt.close()

# Task 3:
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
for ax, c in zip(axes.ravel(), cols):
    stats.probplot(data[c], dist="norm", plot=ax)
    ax.set_title(f"Q-Q plot: {c}")
plt.tight_layout()
plt.savefig("qqplots.png")
plt.close()

for c in cols:
    stat, p = stats.shapiro(data[c])
    print(f"{c}: Shapiro p = {p:.4f}, skew = {stats.skew(data[c]):.3f}")