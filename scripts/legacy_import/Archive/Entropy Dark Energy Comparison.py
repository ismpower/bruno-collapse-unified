import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols for density, pressure, entropy function, and Hubble parameter
rho, P, f_S, H = sp.symbols('rho P f_S H')

# Define observed dark energy density (Ω_Λ = 0.7, ρ_crit ≈ 8.5e-27 kg/m³)
rho_dark_energy = 0.7 * 8.5e-27  # kg/m^3

# Compute entropy-driven expansion equation
expansion_eq = f_S - (8.38717273914206e-10 * P + 2.79572424638069e-10 * rho)

# Solve for f_S using observed dark energy density
f_S_dark_energy = expansion_eq.subs({rho: rho_dark_energy, P: 0})  # Assuming negligible pressure component

# Display results
print("Entropy-driven expansion equation:", expansion_eq)
print("Solved entropy function f_S compared to observed dark energy density:", f_S_dark_energy)
