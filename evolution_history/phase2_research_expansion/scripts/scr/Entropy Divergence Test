import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = np.pi

# Define mass range for black holes (solar masses to kg)
M_solar = 1.989e30  # Solar mass in kg
M_values = np.logspace(35, 42, 100)  # Extremely large masses

# Compute Schwarzschild radius
r_s_values = (2 * G * M_values) / c**2

# Compute standard Bekenstein-Hawking entropy
S_BH_standard = (k_B * 4 * pi * r_s_values**2) / (hbar * G / c**3)

# Compute entropy-modified version (testing alternative model)
f_S = 1e-20  # Hypothetical correction factor for testing
S_BH_modified = S_BH_standard + f_S

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(M_values / M_solar, S_BH_standard, label="Standard Model", color='blue')
plt.plot(M_values / M_solar, S_BH_modified, linestyle='dashed', label="Entropy-Modified Model", color='cyan')
plt.axvline(x=1e6, color='k', linestyle='dotted', label="Divergence Point")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Black Hole Mass (Solar Masses)")
plt.ylabel("Entropy (J/K)")
plt.title("Testing Second Equation: Entropy at Extreme Masses")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
