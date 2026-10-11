import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load Dataset 1
df = pd.read_csv("heart.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

continuous_cols = ["age", "chol", "trestbps", "thalach"]

# Task 2: Visualize distributions
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for i, col in enumerate(continuous_cols):
    axes[i].hist(df[col], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    axes[i].set_title(f"Distribution of {col}")
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("distributions.png")
plt.close()

# Task 3: Normality Checks (Shapiro-Wilk test)
print("\n--- Normality Test Results (Shapiro-Wilk) ---")
for col in continuous_cols:
    stat, p_value = stats.shapiro(df[col])
    normality = "Approximately Normal" if p_value > 0.05 else "Not Normal"
    print(f"{col}: W = {stat:.4f}, p-value = {p_value:.4e} -> {normality}")

# Task 4: Compare thalach between disease vs healthy
disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]

t_stat, p_val_t = stats.ttest_ind(disease, healthy)
u_stat, p_val_u = stats.mannwhitneyu(disease, healthy)

print(f"\n--- Thalach Comparison ---")
print(f"Disease Mean: {disease.mean():.2f} ± {disease.sem():.2f}")
print(f"Healthy Mean: {healthy.mean():.2f} ± {healthy.sem():.2f}")
print(f"t-test p-value: {p_val_t:.4e}")
print(f"Mann-Whitney U p-value: {p_val_u:.4e}")

# Plot means with error bars (Standard Error of the Mean - SEM)
plt.figure(figsize=(6, 5))
means = [healthy.mean(), disease.mean()]
errors = [healthy.sem(), disease.sem()]
plt.bar(["Healthy (0)", "Disease (1)"], means, yerr=errors, capsize=5, color=['green', 'red'], alpha=0.7)
plt.ylabel("Mean Max Heart Rate (thalach)")
plt.title("Max Heart Rate by Heart Disease Status (with SEM)")
plt.savefig("thalach_comparison.png")
plt.close()

# Task 5: Relationship between age and thalach
corr_pearson, p_p = stats.pearsonr(df["age"], df["thalach"])
corr_spearman, p_s = stats.spearmanr(df["age"], df["thalach"])

print(f"\n--- Age vs Thalach Correlation ---")
print(f"Pearson r: {corr_pearson:.4f} (p = {p_p:.4e})")
print(f"Spearman r: {corr_spearman:.4f} (p = {p_s:.4e})")

plt.figure(figsize=(7, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6, color='purple')
plt.xlabel("Age")
plt.ylabel("Max Heart Rate (thalach)")
plt.title("Age vs Max Heart Rate")
plt.savefig("age_vs_thalach.png")
plt.close()