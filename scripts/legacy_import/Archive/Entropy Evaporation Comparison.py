# Compare entropy horizon prediction to black hole evaporation time
# Based on Hawking evaporation time vs. saturation horizon model
# Figure 43

import numpy as np
import matplotlib.pyplot as plt

# Constants (naturalized units)
G = 6.67430e-11       # m^3 kg^-1 s^-2
hbar = 1.0545718e-34  # Js
c = 299792458         # m/s

# Hawking evaporation time (non-rotating, uncharged BH)
# T = 5120 * pi * G^2 * M^3 / (hbar * c^4)
def hawking_evaporation_time(M):
    return (5120 * np.pi * G**2 * M**3) / (hbar * c**4)  # in seconds

# Saturation entropy horizon model
# tau = -ln(1 - 0.999) / k
S_target = 0.999
S_inf = 1.0
k_entropy = 0.015  # from empirical fit

def entropy_horizon(k):
    return -np.log(1 - S_target / S_inf) / k

# Sample black hole masses (solar mass to small)
solar_mass = 1.98847e30  # kg
masses = np.logspace(10, 30, 300)  # range from 10^10 to ~10^30 kg

# Compute evaporation times
evap_times = [hawking_evaporation_time(M) for M in masses]  # seconds

# Normalize evaporation time for visual comparison
evap_times_norm = np.array(evap_times) / np.max(evap_times)

# Compare to entropy horizon
tau_h = entropy_horizon(k_entropy)

# Plot comparison
plt.figure(figsize=(8, 5))
plt.plot(masses, evap_times_norm, label="Normalized Hawking Evaporation Time", color='blue')
plt.axhline(y=tau_h / np.max(evap_times), color='orange', linestyle='--', label=f"Entropy Horizon (k={k_entropy})")
plt.xscale('log')
plt.yscale('linear')
plt.xlabel("Black Hole Mass (kg)")
plt.ylabel("Normalized Time")
plt.title("Evaporation Time vs. Entropy Saturation Horizon")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"Entropy horizon (τ) for k={k_entropy}: {tau_h:.2f} (unitless structural steps)")
