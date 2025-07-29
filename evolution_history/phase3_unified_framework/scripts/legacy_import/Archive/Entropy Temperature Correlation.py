import numpy as np
import matplotlib.pyplot as plt

# Define mass range for black holes (logarithmic scale for better resolution)
mass_values = np.logspace(6, 10, 100)  # From 10^6 to 10^10 solar masses

# Standard Hawking temperature formula
T_H_standard = 5.33266392337024 / (np.pi * mass_values)

# Entropy-modified model: introducing an entropy correction term
entropy_correction = np.log(mass_values) / (np.pi * mass_values)  # Hypothetical correction term
T_H_modified = T_H_standard + entropy_correction  # Adding entropy effects

# Identify critical divergence point
divergence_index = np.argmax(np.abs(T_H_modified - T_H_standard) > 1e-9)  # Where deviation becomes significant
critical_mass = mass_values[divergence_index]

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(mass_values, T_H_standard, label="Standard Model", color='blue')
plt.plot(mass_values, T_H_modified, linestyle='dashed', label="Entropy-Modified Model", color='cyan')
plt.axvline(critical_mass, linestyle='dotted', color='black', label="Divergence Point")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Black Hole Mass (Solar Masses)")
plt.ylabel("Hawking Temperature (K)")
plt.title("Refined Correlation: Hawking Temperature and Entropy Divergence")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()

# Print out key data points
print(f"Critical Mass where divergence begins: {critical_mass:.2e} Solar Masses")
