# Inverse Entropy Horizon Mapping – Predicting Black Hole Mass from Structural τ

import numpy as np
from sympy import symbols, Eq, solve, pi, simplify

# Constants (SI units)
G = 6.67430e-11       # gravitational constant (m^3 kg^-1 s^-2)
c = 299792458         # speed of light (m/s)
hbar = 1.054571817e-34  # reduced Planck constant (J·s)
kB = 1.380649e-23     # Boltzmann constant (J/K)

# Symbolic variables
M, tau = symbols('M tau', positive=True, real=True)
k_val = 0.001005  # Best-fit entropy decay constant
S_inf = 1.0       # Normalized saturation entropy

# Step 1: Invert the entropy saturation function to solve for tau
# S(tau) = S_inf * (1 - exp(-k * tau)) → tau = -ln(1 - S/S_inf) / k
# Assume S = 0.999 for 99.9% saturation
S_target = 0.999

# Compute symbolic tau from S_target
from sympy import log
entropy_tau = -log(1 - S_target) / k_val
entropy_tau = simplify(entropy_tau)

# Step 2: Map tau back to Bekenstein-Hawking entropy scale
# S_BH = S_inf * tau → in actual units: S_BH = tau (unitless)
# Solve for black hole mass using:
# S_BH = (4 * pi * G * A) / (hbar * c * kB)
# where A = 16 * pi * (G * M / c^2)^2

A_expr = 16 * pi * (G * M / c**2)**2
S_BH_expr = (4 * pi * G * A_expr) / (hbar * c * kB)

# Set S_BH = tau to find M
mass_eq = Eq(S_BH_expr, entropy_tau)
M_sol = solve(mass_eq, M)[0].evalf()

print("Target Entropy Level (S = 0.999):")
print("τ required:", entropy_tau)
print("Predicted Black Hole Mass (kg):", M_sol)
