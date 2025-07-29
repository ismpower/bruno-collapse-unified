import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols
M, r_s, S_BH, T_H, L_H, M_critical, f_S = sp.symbols('M r_s S_BH T_H L_H M_critical f_S')

# Schwarzschild radius equation (unchanged)
r_s_eq = sp.Eq(r_s, (2 * G * M) / c**2)

# Modified Bekenstein-Hawking entropy equation with entropy stabilization effect
S_BH_eq = sp.Piecewise(
    (k_B * 4 * pi * sp.Pow(r_s, 2) / (hbar * G / c**3), M < M_critical),  # Standard regime
    (f_S + k_B * 4 * pi * sp.Pow(r_s, 2) / (hbar * G / c**3), True)  # Entropy-stabilized regime
)

# Modified Hawking temperature equation
T_H_eq = sp.Piecewise(
    ((hbar * c**3) / (8 * pi * G * M), M < M_critical),  # Standard model
    (f_S + (hbar * c**3) / (8 * pi * G * M), True)  # Stabilized regime
)

# Hawking radiation luminosity equation (remains unchanged)
L_H_eq = sp.Piecewise(
    ((hbar * c**6) / (15360 * pi * G**2 * M**2), M < M_critical),  # Standard model
    (f_S + (hbar * c**6) / (15360 * pi * G**2 * M**2), True)  # Stabilized regime
)

# Display equations
print("Modified Schwarzschild radius equation:", r_s_eq)
print("Modified Bekenstein-Hawking entropy equation:", S_BH_eq)
print("Modified Hawking temperature equation:", T_H_eq)
print("Modified Hawking radiation luminosity equation:", L_H_eq)
