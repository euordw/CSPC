import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
)
from sklearn.inspection import permutation_importance

os.makedirs("results", exist_ok=True)

# A1 & A2: Load and Clean Data
df = pd.read_csv("data/concrete.csv")
df = df.drop_duplicates().reset_index(drop=True)

X = df.drop(columns=["strength"])
y = df["strength"]

# A3: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# A4: Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_train = lr.predict(X_train)
y_pred_test = lr.predict(X_test)

def calc_adj_r2(r2, n, p):
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)

n_train, p_feat = X_train.shape[0], X_train.shape[1]
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
test_mae = mean_absolute_error(y_test, y_pred_test)
train_r2 = r2_score(y_train, y_pred_train)
train_adj_r2 = calc_adj_r2(train_r2, n_train, p_feat)
test_r2 = r2_score(y_test, y_pred_test)

# Plot Residuals vs Age (log scale)
residuals = y_test - y_pred_test
plt.figure(figsize=(7, 5))
plt.scatter(X_test["age"], residuals, alpha=0.7, color='crimson')
plt.axhline(0, color='black', linestyle='--')
plt.xscale("log")
plt.xlabel("Age (days, log scale)")
plt.ylabel("Residuals (True - Predicted Strength in MPa)")
plt.title("Residuals vs Age")
plt.savefig("results/residuals_vs_age.png")
plt.close()

# A5: Polynomial Regression Sweep
poly_results = []
for d in [1, 2, 3, 4]:
    poly_model = make_pipeline(
        PolynomialFeatures(degree=d, include_bias=False),
        StandardScaler(),
        LinearRegression()
    )
    poly_model.fit(X_train, y_train)
    
    p_num = poly_model[0].n_output_features_
    yp_tr = poly_model.predict(X_train)
    yp_te = poly_model.predict(X_test)
    
    tr_rmse = np.sqrt(mean_squared_error(y_train, yp_tr))
    te_rmse = np.sqrt(mean_squared_error(y_test, yp_te))
    tr_r2 = r2_score(y_train, yp_tr)
    tr_adj_r2 = calc_adj_r2(tr_r2, n_train, p_num)
    te_r2 = r2_score(y_test, yp_te)
    
    poly_results.append({
        "Degree": d, "Features (p)": p_num,
        "Train RMSE": round(tr_rmse, 3), "Test RMSE": round(te_rmse, 3),
        "Train R2": round(tr_r2, 3), "Train Adj R2": round(tr_adj_r2, 3),
        "Test R2": round(te_r2, 3)
    })

df_poly = pd.DataFrame(poly_results)

# A6: Classification Setup (Target >= 40 MPa)
y_class = (df["strength"] >= 40).astype(int)
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    X, y_class, test_size=0.2, random_state=42, stratify=y_class
)

# KNN Sweep
knn_accs = []
for k in [1, 3, 5, 7, 15, 25, 51, 101]:
    knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))
    knn.fit(Xc_train, yc_train)
    knn_accs.append((k, knn.score(Xc_train, yc_train), knn.score(Xc_test, yc_test)))

# Decision Tree Sweep
tree_accs = []
for depth in [1, 2, 3, 4, 5, 6, 8, None]:
    tree = DecisionTreeClassifier(criterion="entropy", max_depth=depth, min_samples_leaf=1, random_state=0)
    tree.fit(Xc_train, yc_train)
    tree_accs.append((str(depth), tree.get_n_leaves(), tree.score(Xc_train, yc_train), tree.score(Xc_test, yc_test)))

# Selected Best Models
chosen_knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=7))
chosen_knn.fit(Xc_train, yc_train)

chosen_tree = DecisionTreeClassifier(criterion="entropy", max_depth=4, min_samples_leaf=1, random_state=0)
chosen_tree.fit(Xc_train, yc_train)

# A7: Metrics Table
def get_metrics_row(name, model, X_t, y_t, threshold=0.5):
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X_t)[:, 1]
        preds = (probs >= threshold).astype(int)
    else:
        preds = model.predict(X_t)
    
    tn, fp, fn, tp = confusion_matrix(y_t, preds).ravel()
    return {
        "Model": name, "Threshold": threshold,
        "TP": tp, "FP": fp, "FN": fn, "TN": tn,
        "Accuracy": round(accuracy_score(y_t, preds), 3),
        "Precision": round(precision_score(y_t, preds), 3),
        "Recall": round(recall_score(y_t, preds), 3),
        "F1": round(f1_score(y_t, preds), 3)
    }

metrics_list = [
    get_metrics_row("KNN (k=7)", chosen_knn, Xc_test, yc_test, 0.5),
    get_metrics_row("Decision Tree (depth=4)", chosen_tree, Xc_test, yc_test, 0.5)
]

# Threshold Sweep for Tree
for th in [0.3, 0.5, 0.7, 0.9]:
    metrics_list.append(get_metrics_row(f"Tree (th={th})", chosen_tree, Xc_test, yc_test, th))

df_metrics = pd.DataFrame(metrics_list)
df_metrics.to_csv("results/A_metrics.csv", index=False)
print("SUCCESS: results/A_metrics.csv created!")