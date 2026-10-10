import numpy as np
from scipy.optimize import minimize, newton

# ----------------------------------------------------
# 2A. Easy convex function: f(x) = (x - 3)^2 + 1
# ----------------------------------------------------
def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

def d2f(x):
    return 2

print("=== 2A. Convex Function Optimization ===")

# (1) Gradient Descent
x_gd = 0.0
lr = 0.1
for _ in range(100):
    x_gd = x_gd - lr * df(x_gd)
print(f"1. Gradient Descent result from x0=0: {x_gd:.6f}")

# (2) Newton's method on f'(x) = 0
x_newton = newton(df, x0=0.0, fprime=d2f)
print(f"2. Newton's method result from x0=0:   {x_newton:.6f}")

# (3) SLSQP minimization
res_slsqp = minimize(f, x0=0.0, method="SLSQP")
print(f"3. SLSQP minimize result from x0=0:     {res_slsqp.x[0]:.6f}\n")


# ----------------------------------------------------
# 2B. Harder landscape: g(x) = x^4 - 3x^2 + x + 5
# ----------------------------------------------------
def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def d2g(x):
    return 12*x**2 - 6

def run_landscape_tests(x0):
    print(f"--- Starting from x0 = {x0} ---")
    
    # Gradient Descent
    x_gd = x0
    lr = 0.01
    for _ in range(1000):
        x_gd = x_gd - lr * dg(x_gd)
    print(f"Gradient Descent: x = {x_gd:.6f}, g(x) = {g(x_gd):.6f}")

    # Newton's Method
    x_newt = newton(dg, x0=float(x0), fprime=d2g)
    curvature = d2g(x_newt)
    st_type = "minimum" if curvature > 0 else ("maximum" if curvature < 0 else "inflection")
    print(f"Newton's Method:  x = {x_newt:.6f}, g''(x) = {curvature:.4f} ({st_type})")

    # SLSQP
    res = minimize(g, x0=x0, method="SLSQP")
    print(f"SLSQP:            x = {res.x[0]:.6f}, g(x) = {g(res.x[0]):.6f}\n")

print("=== 2B. Harder Landscape Optimization ===")
run_landscape_tests(x0=0)
run_landscape_tests(x0=2)