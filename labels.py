# In this dataset:
# Samples 1-72 = normal kidney tissue
# Samples 73-144 = kidney cancer tissue

import pandas as pd

df = pd.read_csv("data_clean.txt", sep="\t", index_col=0)

samples = df.columns.tolist()

labels = {}
for i, sample in enumerate(samples):
    if i < 72:
        labels[sample] = "Normal"
    else:
        labels[sample] = "Cancer"

label_df = pd.DataFrame.from_dict(labels, orient="index", columns=["Condition"])
label_df.to_csv("labels.csv")

print("Sample labels created!")
print(label_df["Condition"].value_counts())