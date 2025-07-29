# Goal: Compare entropy of neutron star (NS) vs black hole (BH) to define a collapse threshold constant
# Then explore whether this constant K_collapse can be applied to systems like superconductors

import math

# Constants
G = 6.67430e-11         # Gravitational constant (m^3 kg^-1 s^-2)
c = 299792458           # Speed of light (m/s)
k_B = 1.380649e-23      # Boltzmann constant (J/K)
hbar = 1.054571817e-34  # Reduced Planck constant (J*s)

# Solar mass in kg
M_sun = 1.98847e30

# Estimate entropy of a black hole (Bekenstein-Hawking formula)
def black_hole_entropy(mass_kg):
    area = 16 * math.pi * (G * mass_kg / c**2)**2  # Event horizon area for Schwarzschild BH
    S_bh = (k_B * area * c**3) / (4 * G * hbar)
    return S_bh

# Estimate entropy of a neutron star (approximate model)
def neutron_star_entropy(mass_kg, radius_m):
    # Assuming T ~ 1e6 K and typical neutron star specific entropy per baryon ~ 1 k_B
    # Number of baryons N ~ mass / mass_proton
    m_p = 1.6726219e-27
    N_baryons = mass_kg / m_p
    S_ns = N_baryons * k_B  # ~1 k_B per baryon
    return S_ns

# Test entropy collapse threshold at neutron star limit
mass_ns = 2.2 * M_sun        # Critical neutron star mass (~TOV limit)
radius_ns = 12e3             # Approximate radius in meters (12 km)

S_ns = neutron_star_entropy(mass_ns, radius_ns)
S_bh = black_hole_entropy(mass_ns)
K_collapse = S_bh / S_ns  # Define entropy collapse threshold ratio

print("Neutron Star Entropy (S_ns):", S_ns, "J/K")
print("Black Hole Entropy (S_bh):", S_bh, "J/K")
print("Entropy Collapse Ratio (K_collapse = S_bh / S_ns):", K_collapse)

# Apply K_collapse to a superconducting system
# Hypothetical: Can we detect a structural entropy drop in lab settings?

# Assume experimental material entropy before superconductivity
entropy_normal_state = 1e-3  # J/K per mole (approximation for metals)
entropy_superconducting = entropy_normal_state / K_collapse  # if collapse mimics BH

print("\nEstimated Entropy in Superconducting State using K_collapse:", entropy_superconducting, "J/K per mole")
