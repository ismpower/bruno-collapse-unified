# Entropy vs Scale Factor (a): Entropy Saturation Across Expansion
# Figure 52

import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 0.001  # decay constant (cosmological scale)
S_inf = 1.0  # normalized max entropy

# Define scale factor a (from early universe to today)
a_vals = np.linspace(0.01, 1.0, 200)  # 0.01 to 1.0 (normalized)

# Assume a logarithmic relation between scale factor and structural time tau:
tau_vals = np.log(a_vals / a_vals[0]) / np.log(a_vals[-1] / a_vals[0]) * (1 / k)

# Saturation entropy model: S(tau) = S_inf * (1 - exp(-k * tau))
S_vals = S_inf * (1 - np.exp(-k * tau_vals))

# Plot
plt.figure(figsize=(10, 5))
plt.plot(a_vals, S_vals, color='darkgreen', label='Entropy Saturation (k=0.001)')
plt.axhline(0.999, linestyle='--', color='gray', label='Entropy Horizon (99.9%)')
plt.xlabel("Scale Factor a(t) (normalized)")
plt.ylabel("Entropy (normalized)")
plt.title("Entropy Growth vs Cosmic Expansion")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
