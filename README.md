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
