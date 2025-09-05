import pandas as pd
import numpy as np
from jellyfish import soundex, jaro_winkler_similarity, nysiis
from itertools import combinations
import time

# --- Step 1: Load Data ---
# Replace 'dirty_data.csv' with your dataset
df = pd.read_csv("dirty_data.csv")
print("Original dataset shape:", df.shape)

# --- Step 2: Data Preparation ---
# Drop duplicates, handle missing values
df = df.drop_duplicates().dropna()
print("After cleaning:", df.shape)

# --- Step 3: Attribute Analysis (Example: name, address, etc.) ---
attributes = ["Name", "Address"]
print("Attributes considered:", attributes)

# --- Step 4: Blocking (group similar entities by first letter of Name) ---
start_time = time.time()
df['Block'] = df['Name'].str[0].str.upper()
blocks = dict(tuple(df.groupby('Block')))
print("Number of blocks formed:", len(blocks))

# --- Step 5: Pairwise Matching ---
def compute_similarity(name1, name2):
    return {
        "Soundex": 1 if soundex(name1) == soundex(name2) else 0,
        "NYSIIS": 1 if nysiis(name1) == nysiis(name2) else 0,
        "Jaro-Winkler": jaro_winkler_similarity(name1, name2)
    }

results = []
for block, group in blocks.items():
    pairs = combinations(group["Name"], 2)
    for p1, p2 in pairs:
        sim = compute_similarity(str(p1), str(p2))
        results.append([p1, p2, sim["Soundex"], sim["NYSIIS"], sim["Jaro-Winkler"]])

results_df = pd.DataFrame(results, columns=["Entity1","Entity2","Soundex","NYSIIS","Jaro-Winkler"])
print(results_df.head())

# --- Step 6: Save Results ---
results_df.to_csv("entity_resolution_results.csv", index=False)
print("Entity Resolution completed in", round(time.time() - start_time, 2), "seconds")
