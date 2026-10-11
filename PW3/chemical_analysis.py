import pandas as pd
import scipy.stats as stats

# Load Dataset 2
df = pd.read_csv("chemicals_cancer.csv")

print("--- Naive Analysis (Task 6) ---")
r_benz, _ = stats.pearsonr(df["benzene"], df["malignancy"])
r_cad, _ = stats.pearsonr(df["cadmium"], df["malignancy"])
print(f"Benzene vs Malignancy correlation: {r_benz:.4f}")
print(f"Cadmium vs Malignancy correlation: {r_cad:.4f}")

print("\n--- Confounding Variable Analysis (Task 7) ---")
# Filter by pollution index range
restricted_df = df[(df["pollution_index"] > 40) & (df["pollution_index"] < 60)]

r_benz_sub, _ = stats.pearsonr(restricted_df["benzene"], restricted_df["malignancy"])
r_cad_sub, _ = stats.pearsonr(restricted_df["cadmium"], restricted_df["malignancy"])

print("In restricted pollution group (40 < pollution_index < 60):")
print(f"Benzene vs Malignancy correlation: {r_benz_sub:.4f}")
print(f"Cadmium vs Malignancy correlation: {r_cad_sub:.4f}")

# Bonus Task: Categorical column uncertainty / balance
target_proportions = df["target"].value_counts(normalize=True) if "target" in df.columns else None