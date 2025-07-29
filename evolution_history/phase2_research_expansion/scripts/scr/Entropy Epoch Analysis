import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols for density, pressure, Hubble parameter, entropy function, and scale factor
rho, P, f_S, H, a = sp.symbols('rho P f_S H a')

# Define cosmic epoch parameters (placeholders, replace with real data)
epochs = {
    "Early Universe": {"rho": 1e-18, "P": 1e-15, "H": 1e-14},  # Radiation-dominated
    "Matter-Dominated Era": {"rho": 2.775e-27 * 0.3, "P": 1e-12, "H": 2.0e-18},
    "Late-Time Acceleration": {"rho": 2.775e-27 * 0.3, "P": 5e-10, "H": 6.7e-18}  # Dark energy era
}

# Compute entropy-driven expansion equation
expansion_eq = f_S - (8.38717273914206e-10 * P + 2.79572424638069e-10 * rho)

# Solve for f_S at different cosmic epochs
f_S_values = {epoch: expansion_eq.subs(params) for epoch, params in epochs.items()}

# Display results
print("Entropy-driven expansion equation:", expansion_eq)
for epoch, f_S_value in f_S_values.items():
    print(f"Solved entropy function f_S for {epoch}:", f_S_value)
