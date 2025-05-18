import numpy as np
import matplotlib.pyplot as plt

# Define a temperature range (-1K to 10K)
T = np.linspace(-1, 10, 500)

# Standard entropy model (S ∝ T, where entropy follows classical thermodynamics)
def entropy_standard(T):
    return np.where(T > 0, 1e-22 * T, 0)

# Quantum entropy model (accounts for field-based coherence effects)
def entropy_quantum(T):
    return np.exp(-10 * T) * 1e-22

# Hybrid entropy model (bridging classical and quantum regimes)
def entropy_hybrid(T):
    return np.where(T > 0, 1e-22 * T, np.exp(-10 * T) * 1e-22)

# Plot results
plt.figure(figsize=(8,5))
plt.plot(T, entropy_standard(T), 'b-', label='Standard Model (S ∝ T)')
plt.plot(T, entropy_quantum(T), 'r--', label='Quantum Model (Field-Based)')
plt.plot(T, entropy_hybrid(T), 'g-.', label='Hybrid Model (Thermal & Field)')
plt.axvline(0, color='k', linestyle='dotted', label='0K Boundary')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("Testing Entropy Behavior Without Temperature Shifts")
plt.legend()
plt.grid()
plt.show()
