# Goal: Find a correlation between average temperature of the universe, its age, and Hubble constant
# Extension: Use residual plots to show delta between entropy-derived temperature and Planck temperature for given energy flux
# Figure 61


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

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(T_range, residuals, marker='o', linestyle='-', color='blue')
plt.xscale('log')
plt.axhline(0, color='gray', linestyle='--')
plt.title("Residuals Between Entropy-Based Temp and Planck Temp")
plt.xlabel("Entropy-Derived Temperature (K)")
plt.ylabel("(T - T_planck) / T_planck")
plt.grid(True, which='both', ls='--')
plt.tight_layout()
plt.show()
