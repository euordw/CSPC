import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Read dataset
df = pd.read_csv("kinetics.csv")
t = df["time"].values
C_measured = df["concentration"].values
C0 = C_measured[0]

# Error function to minimize
def total_error(k):
    k_val = k[0] if isinstance(k, (list, np.ndarray)) else k
    C_model = C0 * np.exp(-k_val * t)
    return np.sum((C_measured - C_model)**2)

# Minimize using SLSQP
res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
fitted_k = res.x[0]

print(f"Fitted rate constant k = {fitted_k:.4f}")

# Plotting curve
t_dense = np.linspace(t.min(), t.max(), 200)
C_fit = C0 * np.exp(-fitted_k * t_dense)

plt.figure(figsize=(7, 5))
plt.plot(t, C_measured, 'ro', label='Measured Data')
plt.plot(t_dense, C_fit, 'b-', label=f'Fitted Curve (k = {fitted_k:.4f})')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('First-Order Reaction Kinetics Fitting')
plt.legend()
plt.grid(True)
plt.savefig("kinetics.png")
plt.close()
print("SUCCESS: kinetics.png created!")