# GW150914 Entropy Comparison – Bekenstein vs Saturation Model

import numpy as np
from sympy import symbols, Eq, solve, pi, simplify, log, exp

# Constants (SI units)
G = 6.67430e-11        # m^3 kg^-1 s^-2
c = 299792458          # m/s
hbar = 1.054571817e-34 # J*s
kB = 1.380649e-23      # J/K
M_sun = 1.98847e30     # kg

# Masses from GW150914
M1 = 36 * M_sun
M2 = 29 * M_sun
M_final = 62 * M_sun  # Final black hole (3 M_sun radiated)

# Step 1: Compute Bekenstein-Hawking entropy for initial and final masses
def bh_entropy(M):
    A = 16 * pi * (G * M / c**2)**2
    S = (4 * pi * G * A) / (hbar * c * kB)
    return S.evalf()

S1 = bh_entropy(M1)
S2 = bh_entropy(M2)
S_final = bh_entropy(M_final)
S_initial_total = S1 + S2

# Step 2: Compute Saturation Model τ from normalized entropy
# We normalize entropy by max (final BH) and invert:
k_val = 0.001005
S_norm = S_initial_total / S_final

# Inverse of saturation model: S = 1 - exp(-k * tau)
tau = -log(1 - S_norm) / k_val

# Step 3: Forward check with our model
S_model_check = 1 - exp(-k_val * tau)

print("--- GW150914 Entropy Analysis ---")
print("Initial entropy (S1 + S2):", S_initial_total)
print("Final entropy (S_final):", S_final)
print("Normalized entropy (initial/final):", S_norm)
print("Structural τ from saturation model:", tau.evalf())
print("Model forward-check (should ≈ normalized entropy):", S_model_check.evalf())
