import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("chemicals_cancer.csv")
print(df.columns.tolist())   

# Task 6:
print("All patients:")
print("benzene vs malignancy:", df["benzene"].corr(df["malignancy"]))
print("cadmium vs malignancy:", df["cadmium"].corr(df["malignancy"]))

# Task 7: 
sub = df[(df["pollution_index"] > 40) & (df["pollution_index"] < 60)]
print("\nPollution index 40-60 only (", len(sub), "patients ):")
print("benzene vs malignancy:", sub["benzene"].corr(sub["malignancy"]))
print("cadmium vs malignancy:", sub["cadmium"].corr(sub["malignancy"]))

fig, axes = plt.subplots(2, 2, figsize=(9, 7))
for i, chem in enumerate(["benzene", "cadmium"]):
    axes[0, i].scatter(df[chem], df["malignancy"], s=8)
    axes[0, i].set_title(chem + ": all patients")
    axes[1, i].scatter(sub[chem], sub["malignancy"], s=8, color="orange")
    axes[1, i].set_title(chem + ": pollution 40-60 only")
plt.tight_layout()
plt.savefig("chemicals.png")