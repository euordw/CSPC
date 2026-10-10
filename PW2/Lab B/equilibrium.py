import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 50.0

def k_imbalance(x):
    return ((2 * x)**2) / ((1 - x)**2) - K

def k_imbalance_sq(x):
    x_val = x[0] if isinstance(x, (list, np.ndarray)) else x
    return (k_imbalance(x_val))**2

# Newton root-finding starting at 0.6 to avoid derivative zero error
x_newton = newton(k_imbalance, x0=0.6)

# SLSQP minimization
res_slsqp = minimize(k_imbalance_sq, x0=[0.5], method="SLSQP", bounds=[(0.001, 0.999)])
x_slsqp = res_slsqp.x[0]

print(f"Equilibrium extent x (Newton): {x_newton:.4f}")
print(f"Equilibrium extent x (SLSQP):  {x_slsqp:.4f}")

x_eq = float(x_newton)
nH2_eq = 1 - x_eq
nI2_eq = 1 - x_eq
nHI_eq = 2 * x_eq

print(f"At equilibrium: H2 = {nH2_eq:.3f} mol, I2 = {nI2_eq:.3f} mol, HI = {nHI_eq:.3f} mol")

# Plotting progress
x_vals = np.linspace(0, 0.95, 200)
nH2 = 1 - x_vals
nI2 = 1 - x_vals
nHI = 2 * x_vals

plt.figure(figsize=(7, 5))
plt.plot(x_vals, nH2, label=r'$n_{H_2}$')
plt.plot(x_vals, nI2, '--', label=r'$n_{I_2}$')
plt.plot(x_vals, nHI, label=r'$n_{HI}$')
plt.axvline(x=x_eq, color='gray', linestyle=':', label=f'Equilibrium (x ≈ {x_eq:.2f})')
plt.xlabel('Extent of reaction (x)')
plt.ylabel('Amount (mol)')
plt.title(r'Chemical Equilibrium of $H_2 + I_2 \rightleftharpoons 2HI$')
plt.legend()
plt.grid(True)
plt.savefig("equilibrium.png")
plt.close()
print("SUCCESS: equilibrium.png created!")