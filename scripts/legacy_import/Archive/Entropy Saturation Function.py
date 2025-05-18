# Figure 53

import numpy as np
import matplotlib.pyplot as plt

# Entropy saturation function
def entropy_saturation(tau, k=0.1, S_inf=1.0):
    return S_inf * (1 - np.exp(-k * tau))

# Define τ (structural parameter) over a smaller scale to model microscopic behavior
tau_vals = np.linspace(0, 50, 200)  # very short scale evolution
k_values = [0.5, 0.25, 0.1, 0.05, 0.01]  # high k to model low-temperature/small-system lock-in

# Plot setup
plt.figure(figsize=(10, 5))
for k in k_values:
    S_vals = entropy_saturation(tau_vals, k=k)
    plt.plot(tau_vals, S_vals, label=f'k = {k}')

# Highlight superconductivity analogy
plt.axhline(y=0.999, color='gray', linestyle='--', label='Entropy Horizon (99.9%)')
plt.title("Entropy Saturation at Microscopic Scale (Supraconductivity Analogy)")
plt.xlabel("τ (quantized lattice evolution steps)")
plt.ylabel("Entropy (normalized)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
