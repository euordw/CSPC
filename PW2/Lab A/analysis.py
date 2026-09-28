import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# Part 2: From position to velocity and acceleration
t, y = np.loadtxt('freefall.csv', delimiter=',', skiprows=1, unpack=True)

v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {a.mean():.2f} m/s^2")

# Part 3: The noise problem
print(f"Standard deviation of acceleration: {a.std():.2f}")

# Part 4: Integrating back
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_recovered))
print(f"Max difference between original and recovered position: {max_diff:.2f} meters")

# Part 5: Plot and report
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# Position panel
ax1.plot(t, y, color='blue')
ax1.set_ylabel("Position (m)")
ax1.set_title("Motion Analysis: Freefall")

# Velocity panel
ax2.plot(t, v, color='orange')
ax2.set_ylabel("Velocity (m/s)")

# Acceleration panel
ax3.plot(t, a, color='red')
ax3.set_ylabel("Acceleration (m/s^2)")
ax3.set_xlabel("Time (s)")
ax3.axhline(y=-9.81, color='black', linestyle='--')  # Dashed line for gravity

plt.tight_layout()
plt.savefig('motion.png')