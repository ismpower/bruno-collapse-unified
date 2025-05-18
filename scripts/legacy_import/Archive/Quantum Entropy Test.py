import numpy as np
import matplotlib.pyplot as plt

# Temperature range (-0.2K to 1K) to focus on near-zero effects
T = np.linspace(-0.2, 1, 500)

# Standard entropy model (linear relation with T above 0K, clamped to 0 below 0K)
def entropy_standard(T):
    return np.where(T > 0, 1e-15 * T, 0)

# Quantum corrected entropy (hypothesis: anomalous behavior at near-zero temperatures)
def entropy_quantum(T):
    return np.where(T > 0, np.exp(-10 * T) * 1e-15, np.exp(10 * T) * 1e-15)

# Plot results
plt.figure(figsize=(8,5))
plt.plot(T, entropy_standard(T), 'b-', label='Standard Model (S ∝ T)')
plt.plot(T, entropy_quantum(T), 'r--', label='Quantum Corrected Entropy')
plt.axvline(0, color='k', linestyle='dotted', label='0K Boundary')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("Testing Entropy Behavior Near 0K: Real Effect or Artifact?")
plt.legend()
plt.grid()
plt.show()
