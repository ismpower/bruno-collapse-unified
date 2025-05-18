import numpy as np
import matplotlib.pyplot as plt

# Define temperature range including negative temperatures for hypothetical regions
T = np.linspace(-1.5, 1.5, 500)

# Standard entropy model (S ∝ T above 0K, clamped to 0 below 0K)
def entropy_standard(T):
    return np.where(T > 0, 1e-18 * T, 0)

# Quantum field-based entropy (allowing entropy to continue evolving even when T is stable)
def entropy_quantum(T):
    return 1e-18 * np.exp(-1 / (T + 1e-6))  # Prevents division by zero

# Hybrid model combining thermal entropy and quantum field effects
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
