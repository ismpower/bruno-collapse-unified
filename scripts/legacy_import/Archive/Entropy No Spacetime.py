import numpy as np
import matplotlib.pyplot as plt

# Define temperature range for theoretical extrapolation
T = np.linspace(-0.01, 0.01, 500)  # Hypothetical small scale

# Standard entropy model (S ∝ T for comparison)
def entropy_standard(T):
    return np.where(T > 0, 1e-18 * T, 0)

# Quantum model with field-based entropy behavior
entropy_quantum = np.exp(-1 / (T + 1e-6)) * 1e-18  # Avoid division by zero

# Hypothetical model assuming no space-time constraints (S may not approach zero smoothly)
def entropy_no_spacetime(T):
    return np.exp(-1 / (np.abs(T) + 1e-6)) * 1e-18  # Absolute value to remove negative asymmetry

# Plot results
plt.figure(figsize=(8,5))
plt.plot(T, entropy_standard(T), 'b-', label='Standard Model (S ∝ T)')
plt.plot(T, entropy_quantum, 'r--', label='Quantum Model (Field-Based)')
plt.plot(T, entropy_no_spacetime(T), 'g-.', label='No Space-Time Model')
plt.axvline(0, color='k', linestyle='dotted', label='0K Boundary')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("Entropy Behavior Without Space-Time Constraints")
plt.legend()
plt.grid()
plt.show()
