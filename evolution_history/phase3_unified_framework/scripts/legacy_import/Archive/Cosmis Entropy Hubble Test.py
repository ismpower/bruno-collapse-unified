# Cosmic Entropy Model Applied to Hubble Tension – Entropy-Driven Interpretation

import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11         # m^3 kg^-1 s^-2
hbar = 1.054571817e-34  # J*s
c = 299792458           # m/s
kB = 1.380649e-23       # J/K

# Hubble constant estimates (in km/s/Mpc → converted to 1/s)
H0_planck = 67.4 * 1000 / (3.0857e22)  # Planck (CMB-based)
H0_shoes = 73.0 * 1000 / (3.0857e22)   # SH0ES (supernova-based)

# Characteristic cosmic time from Hubble parameter (1/H0)
t_planck = 1 / H0_planck  # ~age of universe (Planck estimate)
t_shoes = 1 / H0_shoes

# Structural entropy horizon model
k_val = 0.001005  # from BH tangent test
S_inf = 0.9999999999  # or even 0.999999

# Invert the model to solve for τ at cosmic age scale
def tau_from_time(t, k):
    return -np.log(1 - S_inf) / k  # assume full saturation (S → 1)

# Normalize time to max (set Planck τ as 1.0 for reference)
tau_planck = tau_from_time(t_planck, k_val)
tau_shoes = tau_from_time(t_shoes, k_val)

# Plot scaled entropy slope based on time differences
times = np.linspace(t_shoes, t_planck, 300)
tau_vals = -np.log(1 - S_inf) / k_val * (times / t_planck)  # linear scaling for visualization

plt.figure(figsize=(8, 5))
plt.plot(times / (1e9 * 60 * 60 * 24 * 365.25), tau_vals, label="Entropy τ across H0 range")
plt.axhline(y=tau_planck, color='blue', linestyle='--', label=f"Planck τ ≈ {tau_planck:.1f}")
plt.axhline(y=tau_shoes, color='red', linestyle='--', label=f"SH0ES τ ≈ {tau_shoes:.1f}")
plt.xlabel("Cosmic Time (Gyr)")
plt.ylabel("Structural Entropy τ")
plt.title("Entropy Saturation Horizon vs Hubble Tension")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Planck-based τ:", tau_planck)
print("SH0ES-based τ:", tau_shoes)
print("Δτ from Hubble tension:", abs(tau_planck - tau_shoes))
