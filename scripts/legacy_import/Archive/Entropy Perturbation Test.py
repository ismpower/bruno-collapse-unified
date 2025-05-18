import sympy as sp

# Define constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
H0 = 2.2e-18  # Approximate Hubble constant (1/s)

# Define symbols
rho, P, f_S, epsilon = sp.symbols('rho P f_S epsilon')

# Define entropy function with a small perturbation term
test_f_S = f_S + epsilon

# Re-run entropy-driven expansion equation with perturbation
test_expansion_eq = sp.Eq(test_f_S - (8.38717273914206e-10 * P + 2.79572424638069e-10 * rho), 0)

# Solve for perturbation effect
perturbation_result = sp.solve(test_expansion_eq, f_S)

# Check for stability by setting epsilon to a small value
epsilon_test_values = [0, 1e-10, 1e-5, 1e-3, 1]  # Different perturbation levels
results = {eps: perturbation_result[0].subs(epsilon, eps) for eps in epsilon_test_values}

# Compare with Hubble constant equation
hubble_eq = sp.Eq(test_f_S - 1.16549612154152e-23, 0)
hubble_result = sp.solve(hubble_eq, f_S)

# Display results
print("Entropy function perturbation test results:")
for eps, res in results.items():
    print(f"For perturbation epsilon={eps}: f_S = {res}")

print("\nEntropy function comparison with Hubble constant:")
print(f"f_S (Hubble comparison) = {hubble_result}")
