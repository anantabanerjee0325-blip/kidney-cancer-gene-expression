import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading data...")
df = pd.read_csv("data_clean.txt", sep="\t", index_col=0)
labels = pd.read_csv("labels.csv", index_col=0)

# Pick the top 10 most variable genes
top_genes = df.var(axis=1).nlargest(10).index
df_top = df.loc[top_genes]

# Add color labels
col_colors = labels["Condition"].map({"Normal": "steelblue", "Cancer": "tomato"})

# Draw the heatmap
print("Drawing heatmap...")
sns.clustermap(
    df_top,
    col_colors=col_colors,
    cmap="vlag",
    figsize=(14, 6),
    yticklabels=True,
    xticklabels=False
)

plt.suptitle("Top 10 Most Variable Genes: Cancer vs Normal", y=1.02, fontsize=14)
plt.savefig("heatmap.png", bbox_inches="tight", dpi=150)
print("Saved as heatmap.png ✅")