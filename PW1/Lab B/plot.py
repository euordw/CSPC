"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: read decay_observed.csv (columns: time, count; skip the header row)
#         and split it into two arrays: t and observed.
# TODO 1 kodunu bununla əvəz et:
t, observed = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1, unpack=True)
# TODO 2: set N0 to the FIRST observed value, then build the analytical curve
#         analytical = N0 * exp(-LAMBDA * t)
# TODO 2 kodunu bununla əvəz et:
LAMBDA = 0.3
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)
# TODO 3: make a 1x2 subplot with SHARED x and y axes.
#         left panel : scatter of the observed data, titled "Observed data"
#         right panel: line plot of the analytical curve, titled "Analytical"
#         label the axes.
# TODO 3 kodunu bununla əvəz et:
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

# Sol qrafik (Müşahidə edilən - nöqtəli)
ax1.scatter(t, observed, color='blue')
ax1.set_title("Müşahidə edilən")
ax1.set_xlabel("Zaman (t)")
ax1.set_ylabel("Atom sayı (N)")

# Sağ qrafik (Analitik - xətt)
ax2.plot(t, analytical, color='red')
ax2.set_title("Analitik Qanun")
ax2.set_xlabel("Zaman (t)")
# TODO 4: save the figure as figure.png
plt.savefig('figure.png')