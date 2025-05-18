import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = np.pi

# Define mass range focusing on transition region
M_values = np.logspace(4.5, 6, 100)  # Focusing between 10^4.5 and 10^6 solar masses
M_critical = 10**5  # Critical mass threshold

# Compute Schwarzschild radius
r_s_values = (2 * G * M_values) / c**2

# Compute Bekenstein-Hawking entropy with modification
S_BH_standard_values = (k_B * 4 * pi * r_s_values**2) / (hbar * G / c**3)
S_BH_modified_values = np.piecewise(M_values, [M_values < M_critical, M_values >= M_critical],
                                    [lambda M: (k_B * 4 * pi * (2 * G * M / c**2)**2) / (hbar * G / c**3),
                                     lambda M: (k_B * 4 * pi * (2 * G * M / c**2)**2) / (hbar * G / c**3) + 1e-10])

# Compute Hawking temperature
T_H_standard_values = (hbar * c**3) / (8 * pi * G * M_values)
T_H_modified_values = np.piecewise(M_values, [M_values < M_critical, M_values >= M_critical],
                                   [lambda M: (hbar * c**3) / (8 * pi * G * M),
                                    lambda M: ((hbar * c**3) / (8 * pi * G * M)) + 1e-10])

# Compute Hawking radiation luminosity
L_H_standard_values = (hbar * c**6) / (15360 * pi * G**2 * M_values**2)
L_H_modified_values = np.piecewise(M_values, [M_values < M_critical, M_values >= M_critical],
                                   [lambda M: (hbar * c**6) / (15360 * pi * G**2 * M**2),
                                    lambda M: ((hbar * c**6) / (15360 * pi * G**2 * M**2)) + 1e-10])

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Hawking Temperature
axes[0].loglog(M_values, T_H_standard_values, label="Standard Model", color='blue')
axes[0].loglog(M_values, T_H_modified_values, '--', label="Entropy-Modified Model", color='cyan')
axes[0].axvline(M_critical, linestyle=':', color='black', label="Critical Mass")
axes[0].set_xlabel("Black Hole Mass (Solar Masses)")
axes[0].set_ylabel("Hawking Temperature (K)")
axes[0].set_title("Hawking Temperature Transition Region")
axes[0].legend()
axes[0].grid(True, which="both", linestyle="--", linewidth=0.5)

# Hawking Radiation Luminosity
axes[1].loglog(M_values, L_H_standard_values, label="Standard Model", color='red')
axes[1].loglog(M_values, L_H_modified_values, '--', label="Entropy-Modified Model", color='salmon')
axes[1].axvline(M_critical, linestyle=':', color='black', label="Critical Mass")
axes[1].set_xlabel("Black Hole Mass (Solar Masses)")
axes[1].set_ylabel("Hawking Radiation Luminosity (W)")
axes[1].set_title("Hawking Radiation Transition Region")
axes[1].legend()
axes[1].grid(True, which="both", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
