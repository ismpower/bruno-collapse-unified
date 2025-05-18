import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = np.pi

# Define black hole mass range (in solar masses)
M_solar = np.logspace(0, 6, 100)  # 1 to 10^6 solar masses
M_kg = M_solar * 1.98847e30  # Convert to kg

# Standard Hawking Temperature (T_H = hbar * c^3 / (8 * pi * G * M))
T_H_standard = (hbar * c**3) / (8 * pi * G * M_kg)

# Modified entropy correction factor
f_S_correction = 1.16549612154152e-23  # From entropy correlation

# Entropy-Modified Hawking Temperature
T_H_entropy = T_H_standard + f_S_correction

# Observational constraints (Example: CMB and PBH evaporation limits)
M_constraints = np.array([1e-2, 1e1, 1e3, 1e5, 1e8])  # Example masses in solar masses
T_constraints = np.array([1e-2, 1e-4, 1e-6, 1e-8, 1e-10])  # Example observational limits

# Plot results
plt.figure(figsize=(10, 6))
plt.loglog(M_solar, T_H_standard, 'b-', label='Standard Model')
plt.loglog(M_solar, T_H_entropy, 'c--', label='Entropy-Modified Model')
plt.scatter(M_constraints, T_constraints, color='red', marker='x', label='Observational Constraints')
plt.xlabel('Black Hole Mass (Solar Masses)')
plt.ylabel('Hawking Temperature (K)')
plt.title('Hawking Temperature Comparison with Observational Constraints')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
