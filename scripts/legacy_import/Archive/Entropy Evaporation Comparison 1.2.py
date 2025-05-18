# Entropy Evaporation Comparison
# Figure 45

# Mapping entropy horizon τ to physical time via evaporation energy loss
import numpy as np
import matplotlib.pyplot as plt

# Physical constants
G = 6.67430e-11        # m^3 kg^-1 s^-2
hbar = 1.0545718e-34   # Js
c = 299792458          # m/s

# Hawking evaporation power:
def hawking_power(M):
    return (hbar * c**6) / (15360 * np.pi * G**2 * M**2)

def hawking_evaporation_time(M):
    return (5120 * np.pi * G**2 * M**3) / (hbar * c**4)

# Saturation entropy horizon τ:
S_target = 0.999
S_inf = 1.0

# Define entropy horizon

def entropy_horizon(k):
    return -np.log(1 - S_target / S_inf) / k

# Map τ → time using evaporation power
def tau_to_time(M, k, steps):
    P = hawking_power(M)
    total_energy = M * c**2
    dE_per_step = total_energy / steps
    time_per_step = dE_per_step / P
    return steps * time_per_step

# Range of black hole masses
solar_mass = 1.98847e30  # kg
masses = np.logspace(10, 30, 300)

# Test across lower k values
k_values = [0.015, 0.005, 0.001]
colors = ['green', 'orange', 'purple']
labels = ["k = 0.015 (stellar BH)", "k = 0.005 (large-scale field)", "k = 0.001 (cosmological scale)"]

# Compute evaporation reference
evap_times = np.array([hawking_evaporation_time(M) for M in masses])
evap_times_norm = evap_times / np.max(evap_times)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(masses, evap_times_norm, label="Hawking Evaporation Time", color='blue')

for k, color, label in zip(k_values, colors, labels):
    steps = entropy_horizon(k)
    mapped_times = [tau_to_time(M, k, steps) for M in masses]
    mapped_norm = np.array(mapped_times) / np.max(evap_times)
    plt.plot(masses, mapped_norm, linestyle='--', color=color, label=label)

plt.xscale('log')
plt.xlabel("Black Hole Mass (kg)")
plt.ylabel("Normalized Time")
plt.title("Entropy Horizon Mapping for Different k-Scales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
