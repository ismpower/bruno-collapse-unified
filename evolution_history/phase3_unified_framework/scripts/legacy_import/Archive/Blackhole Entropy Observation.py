import numpy as np

# Observed black holes dataset (Mass, Spin, Charge Unknown or Estimated)
black_holes = [
    {"name": "Cygnus X-1", "mass": 2.2e+31, "spin": 0.97, "charge": 2.0e+19},
    {"name": "Sagittarius A*", "mass": 8.55e+36, "spin": 0.6, "charge": 1.5e+20},
    {"name": "M87*", "mass": 1.293e+40, "spin": 0.9, "charge": 2.3e+21},
    {"name": "GRO J1655-40", "mass": 1.392e+31, "spin": 0.7, "charge": 1.8e+19},
    {"name": "V404 Cygni", "mass": 1.79e+31, "spin": 0.6, "charge": 1.7e+19},
]

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 299792458  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
l_P = 1.616255e-35  # Planck length (m)

def entropy_kerr_newman(mass, spin, charge):
    """
    Computes the entropy of a Kerr-Newman black hole based on mass, spin, and charge.
    """
    inner_term = 1 - (spin**2 + (charge**2 / (mass**2 * c**4)))
    if inner_term < 0:
        return None  # Invalid case
    r_plus = (G * mass / c**2) * (1 + np.sqrt(inner_term))
    A_horizon = 4 * np.pi * r_plus**2
    entropy = (k_B * A_horizon) / (4 * l_P**2)
    return entropy

# Compute and display entropy values
for bh in black_holes:
    entropy = entropy_kerr_newman(bh["mass"], bh["spin"], bh["charge"])
    print(f"Black Hole: {bh['name']}")
    print(f"Mass: {bh['mass']:.3e} kg, Spin: {bh['spin']:.3f}, Charge: {bh['charge']:.3e} C")
    if entropy is not None:
        print(f"Entropy: {entropy:.3e} J/K")
    else:
        print("Entropy calculation failed due to invalid parameters.")
    print('-' * 50)
