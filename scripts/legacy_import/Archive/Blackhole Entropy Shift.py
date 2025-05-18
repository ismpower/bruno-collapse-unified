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
M = sp.Symbol('M', real=True, positive=True)
f_S = sp.Symbol('f_S', real=True, positive=True)
M_critical = 1e5  # Set a hypothetical critical mass in solar masses

# Schwarzschild radius equation (Unchanged)
r_s_eq = (2 * G * M) / c**2

# Modified Bekenstein-Hawking entropy equation
S_BH_eq = sp.Piecewise(
    (2.11848383117005e+47 * pi * r_s_eq**2, M < M_critical),
    (f_S + 2.11848383117005e+47 * pi * r_s_eq**2, M >= M_critical)
)

# Modified Hawking temperature equation
T_H_eq = sp.Piecewise(
    (5.33266392337024 / (pi * M), M < M_critical),
    (f_S + 5.33266392337024 / (pi * M), M >= M_critical)
)

# Modified Hawking radiation luminosity equation
L_H_eq = sp.Piecewise(
    (1.12357230604549e+33 / (pi * M**2), M < M_critical),
    (f_S + 1.12357230604549e+33 / (pi * M**2), M >= M_critical)
)

# Numerical evaluation for plotting
mass_values = np.logspace(1, 8, 100)  # Mass range from 10 to 10^8 solar masses
entropy_values = [S_BH_eq.subs({M: m, f_S: 1e-5}).evalf() for m in mass_values]
temperature_values = [T_H_eq.subs({M: m, f_S: 1e-5}).evalf() for m in mass_values]
radiation_values = [L_H_eq.subs({M: m, f_S: 1e-5}).evalf() for m in mass_values]

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Temperature plot
axes[0].loglog(mass_values, temperature_values, 'c--', label='Entropy-Modified Model')
axes[0].loglog(mass_values, [5.33266392337024 / (pi * m) for m in mass_values], 'b', label='Standard Model')
axes[0].axvline(M_critical, color='k', linestyle='dotted', label='Critical Mass')
axes[0].set_xlabel('Black Hole Mass (Solar Masses)')
axes[0].set_ylabel('Hawking Temperature (K)')
axes[0].set_title('Hawking Temperature Comparison')
axes[0].legend()
axes[0].grid(True, which='both', linestyle='--', linewidth=0.5)

# Radiation Luminosity plot
axes[1].loglog(mass_values, radiation_values, 'r--', label='Entropy-Modified Model')
axes[1].loglog(mass_values, [1.12357230604549e+33 / (pi * m**2) for m in mass_values], 'r', label='Standard Model')
axes[1].axvline(M_critical, color='k', linestyle='dotted', label='Critical Mass')
axes[1].set_xlabel('Black Hole Mass (Solar Masses)')
axes[1].set_ylabel('Hawking Radiation Luminosity (W)')
axes[1].set_title('Hawking Radiation Luminosity Comparison')
axes[1].legend()
axes[1].grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()
