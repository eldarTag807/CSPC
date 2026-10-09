import pandas as pd
import numpy as np

df = pd.read_csv("heart.csv")

for col in ["target", "sex"]:
    p = df[col].value_counts(normalize=True)
    print(col)
    print(p)
    entropy = -np.sum(p * np.log2(p))
    print("entropy:", entropy, "bits (max is 1 for two categories)")
    print()