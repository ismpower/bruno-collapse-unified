# Second equation: Entropy behavior under extreme quantum corrections

import numpy as np
import matplotlib.pyplot as plt

# Define temperature range (-0.01K to 0.01K for extreme effects)
T = np.linspace(-0.01, 0.01, 500)

# Standard entropy model (linear relationship with T above 0K, clamped to 0 below 0K)
def entropy_standard(T):
    return np.where(T > 0, 1e-22 * T, 0)

# Quantum correction model with extreme behavior
entropy_quantum = np.exp(-1 / np.abs(T + 1e-10)) * 1e-22  # Adding small offset to prevent division by zero

# Plot results
plt.figure(figsize=(8,5))
plt.plot(T, entropy_standard(T), 'b-', label='Standard Model (S ∝ T)')
plt.plot(T, entropy_quantum, 'r--', label='Quantum Correction Model')
plt.axvline(0, color='k', linestyle='dotted', label='0K Boundary')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("Entropy Behavior Under Extreme Quantum Corrections")
plt.legend()
plt.grid()
plt.show()
