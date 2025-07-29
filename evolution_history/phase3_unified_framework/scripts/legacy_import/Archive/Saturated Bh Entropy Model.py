# Saturated Black Hole Entropy Equation Exploration
# Alternative to Bekenstein-Hawking: bounded entropy growth
# Figure 39
import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters (naturalized or symbolic units)
A_values = np.linspace(0, 100, 200)  # Surface area range (Planck units)
S_inf = 1.0                          # Maximum entropy limit (normalized)
alpha = 0.05                         # Structural decay constant

# Saturated entropy model:
def saturated_entropy(A, S_inf, alpha):
    return S_inf * (1 - np.exp(-alpha * A))

# Classic Bekenstein-Hawking model:
def hawking_entropy(A, scale=0.01):
    return scale * A

# Compute values
S_saturated = saturated_entropy(A_values, S_inf, alpha)
S_bh = hawking_entropy(A_values)

# Plot comparison
plt.figure(figsize=(8, 5))
plt.plot(A_values, S_bh, 'b--', label='Bekenstein-Hawking (linear)')
plt.plot(A_values, S_saturated, 'g-', label='Saturation Model (proposed)')
plt.xlabel("Horizon Surface Area (A)")
plt.ylabel("Entropy (S)")
plt.title("Black Hole Entropy: Divergent vs Saturating Model")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Numerical check near origin and at large mass
print(f"S(A→0): {saturated_entropy(0.0, S_inf, alpha):.4f}")
print(f"S(A→∞): {saturated_entropy(1e6, S_inf, alpha):.4f} (should approach S_inf = {S_inf})")
