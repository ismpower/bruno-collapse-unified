import numpy as np
import matplotlib.pyplot as plt

# Define temperature range including superconducting transition
T = np.linspace(-2, 7, 500)  # Extending slightly below 0K for model testing
T_c = 1.2  # Superconducting transition temperature (K)

# Standard linear entropy model (for reference)
S_standard = np.maximum(T * 1e-22, 0)  # Linear scaling with temperature

# Modified entropy model including superconducting transition effects
S_modified = np.where(T < T_c, np.exp(-((T - T_c) / 0.2)**2) * T * 1e-22, T * 1e-22)

# Plot results
plt.figure(figsize=(8,5))
plt.plot(T, S_standard, label="Standard Model (S ∝ T)", linestyle='-', color='blue')
plt.plot(T, S_modified, label="Modified Model (Superconductivity Correction)", linestyle='--', color='red')
plt.axvline(x=T_c, color='black', linestyle='dotted', label="Superconductivity Transition (1.2K)")

plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("Entropy Behavior Near Superconductivity Transition")
plt.legend()
plt.grid()
plt.show()
