# Goal: Find a correlation between average temperature of the universe, its age, and Hubble constant
# Extension: Use residual plots to show delta between entropy-derived temperature and Planck temperature for given energy flux
# Overlay known physical temperature benchmarks for reference, plus model-derived counterparts for visual comparison
# Overlay tangency point where entropy and Planck models become tangent (k ≈ 0.001005)
# NEW: Compare black hole surface entropy to Chajar core temperature to reveal internal boundary

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
entropy_temps = [(F / a_rad)**0.25 for F in fluxes]  # Derived back from flux
residuals = [(T - T_planck) / T_planck for T in entropy_temps]

# Known physics reference temperatures (K)
reference_points = {
    "CMB (~2.73 K)": 2.73,
    "Solar Core (~1.5e7 K)": 1.5e7,
    "Supernova Core (~1e9 K)": 1e9,
    "Fusion Reactor (~1e8 K)": 1e8,
    "Hawking (10 solar mass BH ~6e-9 K)": 6e-9,
    "Early Universe (~1e26 K)": 1e26
}

# Compute model-derived temperatures from flux for each reference point
model_points = {}
for label, T_ref in reference_points.items():
    F_ref = a_rad * T_ref**4
    T_model = (F_ref / a_rad)**0.25
    model_points[f"Model of {label}"] = T_model

# Tangency point overlay (k ≈ 0.001005) applied to Planck temperature
k_chajar = 0.001005  # Chajar Constant: entropy tangency threshold
T_tangent = T_planck * k_chajar

# Compare black hole surface entropy to neutron star
S_ns = 3.6109978336801644e34   # Neutron Star Entropy (J/K)
S_bh = 7.009474410896821e54    # Black Hole Entropy (J/K)
K_collapse = S_bh / S_ns       # Collapse entropy ratio (dimensionless)

print("Chajar Constant (k ≈ 0.001005)")
print("Tangent Temperature (K):", T_tangent)
print("Black Hole Entropy (S_bh):", S_bh)
print("Neutron Star Entropy (S_ns):", S_ns)
print("Entropy Collapse Ratio (K_collapse = S_bh / S_ns):", K_collapse)

# Plotting
plt.figure(figsize=(12, 7))
plt.plot(T_range, residuals, marker='o', linestyle='-', color='blue', label="Residual vs Planck T")
plt.xscale('log')
plt.axhline(0, color='gray', linestyle='--')

# Overlay reference points (benchmark lines)
for label, temp in reference_points.items():
    plt.axvline(temp, linestyle='--', linewidth=1, color='black', label=label)

# Overlay model-derived temperatures (as red dashed lines)
for label, temp in model_points.items():
    plt.axvline(temp, linestyle='--', linewidth=1, color='red', label=label)

# Overlay the tangency point
plt.axvline(T_tangent, linestyle='-.', linewidth=2, color='green', label="Tangency Point (Chajar Constant ≈ 0.001005)")

plt.title("Residuals Between Entropy-Based Temp and Planck Temp with Reference + Model Lines")
plt.xlabel("Entropy-Derived Temperature (K)")
plt.ylabel("(T - T_planck) / T_planck")
plt.grid(True, which='both', ls='--')
plt.legend(loc='lower right', fontsize='small')
plt.tight_layout()
plt.show()
