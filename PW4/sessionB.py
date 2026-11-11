import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

os.makedirs("results", exist_ok=True)

# B1: Load Wine Dataset
wine = load_wine(as_frame=True)
X = wine.data
cultivar = wine.target

# B2: Raw PCA
pca_raw = PCA()
pca_raw.fit(X)

# B3: Scaled PCA
scaler = StandardScaler()
Z = scaler.fit_transform(X)

pca_scaled = PCA()
Z_pca = pca_scaled.fit_transform(Z)

# Scree Plot
plt.figure(figsize=(8, 5))
plt.bar(range(1, 14), pca_scaled.explained_variance_ratio_, alpha=0.7, align='center', label='Individual Variance')
plt.step(range(1, 14), np.cumsum(pca_scaled.explained_variance_ratio_), where='mid', label='Cumulative Variance', color='red')
plt.axhline(0.90, color='gray', linestyle='--', label='90% Threshold')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Scree Plot (Scaled Wine Data)')
plt.legend()
plt.savefig("results/scree_plot.png")
plt.close()

# B4: K-Means Clustering (Scaled Data)
km_scaled = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0)
km_scaled.fit(Z)

# B6: Agreement Calculation
def compute_agreement(true_labels, cluster_labels):
    ct = pd.crosstab(true_labels, cluster_labels)
    return ct.max(axis=0).sum() / len(true_labels)

# 1. Scaled K-Means
ag_scaled = compute_agreement(cultivar, km_scaled.labels_)

# 2. Raw K-Means
km_raw = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0)
km_raw.fit(X)
ag_raw = compute_agreement(cultivar, km_raw.labels_)

# 3. PCA (2 components) K-Means
km_pca2 = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0)
km_pca2.fit(Z_pca[:, :2])
ag_pca2 = compute_agreement(cultivar, km_pca2.labels_)

df_agreement = pd.DataFrame([
    {"Representation": "Scaled (13 features)", "Agreement": round(ag_scaled, 4)},
    {"Representation": "Raw Unscaled (13 features)", "Agreement": round(ag_raw, 4)},
    {"Representation": "Scaled PCA (2 components)", "Agreement": round(ag_pca2, 4)}
])

df_agreement.to_csv("results/B_agreement.csv", index=False)
print("SUCCESS: results/B_agreement.csv created!")