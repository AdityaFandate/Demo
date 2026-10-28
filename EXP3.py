import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("employee_salary_dataset.csv")

# Display first few rows
print("===== ORIGINAL DATASET =====")
print(df.head())

# ---------------------------------
# 1. Simple Random Sampling (20%)
# ---------------------------------
srs_sample = df.sample(frac=0.2, random_state=42)

print("\n===== SIMPLE RANDOM SAMPLE =====")
print(srs_sample)

# ---------------------------------
# 2. Stratified Sampling (20%)
# ---------------------------------
train, stratified_sample = train_test_split(
    df,
    test_size=0.2,
    stratify=df["Department"],
    random_state=42
)

print("\n===== STRATIFIED SAMPLE =====")
print(stratified_sample)

# ---------------------------------
# 3. Cluster Sampling
# ---------------------------------
# Select one random city as a cluster
clusters = df["City"].dropna().unique()

rng = np.random.default_rng(42)
selected_cluster = rng.choice(clusters)

cluster_sample = df[df["City"] == selected_cluster]

print("\n===== CLUSTER SAMPLING =====")
print("Selected Cluster (City):", selected_cluster)
print(cluster_sample)

# ---------------------------------
# 4. Display Sample Sizes
# ---------------------------------
print("\n===== SAMPLE SIZES =====")
print("Original Dataset:", len(df))
print("Simple Random Sample:", len(srs_sample))
print("Stratified Sample:", len(stratified_sample))
print("Cluster Sample:", len(cluster_sample))
