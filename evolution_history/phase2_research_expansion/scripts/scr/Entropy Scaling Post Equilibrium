import numpy as np
import matplotlib.pyplot as plt

# Define constants
H0 = 2.2e-18  # Hubble constant in 1/s
M_eq = 1e5  # Equilibrium threshold in solar masses (example value)

# Define black hole mass range (in solar masses)
M_solar = np.logspace(0, 8, 100)  # From 1 to 10^8 solar masses

# Standard Model Equations
T_H_standard = 5.33266392337024 / (np.pi * M_solar)
L_H_standard = 1.12357230604549e+33 / (np.pi * M_solar**2)

# Entropy-Modified Model with Post-Equilibrium Scaling
f_S_mod_base = 1.16549612154152e-23
alpha = np.ones_like(M_solar)
alpha[M_solar > M_eq] = (M_solar[M_solar > M_eq] / M_eq)  # Scaling only applied past equilibrium

# Apply entropy correction only post-equilibrium
f_S_mod = f_S_mod_base * alpha
T_H_modified = f_S_mod + 5.33266392337024 / (np.pi * M_solar)
L_H_modified = f_S_mod + 1.12357230604549e+33 / (np.pi * M_solar**2)

# Plot results
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot Temperature Comparison
axs[0].loglog(M_solar, T_H_standard, label='Standard Model', color='blue')
axs[0].loglog(M_solar, T_H_modified, '--', label='Entropy-Modified Model (Scaling Applied Post-Equilibrium)', color='cyan')
axs[0].axvline(M_eq, linestyle='dotted', color='black', label='Equilibrium Threshold')
axs[0].set_xlabel("Black Hole Mass (Solar Masses)")
axs[0].set_ylabel("Hawking Temperature (K)")
axs[0].set_title("Hawking Temperature Comparison with Scaling Post-Equilibrium")
axs[0].legend()
axs[0].grid(True, which='both')

# Plot Luminosity Comparison
axs[1].loglog(M_solar, L_H_standard, label='Standard Model', color='red')
axs[1].loglog(M_solar, L_H_modified, '--', label='Entropy-Modified Model (Scaling Applied Post-Equilibrium)', color='salmon')
axs[1].axvline(M_eq, linestyle='dotted', color='black', label='Equilibrium Threshold')
axs[1].set_xlabel("Black Hole Mass (Solar Masses)")
axs[1].set_ylabel("Hawking Radiation Luminosity (W)")
axs[1].set_title("Hawking Radiation Luminosity Comparison with Scaling Post-Equilibrium")
axs[1].legend()
axs[1].grid(True, which='both')

plt.tight_layout()
plt.show()
