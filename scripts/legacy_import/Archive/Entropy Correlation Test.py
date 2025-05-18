# Figure 46
# Re-test entropy correlation using updated horizon saturation framework
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11
hbar = 1.0545718e-34
c = 299792458

# Structural entropy equation (saturating form)
def entropy_tau(k, tau):
    return 1.0 * (1 - np.exp(-k * tau))

# Hawking temperature (for reference)
def hawking_temperature(M):
    return (hbar * c**3) / (8 * np.pi * G * M * 1.380649e-23)  # using k_B in J/K

# Target: check entropy values at different τ vs black hole surface area or mass
masses = np.logspace(10, 30, 300)
k_val = 0.015

# Compute τ such that S(τ) ≈ 99.9% entropy
tau_horizon = -np.log(1 - 0.999) / k_val

# Generate τ range to compare entropy trend vs Hawking values
tau_values = np.linspace(0, tau_horizon, 300)
entropy_vals = entropy_tau(k_val, tau_values)

# For comparison: entropy from Bekenstein-Hawking
# S_BH = A / (4 * l_p^2), where A = 4πR^2 = 16πG^2M^2 / c^4
l_p_sq = (hbar * G / c**3)
A_vals = 16 * np.pi * G**2 * masses**2 / c**4
S_BH_vals = A_vals / (4 * l_p_sq)
S_BH_norm = S_BH_vals / np.max(S_BH_vals)

# Plot entropy curve from structural model vs Bekenstein-Hawking trend
plt.figure(figsize=(8, 5))
plt.plot(tau_values, entropy_vals, label="Entropy Saturation Model", color='orange')
plt.plot(np.linspace(0, tau_horizon, 300), S_BH_norm, label="Normalized Bekenstein-Hawking Entropy", linestyle='--', color='blue')
plt.xlabel("τ (structural steps)")
plt.ylabel("Entropy (normalized)")
plt.title("Re-Evaluated Correlation: Structural Entropy vs BH Surface Entropy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
