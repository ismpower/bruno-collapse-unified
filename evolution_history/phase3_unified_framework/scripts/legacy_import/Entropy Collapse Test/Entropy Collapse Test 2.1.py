# Goal: Find a correlation between average temperature of the universe, its age, and Hubble constant
# Extension: Use residual plots to show delta between entropy-derived temperature and Planck temperature for given energy flux
# Overlay known physical temperature benchmarks for reference, plus model-derived counterparts for visual comparison
# Overlay tangency point where entropy and Planck models become tangent (k ≈ 0.001005)
# Compare black hole surface entropy to Chajar core temperature to reveal internal boundary and estimate minimal entropy volume
# NEW: Compare surface entropy density to volumetric Chajar density (supporting 2D holographic structure)

import math
import matplotlib.pyplot as plt

# Constants
k_B = 1.380649e-23         # Boltzmann constant (J/K)
h = 6.62607015e-34         # Planck constant (J·s)
c = 299792458              # Speed of light (m/s)
G = 6.67430e-11            # Gravitational constant (m^3 kg^-1 s^-2)
sigma = 5.670374419e-8     # Stefan-Boltzmann constant (W/m^2/K^4)

# Radiation constant
a_rad = 4 * sigma / c

# Temperature range (log scale up to Planck temperature)
T_range = [10**i for i in range(1, 33)]  # from 10 K to ~1e32 K
T_planck = (h * c**5 / G)**0.5 / k_B     # Planck temperature in K

# Compute energy flux for each temperature and compare to Planck temperature
fluxes = [a_rad * T**4 for T in T_range]
entropy_temps = [(F / a_rad)**0.25 for F in fluxes]
residuals = [(T - T_planck) / T_planck for T in entropy_temps]

# Reference temperatures
reference_points = {
    "CMB (~2.73 K)": 2.73,
    "Solar Core (~1.5e7 K)": 1.5e7,
    "Supernova Core (~1e9 K)": 1e9,
    "Fusion Reactor (~1e8 K)": 1e8,
    "Hawking (10 solar mass BH ~6e-9 K)": 6e-9,
    "Early Universe (~1e26 K)": 1e26
}

model_points = {}
for label, T_ref in reference_points.items():
    F_ref = a_rad * T_ref**4
    T_model = (F_ref / a_rad)**0.25
    model_points[f"Model of {label}"] = T_model

k_chajar = 0.001005
T_tangent = T_planck * k_chajar

S_ns = 3.6109978336801644e34
S_bh = 7.009474410896821e54
K_collapse = S_bh / S_ns

entropy_density_chajar = (4/3) * a_rad * T_tangent**3
volume_required = S_bh / entropy_density_chajar

M_solar = 1.98847e30
mass_bh = 10 * M_solar
r_s = 2 * G * mass_bh / c**2
volume_bh = (4/3) * math.pi * r_s**3
surface_area_bh = 4 * math.pi * r_s**2
surface_entropy_density = S_bh / surface_area_bh

print("Chajar Constant (k ≈ 0.001005)")
print("Tangent Temperature (K):", T_tangent)
print("Black Hole Entropy (S_bh):", S_bh)
print("Neutron Star Entropy (S_ns):", S_ns)
print("Entropy Collapse Ratio (K_collapse = S_bh / S_ns):", K_collapse)
print("\nEstimated Entropy Density at Chajar T (J/K/m^3):", entropy_density_chajar)
print("Volume Required to Contain S_bh at Chajar T (m^3):", volume_required)
print("Reference BH Volume (m^3):", volume_bh)
print("Reference BH Surface Area (m^2):", surface_area_bh)
print("Surface Entropy Density (J/K/m^2):", surface_entropy_density)

# Plotting
plt.figure(figsize=(12, 7))
plt.plot(T_range, residuals, marker='o', linestyle='-', color='blue', label="Residual vs Planck T")
plt.xscale('log')
plt.axhline(0, color='gray', linestyle='--')

for label, temp in reference_points.items():
    plt.axvline(temp, linestyle='--', linewidth=1, color='black', label=label)
for label, temp in model_points.items():
    plt.axvline(temp, linestyle='--', linewidth=1, color='red', label=label)

plt.axvline(T_tangent, linestyle='-.', linewidth=2, color='green', label="Tangency Point (Chajar Constant ≈ 0.001005)")

plt.title("Residuals Between Entropy-Based Temp and Planck Temp with Reference + Model Lines")
plt.xlabel("Entropy-Derived Temperature (K)")
plt.ylabel("(T - T_planck) / T_planck")
plt.grid(True, which='both', ls='--')
plt.legend(loc='lower right', fontsize='small')
plt.tight_layout()
plt.show()
