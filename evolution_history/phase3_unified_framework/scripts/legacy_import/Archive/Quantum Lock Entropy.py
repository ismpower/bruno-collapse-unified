import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 299792458  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
l_P = 1.616255e-35  # Planck length (m)
hbar = 1.054571817e-34  # Reduced Planck's constant (J·s)
planck_mass = 2.17651e-8  # Planck mass in kg

# Function to compute entropy with quantum stabilization

def entropy_quantum_locked(mass, spin, charge):
    """
    Computes the entropy of a black hole, incorporating a stabilization effect at the Planck scale.
    """
    inner_term = 1 - (spin**2 + (charge**2 / (mass**2 * c**4)))
    if inner_term < 0:
        return None  # Invalid case
    r_plus = (G * mass / c**2) * (1 + np.sqrt(inner_term))
    A_horizon = 4 * np.pi * r_plus**2
    entropy = (k_B * A_horizon) / (4 * l_P**2)
    
    # Introduce stabilization effect at Planck mass scale
    if mass <= planck_mass:
        entropy *= np.exp(-mass / planck_mass)  # Exponential suppression at small scales
    
    return entropy

# Test values for different mass scales
mass_values = np.logspace(np.log10(planck_mass), np.log10(1e31), num=50)  # Log-spaced values
spin_test = 0.6  # Typical spin
charge_test = 0  # Neutral case

# Compute entropy
entropy_results = [entropy_quantum_locked(m, spin_test, charge_test) for m in mass_values]

# Display results
for i, (mass, entropy) in enumerate(zip(mass_values, entropy_results)):
    print(f"Step {i}: Mass = {mass:.3e} kg, Entropy = {entropy:.3e} J/K")
