# Mapping entropy horizon τ to physical time via evaporation energy loss
import numpy as np
import matplotlib.pyplot as plt

# Physical constants
G = 6.67430e-11        # m^3 kg^-1 s^-2
hbar = 1.0545718e-34   # Js
c = 299792458          # m/s

# Evaporation power output from Hawking radiation:
# Power = ħc^6 / (15360πG^2M^2)
def hawking_power(M):
    return (hbar * c**6) / (15360 * np.pi * G**2 * M**2)

# Evaporation time from full integration (for reference)
def hawking_evaporation_time(M):
    return (5120 * np.pi * G**2 * M**3) / (hbar * c**4)

# Structural entropy saturation horizon τ
S_target = 0.999
S_inf = 1.0
k_entropy = 0.015

def entropy_horizon(k):
    return -np.log(1 - S_target / S_inf) / k

# Define a mapping τ → t via energy decay, assuming discrete loss per τ-step
def tau_to_time(M, k, steps=460):
    P = hawking_power(M)  # W = J/s
    total_energy = M * c**2  # J
    dE_per_step = total_energy / steps  # average energy loss per τ
    time_per_step = dE_per_step / P  # s
    return steps * time_per_step  # total mapped time

# Test on various black hole masses
solar_mass = 1.98847e30  # kg
masses = np.logspace(10, 30, 300)

# Compare Hawking full evaporation time vs mapped τ-time
mapped_tau_times = [tau_to_time(M, k_entropy, steps=entropy_horizon(k_entropy)) for M in masses]
evap_times = [hawking_evaporation_time(M) for M in masses]

mapped_tau_times = np.array(mapped_tau_times)
evap_times = np.array(evap_times)

# Normalize for shape comparison
mapped_tau_times_norm = mapped_tau_times / np.max(evap_times)
evap_times_norm = evap_times / np.max(evap_times)

# Plot comparison
plt.figure(figsize=(8, 5))
plt.plot(masses, evap_times_norm, label="Hawking Evaporation Time", color='blue')
plt.plot(masses, mapped_tau_times_norm, label="τ to Time Mapping (Entropy Horizon)", color='green', linestyle='--')
plt.xscale('log')
plt.xlabel("Black Hole Mass (kg)")
plt.ylabel("Normalized Time")
plt.title("Mapping τ to Physical Time via Hawking Energy Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
