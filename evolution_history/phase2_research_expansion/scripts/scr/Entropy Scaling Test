import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
H0 = 2.2e-18  # Approximate Hubble constant in 1/s

# Define entropy scaling parameters
f_S, f_S_mod, epsilon, alpha = sp.symbols('f_S f_S_mod epsilon alpha')

# Introduce scaling factor alpha
f_S_scaled = alpha * (1.16549612154152e-23 - epsilon)

# Hubble constant comparison with scaling
hubble_result_scaled = f_S_scaled - H0

# Solve for alpha if we force equality with H0
alpha_solution = sp.solve(sp.Eq(hubble_result_scaled, 0), alpha)

# Display results
print(f"f_S_scaled compared to Hubble constant: {hubble_result_scaled}")
print(f"Required alpha for exact match: {alpha_solution}")
