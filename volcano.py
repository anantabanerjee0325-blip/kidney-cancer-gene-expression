import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("Loading data...")
df = pd.read_csv("data_clean.txt", sep="\t", index_col=0)
labels = pd.read_csv("labels.csv", index_col=0)

normal = labels[labels["Condition"] == "Normal"].index
cancer = labels[labels["Condition"] == "Cancer"].index

print("Calculating gene differences...")
results = []
for gene in df.index:
    normal_vals = df.loc[gene, normal]
    cancer_vals = df.loc[gene, cancer]
    
    fold_change = cancer_vals.mean() - normal_vals.mean()
    _, pvalue = stats.ttest_ind(cancer_vals, normal_vals)
    results.append({"gene": gene, "fold_change": fold_change, "pvalue": pvalue})

results_df = pd.DataFrame(results)
results_df["-log10_pvalue"] = -np.log10(results_df["pvalue"] + 1e-10)

# Plot
print("Drawing volcano plot...")
plt.figure(figsize=(10, 7))
plt.scatter(results_df["fold_change"], results_df["-log10_pvalue"],
            alpha=0.3, color="grey", s=5)

# Highlight significant genes
sig = results_df[(results_df["pvalue"] < 0.05) & (results_df["fold_change"].abs() > 1)]
up = sig[sig["fold_change"] > 0]
down = sig[sig["fold_change"] < 0]

plt.scatter(up["fold_change"], up["-log10_pvalue"], color="tomato", s=5, alpha=0.6, label="Higher in Cancer")
plt.scatter(down["fold_change"], down["-log10_pvalue"], color="steelblue", s=5, alpha=0.6, label="Higher in Normal")

plt.axvline(x=1, color="black", linestyle="--", linewidth=0.8)
plt.axvline(x=-1, color="black", linestyle="--", linewidth=0.8)
plt.axhline(y=-np.log10(0.05), color="black", linestyle="--", linewidth=0.8)

plt.xlabel("Fold Change (Cancer vs Normal)", fontsize=12)
plt.ylabel("-log10(p-value)", fontsize=12)
plt.title("Volcano Plot: Kidney Cancer vs Normal Tissue", fontsize=14)
plt.legend()
plt.savefig("volcano.png", dpi=150, bbox_inches="tight")
print("Saved as volcano.png ✅")
print(f"\nSignificant genes found: {len(sig)}")
print(f"Higher in cancer: {len(up)}")
print(f"Higher in normal: {len(down)}")