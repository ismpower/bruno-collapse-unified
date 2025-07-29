import numpy as np
import matplotlib.pyplot as plt

# Define black hole mass range (solar masses)
mass_values = np.logspace(1, 8, 100)  # From 10 to 10^8 solar masses

# Standard model calculations
S_BH_standard = 2.11848383117005e+47 * np.pi * (1.48317777777778e-27 * mass_values)**2
T_H_standard = 5.33266392337024 / (np.pi * mass_values)
L_H_standard = 1.12357230604549e+33 / (np.pi * mass_values**2)

# Entropy-modified model calculations
f_S = 8.89906666666667e-11 * np.pi * (3 * mass_values + mass_values)  # Placeholder entropy function
S_BH_modified = f_S + S_BH_standard
T_H_modified = f_S + T_H_standard
L_H_modified = f_S + L_H_standard

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Hawking Temperature Comparison
axes[0].loglog(mass_values, T_H_standard, label="Standard Model", color='b')
axes[0].loglog(mass_values, T_H_modified, linestyle='dashed', label="Entropy-Modified Model", color='cyan')
axes[0].set_xlabel("Black Hole Mass (Solar Masses)")
axes[0].set_ylabel("Hawking Temperature (K)")
axes[0].set_title("Hawking Temperature Comparison")
axes[0].legend()

# Hawking Radiation Luminosity Comparison
axes[1].loglog(mass_values, L_H_standard, label="Standard Model", color='r')
axes[1].loglog(mass_values, L_H_modified, linestyle='dashed', label="Entropy-Modified Model", color='salmon')
axes[1].set_xlabel("Black Hole Mass (Solar Masses)")
axes[1].set_ylabel("Hawking Radiation Luminosity (W)")
axes[1].set_title("Hawking Radiation Luminosity Comparison")
axes[1].legend()

plt.tight_layout()
plt.show()
