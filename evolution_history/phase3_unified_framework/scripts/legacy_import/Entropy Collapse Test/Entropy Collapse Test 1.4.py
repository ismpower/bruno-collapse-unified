# Goal: Find a correlation between average temperature of the universe, its age, and Hubble constant
# Hypothesis: Our entropy-first model should align with existing cosmological constants in a way that forms a meaningful relation

import math

# Constants
k_B = 1.380649e-23         # Boltzmann constant (J/K)
h = 6.62607015e-34         # Planck constant (J·s)
c = 299792458              # Speed of light (m/s)
G = 6.67430e-11            # Gravitational constant (m^3 kg^-1 s^-2)
sigma = 5.670374419e-8     # Stefan-Boltzmann constant (W/m^2/K^4)

# Cosmological data (current universe)
T_universe = 2.725          # Average temperature of the observable universe in Kelvin
age_universe_yr = 13.8e9    # Age of the universe in years
age_universe_s = age_universe_yr * 365.25 * 24 * 3600
H0_km_s_Mpc = 70            # Hubble constant in km/s/Mpc

# Convert Hubble constant to 1/s
H0 = H0_km_s_Mpc * 1000 / (3.085677581e22)  # in s^-1

# Radiation constant
a_rad = 4 * sigma / c

# Calculate current universe values
energy_density = a_rad * T_universe**4  # J/m^3
entropy_density = (4/3) * a_rad * T_universe**3  # J/K/m^3
cosmic_entropy_factor = entropy_density * age_universe_s * H0

print("--- Current Universe ---")
print("Average Temperature (K):", T_universe)
print("Age (s):", age_universe_s)
print("Hubble Constant (1/s):", H0)
print("Energy Density (J/m^3):", energy_density)
print("Entropy Density (J/K/m^3):", entropy_density)
print("Cosmic Entropy Correlation Factor (CECF):", cosmic_entropy_factor)

# --- Recombination Era ---
# T ~ 3000K, age ~ 380,000 years, H ~ 1.8e-13 1/s (est. from expansion rate at z~1100)
T_recombination = 3000
age_recombination_s = 380000 * 365.25 * 24 * 3600
H_recombination = 1.8e-13  # approx value in 1/s

energy_density_rec = a_rad * T_recombination**4
entropy_density_rec = (4/3) * a_rad * T_recombination**3
cosmic_entropy_factor_rec = entropy_density_rec * age_recombination_s * H_recombination

print("\n--- Recombination Era ---")
print("Temperature (K):", T_recombination)
print("Age (s):", age_recombination_s)
print("Hubble Constant (1/s):", H_recombination)
print("Energy Density (J/m^3):", energy_density_rec)
print("Entropy Density (J/K/m^3):", entropy_density_rec)
print("Cosmic Entropy Correlation Factor (CECF):", cosmic_entropy_factor_rec)
