import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 299792458  # Speed of light (m/s)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
l_P = 1.616255e-35  # Planck length (m)
hbar = 1.054571817e-34  # Reduced Planck's constant (J·s)
solar_mass_kg = 1.988e30  # Solar mass in kg

# Entropy function
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

# Hawking radiation power formula
def hawking_radiation_power(mass):
    """
    Computes the power (energy loss rate) due to Hawking radiation.
    """
    return (hbar * c**6) / (15360 * np.pi * G**2 * mass**2)

# Entropy evolution function
def entropy_evolution(mass, spin, charge, time_steps=1000000, dt=4.35e17):
    entropy_values = []
    mass_values = []
    current_mass = mass  # Ensure current_mass is properly initialized

    for step in range(int(time_steps)):  
        entropy = entropy_kerr_newman(current_mass, spin, charge)
        if entropy is None:
            print(f"⚠ Stopping early at step {step}: Invalid entropy.")
            break

        entropy_values.append(entropy)
        mass_values.append(current_mass)

        # Compute Hawking radiation loss
        power_loss = hawking_radiation_power(current_mass)
        energy_loss = power_loss * dt
        mass_loss = energy_loss / c**2  # Convert energy loss to mass loss

        # Debugging: Print first 10 iterations
        if step < 10:
            print(f"Step {step}: Mass = {current_mass:.3e} kg, Entropy = {entropy:.3e} J/K")
            print(f"Power Loss = {power_loss:.3e} W, Energy Loss = {energy_loss:.3e} J, Mass Loss = {mass_loss:.3e} kg")

        # Update mass
        current_mass -= mass_loss
        if current_mass <= 0:
            print("⚠ Black hole fully evaporated.")
            break

    return np.array(mass_values), np.array(entropy_values)

# Test values
mass_test = 1e4 * solar_mass_kg  # Sagittarius A* (kg)
spin_test = 0.6
charge_test = 0

# Compute entropy evolution
mass_values, entropy_values = entropy_evolution(mass_test, spin_test, charge_test)

# Display results
if len(mass_values) > 0 and len(entropy_values) > 0:
    plt.figure(figsize=(8, 5))
    plt.plot(mass_values, entropy_values, label="Entropy Evolution")
    plt.xlabel("Mass (kg)")
    plt.ylabel("Entropy (J/K)")
    plt.title("Black Hole Entropy Evolution - Sagittarius A*")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("⚠ No data to plot. Check entropy evolution calculations.")
