import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols for black hole properties
M, r_s, S_BH, T_H, L_H = sp.symbols('M r_s S_BH T_H L_H')

# Standard Schwarzschild radius equation
r_s_eq = sp.Eq(r_s, (2 * G * M) / c**2)

# Standard Bekenstein-Hawking entropy equation
S_BH_eq = sp.Eq(S_BH, (k_B * 4 * pi * sp.Pow(r_s, 2)) / (hbar * G / c**3))

# Standard Hawking temperature equation
T_H_eq = sp.Eq(T_H, (hbar * c**3) / (8 * pi * G * M))

# Standard Hawking radiation luminosity equation
L_H_eq = sp.Eq(L_H, (hbar * c**6) / (15360 * pi * G**2 * M**2))

# Display results
print("Schwarzschild radius equation:", r_s_eq)
print("Bekenstein-Hawking entropy equation:", S_BH_eq)
print("Hawking temperature equation:", T_H_eq)
print("Hawking radiation luminosity equation:", L_H_eq)
