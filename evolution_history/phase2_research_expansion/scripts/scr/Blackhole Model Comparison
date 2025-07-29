import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols for black hole properties
M = sp.symbols('M')  # Mass

# Standard Schwarzschild radius equation (General Relativity model)
r_s_standard = (2 * G * M) / c**2

# Modified Schwarzschild radius equation including entropy effects
f_S = 1.66345592659651e-36  # Previously computed entropy contribution
r_s_entropy = (2 * G * M) / c**2 + f_S  # Adding entropy correction

# Define mass range for plotting (in solar masses)
mass_values = np.linspace(0, 6, 100) * 1.989e30  # Convert to kg

# Compute Schwarzschild radii for both models
r_s_standard_values = [r_s_standard.subs(M, m).evalf() for m in mass_values]
r_s_entropy_values = [r_s_entropy.subs(M, m).evalf() for m in mass_values]

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(mass_values / 1.989e30, r_s_standard_values, label='Standard GR Model', color='blue')
plt.plot(mass_values / 1.989e30, r_s_entropy_values, label='Entropy-Modified Model', color='lightblue', linestyle='dashed')

# Labels and title
plt.xlabel("Black Hole Mass (Solar Masses)")
plt.ylabel("Schwarzschild Radius (m)")
plt.title("Comparison of Standard and Entropy-Modified Black Hole Models")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
