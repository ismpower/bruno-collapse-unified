import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define constants
pi = np.pi
M_critical = 1e5  # Arbitrary critical mass threshold for transition

# Define black hole mass range
mass_values = np.logspace(1, 8, 100)

# Standard Model calculations
T_H_standard = 5.33266392337024 / (pi * mass_values)
L_H_standard = 1.12357230604549e+33 / (pi * mass_values**2)

# Entropy-Modified Model (Piecewise function application)
T_H_modified = np.piecewise(mass_values, [mass_values < M_critical, mass_values >= M_critical],
                             [lambda M: 5.33266392337024 / (pi * M), lambda M: 5.33266392337024 / (pi * M) + 1e-5])

L_H_modified = np.piecewise(mass_values, [mass_values < M_critical, mass_values >= M_critical],
                             [lambda M: 1.12357230604549e+33 / (pi * M**2), lambda M: 1.12357230604549e+33 / (pi * M**2) + 1e-5])

# Create plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot Hawking Temperature Comparison
axes[0].plot(mass_values, T_H_standard, label="Standard Model", color='b')
axes[0].plot(mass_values, T_H_modified, linestyle='dashed', label="Entropy-Modified Model", color='cyan')
axes[0].axvline(M_critical, color='black', linestyle='dotted', label="Critical Mass")
axes[0].set_xscale("log")
axes[0].set_yscale("log")
axes[0].set_xlabel("Black Hole Mass (Solar Masses)")
axes[0].set_ylabel("Hawking Temperature (K)")
axes[0].set_title("Hawking Temperature Comparison")
axes[0].legend()

# Plot Hawking Radiation Luminosity Comparison
axes[1].plot(mass_values, L_H_standard, label="Standard Model", color='r')
axes[1].plot(mass_values, L_H_modified, linestyle='dashed', label="Entropy-Modified Model", color='salmon')
axes[1].axvline(M_critical, color='black', linestyle='dotted', label="Critical Mass")
axes[1].set_xscale("log")
axes[1].set_yscale("log")
axes[1].set_xlabel("Black Hole Mass (Solar Masses)")
axes[1].set_ylabel("Hawking Radiation Luminosity (W)")
axes[1].set_title("Hawking Radiation Luminosity Comparison")
axes[1].legend()

plt.tight_layout()
plt.show()
