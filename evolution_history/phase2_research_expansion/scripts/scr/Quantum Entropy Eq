# Investigating entropy spikes near 0K with potential physical effects
import numpy as np
import matplotlib.pyplot as plt

# Temperature range near 0K
T = np.linspace(-0.02, 0.02, 1000)

# Standard entropy model (S ∝ T, clamped to zero at 0K)
def entropy_standard(T):
    return np.where(T > 0, 1e-22 * T, 0)

# Quantum Field Contribution (modeled as an exponential divergence near 0K)
def entropy_quantum(T):
    return np.exp(-1/(T + 1e-9)) * 1e124  # Adding a small offset to avoid division issues

# Hybrid model combining both thermal and field-based effects
def entropy_hybrid(T):
    return entropy_standard(T) + entropy_quantum(T)

# Plot results
plt.figure(figsize=(8,5))
plt.plot(T, entropy_standard(T), 'b-', label='Standard Model (S ∝ T)')
plt.plot(T, entropy_quantum(T), 'r--', label='Quantum Model (Field-Based)')
plt.plot(T, entropy_hybrid(T), 'g-.', label='Hybrid Model (Thermal & Field)')
plt.axvline(0, color='k', linestyle='dotted', label='0K Boundary')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("Entropy Behavior Incorporating Quantum Effects")
plt.legend()
plt.grid()
plt.show()
