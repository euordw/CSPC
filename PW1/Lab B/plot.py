import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read dataset
df = pd.read_csv("decay_observed.csv")

# Get columns dynamically to avoid KeyError
t = df.iloc[:, 0].values  # First column (time)
N_obs = df.iloc[:, 1].values  # Second column (observed count)

# Theoretical law: N(t) = N0 * exp(-lambda * t)
N0 = N_obs[0]
lam = 0.4
N_analytical = N0 * np.exp(-lam * t)

# Plot side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

# 1. Observed Data
ax1.plot(t, N_obs, 'bo', label='Observed')
ax1.set_title('Observed Data')
ax1.set_xlabel('Time (t)')
ax1.set_ylabel('Number of Atoms (N)')

# 2. Analytical Law
ax2.plot(t, N_analytical, 'r-', label='Analytical')
ax2.set_title('Analytical Law')
ax2.set_xlabel('Time (t)')

plt.tight_layout()
plt.savefig("figure.png")
plt.close()
print("SUCCESS: figure.png updated with English labels!")