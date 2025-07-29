import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols
H0, f_S_mod = sp.symbols('H0 f_S_mod')

# Standard Hubble constant equation
Hubble_eq = sp.Eq(H0, (8 * pi * G / 3) * f_S_mod)

# Solve for f_S_mod
f_S_mod_value = sp.solve(Hubble_eq, f_S_mod)

# Display result
print("Solved entropy function f_S_mod compared to Hubble constant:", f_S_mod_value)
