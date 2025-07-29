# Re-test entropy correlation using updated horizon saturation framework
# Figure 47
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11
hbar = 1.0545718e-34
c = 299792458

# Structural entropy equation (saturating form)
def entropy_tau(k, tau):
    return 1.0 * (1 - np.exp(-k * tau))

# Range of black hole masses
masses = np.logspace(10, 30, 300)
k_val = 0.015

# Structural mapping: Let τ scale with surface area (A ∝ M²)
l_p_sq = (hbar * G / c**3)
A_vals = 16 * np.pi * G**2 * masses**2 / c**4
A_norm = A_vals / np.max(A_vals)

# Assume τ = normalized area * max_tau
tau_max = -np.log(1 - 0.999) / k_val
scaled_tau = A_norm * tau_max

# Entropy from saturation model
entropy_vals = entropy_tau(k_val, scaled_tau)

# For comparison: entropy from Bekenstein-Hawking
S_BH_vals = A_vals / (4 * l_p_sq)
S_BH_norm = S_BH_vals / np.max(S_BH_vals)

# Plot comparison
plt.figure(figsize=(8, 5))
plt.plot(scaled_tau, entropy_vals, label="Entropy Saturation Model", color='orange')
plt.plot(scaled_tau, S_BH_norm, label="Normalized Bekenstein-Hawking Entropy", linestyle='--', color='blue')
plt.xlabel("τ (rescaled via A ∝ M²)")
plt.ylabel("Entropy (normalized)")
plt.title("Structural Entropy vs BH Surface Entropy (Area-Matched)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
