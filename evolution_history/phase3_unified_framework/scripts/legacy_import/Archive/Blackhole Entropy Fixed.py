import numpy as np

def entropy_kerr_newman(mass, spin, charge):
    """
    Computes the entropy of a Kerr-Newman black hole based on mass, spin, and charge.

    Parameters:
    mass (float or array): Black hole mass in kg
    spin (float or array): Dimensionless spin parameter (0 to ~0.998)
    charge (float or array): Charge in Coulombs

    Returns:
    float or array: Estimated entropy (J/K) or None if an invalid condition is met
    """
    G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
    c = 299792458  # Speed of light (m/s)
    k_B = 1.380649e-23  # Boltzmann constant (J/K)
    l_P = 1.616255e-35  # Planck length (m)

    # Schwarzschild radius for a non-rotating, non-charged case
    r_s = (2 * G * mass) / c**2

    # Ensure that the term inside sqrt() does not become negative
    inner_term = 1 - (spin**2 + (charge**2 / (mass**2 * c**4)))

    print(f"Checking values: mass={mass}, spin={spin}, charge={charge}")
    print(f"inner_term: {inner_term}")

    if np.any(inner_term < 0):
        print("⚠ ERROR: Invalid Kerr-Newman parameters! sqrt of negative number detected.")
        return None

    # Event horizon radius for Kerr-Newman black hole
    r_plus = (G * mass / c**2) * (1 + np.sqrt(inner_term))

    print(f"r_plus: {r_plus}")

    # Horizon area
    A_horizon = 4 * np.pi * r_plus**2

    print(f"A_horizon: {A_horizon}")

    # Entropy formula (Bekenstein-Hawking with corrections for spin and charge)
    entropy = (k_B * A_horizon) / (4 * l_P**2)

    print(f"Entropy computed: {entropy}")

    return entropy

# Test values
mass_values = np.array([1.8e+31, 2.0e+31, 2.2e+31])  # kg
spin_values = np.array([0.1, 0.5, 0.98])  # Near-zero to maximal spin
charge_values = np.array([1.0e19, 2.0e19, 3.0e19])  # Coulombs

# Compute entropy values
entropy_results = entropy_kerr_newman(mass_values, spin_values, charge_values)

# Display results
if entropy_results is not None:
    for i in range(len(mass_values)):
        print(f"Mass: {mass_values[i]:.3e} kg, Spin: {spin_values[i]:.3f}, Charge: {charge_values[i]:.3e} C")
        print(f"Entropy: {entropy_results[i]:.3e} J/K")
        print('-' * 50)
else:
    print("❌ Entropy function returned None. Check error messages above.")
