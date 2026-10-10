import csv
import numpy as np
import matplotlib.pyplot as plt

# Read titration.csv
volumes = []
phs = []
with open("titration.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        volumes.append(float(row["volume_base"]))
        phs.append(float(row["pH"]))

V = np.array(volumes)
pH = np.array(phs)

# Numerical derivative (slope) calculation
dpH_dV = np.gradient(pH, V)
max_idx = np.argmax(dpH_dV)
v_eq = V[max_idx]

print(f"Equivalence point volume: {v_eq:.2f} mL")

# Plotting side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# pH Curve
ax1.plot(V, pH, 'b.-', label='pH')
ax1.axvline(v_eq, color='r', linestyle='--', label=f'V_eq = {v_eq:.1f} mL')
ax1.set_xlabel('Volume of Base Added (mL)')
ax1.set_ylabel('pH')
ax1.set_title('Titration Curve')
ax1.legend()
ax1.grid(True)

# Slope Curve
ax2.plot(V, dpH_dV, 'g.-', label='dpH/dV')
ax2.axvline(v_eq, color='r', linestyle='--', label=f'Peak at {v_eq:.1f} mL')
ax2.set_xlabel('Volume of Base Added (mL)')
ax2.set_ylabel('dpH / dV')
ax2.set_title('First Derivative (Slope)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("titration.png")
plt.close()
print("SUCCESS: titration.png created!")