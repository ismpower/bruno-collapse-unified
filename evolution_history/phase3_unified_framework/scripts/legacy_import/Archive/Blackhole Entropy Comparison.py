import numpy as np
import matplotlib.pyplot as plt

# Define black hole mass range (in solar masses)
M_solar = np.logspace(0, 8, 100)  # From 1 to 10^8 solar masses

# Standard Model Equations
T_H_standard = 5.33266392337024 / (np.pi * M_solar)
L_H_standard = 1.12357230604549e+33 / (np.pi * M_solar**2)

# Entropy-Modified Model Predictions
f_S_mod = 1.0e-23  # Assumed entropy modification constant (based on previous results)
T_H_modified = f_S_mod + 5.33266392337024 / (np.pi * M_solar)
L_H_modified = f_S_mod + 1.12357230604549e+33 / (np.pi * M_solar**2)

# Observational Constraints (fictional but reasonable for comparison)
M_obs = np.array([0.1, 1, 10, 10**3, 10**5, 10**7])  # Solar masses
T_obs = np.array([1e-3, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12])  # Kelvin
L_obs = np.array([1e-22, 1e-24, 1e-28, 1e-32, 1e-36, 1e-40])  # Watts

# Create the figure
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot Temperature Comparison
axs[0].loglog(M_solar, T_H_standard, label='Standard Model', color='blue')
axs[0].loglog(M_solar, T_H_modified, '--', label='Entropy-Modified Model', color='cyan')
axs[0].scatter(M_obs, T_obs, color='red', marker='x', label='Observational Constraints')
axs[0].set_xlabel("Black Hole Mass (Solar Masses)")
axs[0].set_ylabel("Hawking Temperature (K)")
axs[0].set_title("Hawking Temperature Comparison with Observations")
axs[0].legend()
axs[0].grid(True, which='both')

# Plot Luminosity Comparison
axs[1].loglog(M_solar, L_H_standard, label='Standard Model', color='red')
axs[1].loglog(M_solar, L_H_modified, '--', label='Entropy-Modified Model', color='salmon')
axs[1].scatter(M_obs, L_obs, color='black', marker='x', label='Observational Constraints')
axs[1].set_xlabel("Black Hole Mass (Solar Masses)")
axs[1].set_ylabel("Hawking Radiation Luminosity (W)")
axs[1].set_title("Hawking Radiation Luminosity Comparison with Observations")
axs[1].legend()
axs[1].grid(True, which='both')

plt.tight_layout()
plt.show()
