Create the environment for a given lab: `conda env create -f PW/Lab/environment.yml` and `conda activate cspc`

## PW1 Lab A: Reproducible Foundations

**What I built:** I set up a reproducible environment using Conda, version control with Git, wrote tests, and linked it to GitHub.

**Speed comparison (loop vs NumPy):**
* **loop:** 1.6814 s
* **numpy:** 0.0002 s
* **speed-up:** 7283.4 x faster

**Tests:** All passing? Yes

**Conclusion:** I learned how to configure Git, create a Conda environment, run automated tests with PyTest, and compare the execution time of pure Python loops vs NumPy arrays. Everything worked successfully.

---

## PW1 Lab B: Data, Plotting, and Automation

**Conclusion:** The plot showed that the observed radioactive decay data perfectly matches the theoretical analytical law (the smooth curve).

**Automation:** Snakemake is a tool that automates the pipeline steps, ensuring that output files are only rebuilt when their input files are changed.

---

## PW2 Lab A: Motion from Tracking Data

**Results & Observations:**
* **Mean Acceleration:** The measured mean acceleration is approximately -9.81 m/s^2, which confirms the object is in free fall.

---

## PW2 Lab B: Optimization in Chemistry

### Part 2: Optimization Methods Comparison
* **Convex Function ($f(x) = (x-3)^2 + 1$):** All three methods (Gradient Descent, Newton's method on $f'(x)=0$, and SLSQP) rapidly converged to the global minimum at $x \approx 3.0$.
* **Non-Convex Landscape ($g(x) = x^4 - 3x^2 + x + 5$):** 
  * Starting from $x_0 = 0$, Newton's method converged to a local maximum ($x \approx 0.17$, $g''(x) < 0$), whereas Gradient Descent and SLSQP moved toward the local minimum near $x \approx -1.3$.
  * Starting from $x_0 = 2$, all algorithms converged to the global minimum near $x \approx 1.16$.
  * **Conclusion:** Algorithm selection and initial guess heavily influence the optimization path on complex landscapes.

### Part 3: Kinetics Fitting
* **Fitted Rate Constant ($k$):** $k \approx 0.2500\text{ s}^{-1}$ obtained via SLSQP minimization.

### Part 4: Chemical Equilibrium
* **Equilibrium Extent ($x$):** $x \approx 0.6667\text{ mol}$.
* **Equilibrium Composition:**
  * $n_{H_2} \approx 0.333\text{ mol}$
  * $n_{I_2} \approx 0.333\text{ mol}$
  * $n_{HI} \approx 1.333\text{ mol}$
* Root-finding via Newton's method and function minimization via SLSQP yielded identical equilibrium extents.

### Part 5: Titration Equivalence Point
* **Equivalence Volume:** $V_{\text{eq}} \approx 50.0\text{ mL}$, identified where the numerical derivative ($\frac{dpH}{dV}$) reaches its maximum value.

## PW3: Data, Distributions, Testing, and Causation

### Dataset 1: Heart Disease Analysis

#### 1. Normality Verdicts
* **age:** Approximately normal (bell-shaped distribution, p-value from Shapiro-Wilk test evaluated).
* **chol:** Right-skewed (contains some extreme high values/outliers). Not strictly normal.
* **trestbps:** Slightly right-skewed. Not strictly normal.
* **thalach:** Approximately normal (left-skewed slightly, but reasonable for parametric tests).

#### 2. Max Heart Rate Difference (Disease vs Healthy)
* **Method:** Two-sample Student's t-test and Mann-Whitney U test.
* **Result:** Patients with heart disease reach a significantly lower maximum heart rate (`thalach`) compared to healthy individuals ($p < 0.001$).
* **Uncertainty:** The mean `thalach` for healthy patients is higher than for heart-disease patients, confirmed visually with standard error bars in `thalach_comparison.png`.

#### 3. Age vs Max Heart Rate
* **Correlation:** Negative correlation ($r \approx -0.42$).
* **Interpretation:** As age increases, maximum achievable heart rate tends to decrease.

---

### Dataset 2: Chemical Exposure Mystery

#### 1. Naive Analysis
* Naively, **benzene** (or pollution-correlated chemical) showed a much stronger initial correlation with tumour malignancy than cadmium.

#### 2. Confounding Variable Analysis
* After controlling for `pollution_index` (restricting analysis to a fixed pollution range), the apparent correlation between benzene and malignancy disappeared/dropped significantly, while **cadmium** retained a consistent direct correlation with malignancy.
* **Conclusion:** **Cadmium** is the true biological cause of tumour malignancy. Benzene only looked guilty naively because both benzene levels and malignancy scores were confounded by regional `pollution_index`.