import numpy as np
import matplotlib.pyplot as plt

# Define constants
hbar = 1.054571817e-34  # Reduced Planck's constant (J·s)
c = 3.0e8  # Speed of light (m/s)
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
k_B = 1.380649e-23  # Boltzmann constant (J/K)

# Black hole mass range (solar masses to kg conversion)
solar_mass = 1.989e30  # kg
M_values = np.logspace(1, 8, 100) * solar_mass  # Black hole masses from 10 to 10^8 solar masses

# Standard Hawking radiation equations
T_H_standard = (hbar * c**3) / (8 * np.pi * G * M_values * k_B)
L_H_standard = (hbar * c**6) / (15360 * np.pi * G**2 * M_values**2)

# Dynamic entropy formulation: Entropy as a function of the system's energy state
S_dynamic = k_B * (L_H_standard / (hbar * c))  # Relating entropy to Hawking radiation output

# Plot the results
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_xlabel("Black Hole Mass (Solar Masses)")
ax1.set_ylabel("Entropy (J/K)", color='b')
ax1.plot(M_values / solar_mass, S_dynamic, 'b-', label="Dynamic Entropy (Derived)")
ax1.tick_params(axis='y', labelcolor='b')
ax1.legend(loc='upper right')
ax1.grid(True, which="both", linestyle="--", linewidth=0.5)
ax1.set_title("Dynamic Entropy Derived from Hawking Radiation")

plt.show()
