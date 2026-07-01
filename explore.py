import pandas as pd

print("Loading data...")

# Read the file, skipping comment lines that start with "!"
rows = []
with open("data.txt", "r") as f:
    for line in f:
        if not line.startswith("!"):
            rows.append(line.strip())

# Save cleaned version
with open("data_clean.txt", "w") as f:
    f.write("\n".join(rows))

# Load into pandas
df = pd.read_csv("data_clean.txt", sep="\t", index_col=0)

print(f"Dataset shape: {df.shape[0]} genes x {df.shape[1]} samples")
print("\nFirst 5 gene IDs:")
print(df.index[:5].tolist())
print("\nFirst 5 sample names:")
print(df.columns[:5].tolist())