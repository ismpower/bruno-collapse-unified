import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define mass range for black holes (logarithmic scale)
mass_values = np.logspace(0, 6, 100) * 1.989e30  # From 1 to 10^6 Solar Masses

# Standard Model Equations (Without Entropy Correction)
T_H_standard = [(hbar * c**3) / (8 * pi * G * M) for M in mass_values]
L_H_standard = [(hbar * c**6) / (15360 * pi * G**2 * M**2) for M in mass_values]

# Entropy-Modified Model (Using entropy correction f_S)
f_S = 1.66345592659651e-36  # Entropy correction previously computed
T_H_entropy = [(hbar * c**3) / (8 * pi * G * M) + f_S for M in mass_values]
L_H_entropy = [(hbar * c**6) / (15360 * pi * G**2 * M**2) + f_S for M in mass_values]

# Create the figure
plt.figure(figsize=(10, 5))

# Plot Hawking Temperature comparison
plt.subplot(1, 2, 1)
plt.plot(mass_values / 1.989e30, T_H_standard, label='Standard Model', color='blue')
plt.plot(mass_values / 1.989e30, T_H_entropy, label='Entropy-Modified Model', color='lightblue', linestyle='dashed')
plt.xlabel("Black Hole Mass (Solar Masses)")
plt.ylabel("Hawking Temperature (K)")
plt.title("Hawking Temperature Comparison")
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True)

# Plot Hawking Radiation Luminosity comparison
plt.subplot(1, 2, 2)
plt.plot(mass_values / 1.989e30, L_H_standard, label='Standard Model', color='red')
plt.plot(mass_values / 1.989e30, L_H_entropy, label='Entropy-Modified Model', color='lightcoral', linestyle='dashed')
plt.xlabel("Black Hole Mass (Solar Masses)")
plt.ylabel("Hawking Radiation Luminosity (W)")
plt.title("Hawking Radiation Luminosity Comparison")
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
