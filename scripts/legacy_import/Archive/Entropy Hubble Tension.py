import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
pi = sp.pi

# Define symbols for density, pressure, entropy function, Hubble parameter
rho, P, f_S, H = sp.symbols('rho P f_S H')

# Define Hubble constant values from different measurements
Hubble_CMB = 67.4e3 / (3.086e22)  # Planck 2018 (CMB) measurement in s^-1
Hubble_SN = 73.0e3 / (3.086e22)  # Supernovae measurements in s^-1

# Compute entropy-driven expansion equation
expansion_eq = f_S - (8.38717273914206e-10 * P + 2.79572424638069e-10 * rho)

# Solve for f_S using different Hubble values
f_S_CMB = expansion_eq.subs({H: Hubble_CMB, P: 0, rho: 2.775e-27 * 0.3})
f_S_SN = expansion_eq.subs({H: Hubble_SN, P: 0, rho: 2.775e-27 * 0.3})

# Compare the difference
f_S_difference = f_S_SN - f_S_CMB

# Display results
print("Entropy-driven expansion equation:", expansion_eq)
print("Solved entropy function f_S for CMB Hubble value:", f_S_CMB)
print("Solved entropy function f_S for Supernovae Hubble value:", f_S_SN)
print("Difference in entropy function f_S between Hubble measurements:", f_S_difference)
