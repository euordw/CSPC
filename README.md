# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

## PW1 Lab A: Reproducible Foundations

**What I built:**
I set up a reproducible environment using Conda, version control with Git, wrote tests, and linked it to GitHub.

**Speed comparison (loop vs NumPy): **
- loop: 1.6814 s
- numpy: 0.0002 s
- speed-up: 7283.4 x faster

**Tests: ** all passing? yes

**Conclusion: **
I learned how to configure Git, create a Conda environment, run automated tests with Pytest, and compare the execution time of pure Python loops vs NumPy arrays. Everything worked successfully.


## PW1 Lab B: Data, Plotting, and Automation

**Conclusion:** The plot showed that the observed radioactive decay data perfectly matches the theoretical analytical law (the smooth curve).

**Automation:** Snakemake is a tool that automates the pipeline steps, ensuring that output files are only rebuilt when their input files are changed[cite: 2].

## PW2 Lab A: Motion from Tracking Data

**Results & Observations:**
*   **Mean Acceleration:** The measured mean acceleration is approximately -9.81 m/s^2, which confirms the object is in free fall.
*   **The Noise Problem:** The calculated acceleration is very noisy because it was obtained by applying the derivative twice to the position data. Differentiation amplifies the random measurement noise.
*   **Integrating Back:** When integrating the noisy acceleration back up to velocity and position, the random noise partly cancelled out. The integration successfully suppressed the noise, and the recovered position matched the original measurements within about a metre.