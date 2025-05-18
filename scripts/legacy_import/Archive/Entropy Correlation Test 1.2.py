# Re-test entropy correlation using updated horizon saturation framework
# Figure 48
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Constants
G = 6.67430e-11
hbar = 1.0545718e-34
c = 299792458

# Structural entropy equation (saturating form)
def entropy_tau(k, tau):
    return 1.0 * (1 - np.exp(-k * tau))

def entropy_tau_derivative(k, tau):
    return k * np.exp(-k * tau)

# Normalized Bekenstein-Hawking entropy is linear in area → S_BH_norm = tau / tau_max
# Find k where entropy curve is tangent to S_BH_norm = tau / tau_max

# Objective: minimize the squared difference between slope of saturation model and linear model at some point

def tangent_loss(k):
    tau_max = -np.log(1 - 0.999) / k
    tau_test = 0.3 * tau_max  # test near 30% to avoid edge bias
    sat_slope = entropy_tau_derivative(k, tau_test)
    lin_slope = 1.0 / tau_max
    return abs(sat_slope - lin_slope)

# Minimize the loss to find best tangent match
res = minimize_scalar(tangent_loss, bounds=(0.001, 0.05), method='bounded')
k_tangent = res.x

# Generate data with this k
masses = np.logspace(10, 30, 300)
l_p_sq = (hbar * G / c**3)
A_vals = 16 * np.pi * G**2 * masses**2 / c**4
A_norm = A_vals / np.max(A_vals)
tau_max = -np.log(1 - 0.999) / k_tangent
scaled_tau = A_norm * tau_max

entropy_vals = entropy_tau(k_tangent, scaled_tau)
S_BH_vals = A_vals / (4 * l_p_sq)
S_BH_norm = S_BH_vals / np.max(S_BH_vals)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(scaled_tau, entropy_vals, label=f"Saturation Model (k = {k_tangent:.5f})", color='orange')
plt.plot(scaled_tau, S_BH_norm, label="Normalized Bekenstein-Hawking Entropy", linestyle='--', color='blue')
plt.xlabel("τ (rescaled via A ∝ M²)")
plt.ylabel("Entropy (normalized)")
plt.title("Tangent Test: Where Structural & Surface Entropies Align")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Best-fit tangent decay constant: k ≈ {k_tangent:.6f}")
