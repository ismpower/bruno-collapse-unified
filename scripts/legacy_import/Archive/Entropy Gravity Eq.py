import sympy as sp

# Define fundamental constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols
M, r_s, S_BH, T_H, L_H, f_S, rho, a, P = sp.symbols('M r_s S_BH T_H L_H f_S rho a P')

# Schwarzschild radius equation
r_s_eq = sp.Eq(r_s, (2 * G * M) / c**2)

# Bekenstein-Hawking entropy equation with entropy modification
S_BH_eq = sp.Eq(S_BH, f_S + (k_B * 4 * pi * r_s**2) / (hbar * G / c**3))

# Hawking temperature equation with entropy modification
T_H_eq = sp.Eq(T_H, f_S + (hbar * c**3) / (8 * pi * G * M))

# Hawking radiation luminosity equation with entropy modification
L_H_eq = sp.Eq(L_H, f_S + (hbar * c**6) / (15360 * pi * G**2 * M**2))

# Entropy-driven expansion equation (modification to standard cosmology)
expansion_eq = sp.Eq(sp.diff(a, a, 2) / a, -(4 * pi * G / 3) * (rho + 3 * P) + f_S)

# Display equations
print("Schwarzschild radius equation:", r_s_eq)
print("Bekenstein-Hawking entropy equation:", S_BH_eq)
print("Hawking temperature equation:", T_H_eq)
print("Hawking radiation luminosity equation:", L_H_eq)
print("Entropy-driven expansion equation:", expansion_eq)
