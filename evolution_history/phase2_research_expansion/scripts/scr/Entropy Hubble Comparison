import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
H0 = 2.2e-18  # Approximate Hubble constant in 1/s

# Define entropy function symbols
f_S, f_S_mod, epsilon = sp.symbols('f_S f_S_mod epsilon')

# Initial entropy function
f_S_value = 1.16549612154152e-23

# Modified entropy function
f_S_mod_value = 1.16549612154152e-23 - epsilon

# Hubble constant comparison
hubble_result_standard = f_S_value - H0
hubble_result_modified = f_S_mod_value - H0

# Display results
print(f"f_S (Standard) compared to Hubble constant: {hubble_result_standard}")
print(f"f_S_mod (Modified) compared to Hubble constant: {hubble_result_modified}")
