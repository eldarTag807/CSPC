import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")

# Task 4: 
sick = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]


u, p = stats.mannwhitneyu(sick, healthy, alternative="two-sided")
print(f"Mann-Whitney U = {u:.1f}, p = {p:.3g}")

for name, g in [("disease", sick), ("healthy", healthy)]:
    sem = g.std(ddof=1) / np.sqrt(len(g))
    print(f"{name}: n = {len(g)}, mean = {g.mean():.2f}, SEM = {sem:.2f}")

means = [sick.mean(), healthy.mean()]
sems = [sick.std(ddof=1) / np.sqrt(len(sick)),
        healthy.std(ddof=1) / np.sqrt(len(healthy))]
plt.figure(figsize=(5, 4))
plt.errorbar(["disease", "healthy"], means, yerr=sems, fmt="o", capsize=6)
plt.ylabel("mean thalach (bpm) ± SEM")
plt.xlim(-0.5, 1.5)
plt.tight_layout()
plt.savefig("thalach_means.png")
plt.close()

# Task 5
rho, p_rho = stats.spearmanr(df["age"], df["thalach"])
print(f"Spearman rho = {rho:.3f}, p = {p_rho:.3g}")

plt.figure(figsize=(6, 4.5))
plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.xlabel("age")
plt.ylabel("thalach")
plt.title(f"age vs thalach (Spearman rho = {rho:.2f})")
plt.tight_layout()
plt.savefig("age_vs_thalach.png")
plt.close()