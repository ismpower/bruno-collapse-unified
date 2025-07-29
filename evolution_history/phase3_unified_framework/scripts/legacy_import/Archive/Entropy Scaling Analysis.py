import numpy as np
import sympy as sp

# Define the range of black hole masses to analyze
mass_values = np.logspace(1, 8, 10)  # Select representative points from 10 to 10^8 solar masses

# Define the entropy-modified and standard models
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = np.pi

# Schwarzschild radius
r_s_values = (2 * G * mass_values * 1.989e30) / c**2  # Convert solar masses to kg

# Standard Bekenstein-Hawking entropy
S_BH_standard_values = (k_B * 4 * pi * r_s_values**2) / (hbar * G / c**3)

# Entropy-modified Bekenstein-Hawking entropy (introducing correction post-equilibrium)
f_S_mod = 1.16549612154152e-23  # Previously determined scaling entropy correction
S_BH_modified_values = f_S_mod + S_BH_standard_values  # Adjusted values

# Compute percentage difference at different points
percentage_difference = ((S_BH_modified_values - S_BH_standard_values) / S_BH_standard_values) * 100

# Output results at key mass points
print("Black Hole Mass (Solar Masses) | Standard Entropy | Modified Entropy | % Difference")
for i in range(len(mass_values)):
    print(f"{mass_values[i]:.2e} | {S_BH_standard_values[i]:.3e} | {S_BH_modified_values[i]:.3e} | {percentage_difference[i]:.5f}%")
