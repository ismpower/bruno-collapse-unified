import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols for black hole properties
M, r_s, S_BH = sp.symbols('M r_s S_BH')  # Mass, Schwarzschild radius, entropy function

# Schwarzschild radius equation (event horizon definition)
r_s_eq = sp.Eq(r_s, (2 * G * M) / c**2)

# Bekenstein-Hawking entropy equation for a black hole
S_BH_eq = sp.Eq(S_BH, (k_B * 4 * pi * r_s**2) / (4 * hbar * G / c**3))

# Standard Einstein Field Equations (GR framework)
Lambda, g_mu_nu, T_mu_nu = sp.symbols('Lambda g_mu_nu T_mu_nu')
Einstein_eq = sp.Eq(G + Lambda * g_mu_nu, (8 * pi * G / c**4) * T_mu_nu)

# Display results
print("Schwarzschild radius equation:", r_s_eq)
print("Bekenstein-Hawking entropy equation:", S_BH_eq)
print("Standard Einstein Field Equation:", Einstein_eq)
