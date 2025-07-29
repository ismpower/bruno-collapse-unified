# Entropy Horizon Function Tester
# Goal: Express tau_horizon as a function of k
# Figure 42

import numpy as np
import matplotlib.pyplot as plt

# Horizon threshold
S_inf = 1.0
S_target = 0.999 * S_inf

# Inverted saturation equation:
#   S(tau) = S_inf * (1 - exp(-k * tau))
#   Solve for tau: tau = -ln(1 - S_target / S_inf) / k

def tau_horizon(k, S_target=S_target, S_inf=S_inf):
    if k <= 0 or S_target >= S_inf:
        return np.nan
    return -np.log(1 - S_target / S_inf) / k

# Test over a range of k values
k_values = np.linspace(0.001, 0.1, 100)
tau_values = [tau_horizon(k) for k in k_values]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(k_values, tau_values, 'purple')
plt.xlabel("Decay Constant (k)")
plt.ylabel("Predicted Entropy Horizon (τ)")
plt.title("Entropy Horizon τ as Function of Decay Constant k")
plt.grid(True)
plt.tight_layout()
plt.show()

# Print a reference point
example_k = 0.015
print(f"For k = {example_k}, predicted τ_horizon = {tau_horizon(example_k):.2f}")
