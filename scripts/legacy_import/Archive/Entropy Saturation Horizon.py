# Figure 51

import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 0.001  # cosmological decay scale
S_inf = 0.99999999  # target saturation entropy

# Compute entropy horizon τ_max
tau_max = -np.log(1 - S_inf) / k

# Hubble constants (km/s/Mpc)
H0_planck = 67.4
H0_shoes = 73.0

# Convert to age in Gyr (approximate: 9.78 / (H0 / 100))
t_planck = 9.78 / (H0_planck / 100)
t_shoes = 9.78 / (H0_shoes / 100)

# Time range and τ mapping
times = np.linspace(t_shoes, t_planck, 100)
tau_vals = tau_max * (times / t_shoes)  # Linear mapping relative to SH0ES baseline

# Plot
plt.figure(figsize=(10, 5))
plt.plot(times, tau_vals, label="Entropy τ across H₀ range", color='blue')
plt.axhline(y=tau_max, color='red', linestyle='--', label=f"SH0ES τ ≈ {tau_max:.1f}")
plt.axhline(y=tau_max * (t_planck / t_shoes), color='blue', linestyle='--', label=f"Planck τ ≈ {tau_max * (t_planck / t_shoes):.1f}")
plt.title("Entropy Saturation Horizon vs Hubble Tension")
plt.xlabel("Cosmic Time (Gyr)")
plt.ylabel("Structural Entropy τ")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
