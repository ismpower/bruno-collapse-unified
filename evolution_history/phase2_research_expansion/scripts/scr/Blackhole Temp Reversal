import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = np.pi

# Define mass range (from stellar-mass to supermassive black holes)
mass_values = np.logspace(1, 9, 100)  # 10 to 10^9 solar masses

# Standard Hawking temperature equation
T_H_standard = (hbar * c**3) / (8 * pi * G * mass_values)

# Entropy-modified temperature equation (potential reversal behavior)
M_critical = 1e5  # Define a threshold where entropy-induced effects may emerge
f_S = 1e-10  # Placeholder entropy effect coefficient
T_H_modified = np.piecewise(mass_values, 
                            [mass_values < M_critical, mass_values >= M_critical],
                            [lambda M: (hbar * c**3) / (8 * pi * G * M), 
                             lambda M: f_S + (hbar * c**3) / (8 * pi * G * M)])

# Plot the results
plt.figure(figsize=(10, 5))
plt.loglog(mass_values, T_H_standard, label="Standard Model", color='blue')
plt.loglog(mass_values, T_H_modified, label="Entropy-Modified Model", linestyle='dashed', color='cyan')
plt.axvline(M_critical, linestyle='dotted', color='black', label='Critical Mass')
plt.xlabel("Black Hole Mass (Solar Masses)")
plt.ylabel("Hawking Temperature (K)")
plt.title("Potential Temperature Reversal in High-Mass Black Holes")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
