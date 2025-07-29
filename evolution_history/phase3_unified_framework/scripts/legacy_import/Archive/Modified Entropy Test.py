import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols for black hole properties
M, r_s, S_BH, T_H, L_H, f_S_mod = sp.symbols('M r_s S_BH T_H L_H f_S_mod')

# Schwarzschild radius equation (remains unchanged)
r_s_eq = sp.Eq(r_s, (2 * G * M) / c**2)

# Bekenstein-Hawking entropy equation with entropy modification
S_BH_eq = sp.Eq(S_BH, f_S_mod + (k_B * 4 * pi * sp.Pow(r_s, 2)) / (hbar * G / c**3))

# Hawking temperature equation with entropy modification
T_H_eq = sp.Eq(T_H, f_S_mod + (hbar * c**3) / (8 * pi * G * M))

# Hawking radiation luminosity equation with entropy modification
L_H_eq = sp.Eq(L_H, f_S_mod + (hbar * c**6) / (15360 * pi * G**2 * M**2))

# Convert equations into numerical functions
mass_values = np.logspace(-1, 8, 100)  # Solar masses range from 0.1 to 10^8
schwarzschild_radii = [(2 * G * m * 1.989e30) / c**2 for m in mass_values]

# Placeholder entropy modification function
f_S_mod_values = np.full_like(mass_values, 1e-23)  # Adjustable based on further refinement

# Compute temperature and luminosity for both models
T_H_standard = [(hbar * c**3) / (8 * pi * G * (m * 1.989e30)) for m in mass_values]
T_H_modified = [fs + (hbar * c**3) / (8 * pi * G * (m * 1.989e30)) for fs, m in zip(f_S_mod_values, mass_values)]

L_H_standard = [(hbar * c**6) / (15360 * pi * G**2 * (m * 1.989e30)**2) for m in mass_values]
L_H_modified = [fs + (hbar * c**6) / (15360 * pi * G**2 * (m * 1.989e30)**2) for fs, m in zip(f_S_mod_values, mass_values)]

# Plot results
plt.figure(figsize=(12, 6))

# Temperature comparison
plt.subplot(1, 2, 1)
plt.loglog(mass_values, T_H_standard, label='Standard Model', color='blue')
plt.loglog(mass_values, T_H_modified, linestyle='dashed', label='Entropy-Modified Model', color='cyan')
plt.xlabel('Black Hole Mass (Solar Masses)')
plt.ylabel('Hawking Temperature (K)')
plt.title('Hawking Temperature Comparison')
plt.legend()

# Luminosity comparison
plt.subplot(1, 2, 2)
plt.loglog(mass_values, L_H_standard, label='Standard Model', color='red')
plt.loglog(mass_values, L_H_modified, linestyle='dashed', label='Entropy-Modified Model', color='salmon')
plt.xlabel('Black Hole Mass (Solar Masses)')
plt.ylabel('Hawking Radiation Luminosity (W)')
plt.title('Hawking Radiation Luminosity Comparison')
plt.legend()

plt.tight_layout()
plt.show()
