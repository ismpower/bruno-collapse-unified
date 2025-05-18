# Exploring Entropy Behavior at Planck-Scale Phenomena

import numpy as np
import matplotlib.pyplot as plt

# Define Planck temperature and entropy reference
T_planck = 1.416808e32  # Planck temperature in Kelvin
S_planck = 1.0  # Arbitrary normalization for entropy at Planck scale

# Define temperature range near Planck scale
T = np.linspace(0, T_planck * 1.1, 500)

# Standard entropy model (classical physics expectation)
def entropy_standard(T):
    return np.where(T > 0, S_planck * (T / T_planck), 0)

# Quantum correction model at Planck scale (hypothetical transition effect)
def entropy_quantum(T):
    return np.where(T > 0, S_planck * np.exp(-T_planck / T), 0)

# No space-time constraints model (alternative extreme physics scenario)
def entropy_no_spacetime(T):
    return np.where(T > 0, S_planck * np.log(1 + T / T_planck), 0)

# Plot results
plt.figure(figsize=(8,5))
plt.plot(T, entropy_standard(T), 'b-', label='Standard Model (S ∝ T)')
plt.plot(T, entropy_quantum(T), 'r--', label='Quantum Model (Planck Correction)')
plt.plot(T, entropy_no_spacetime(T), 'g-.', label='No Space-Time Model')
plt.axvline(T_planck, color='k', linestyle='dotted', label=f'Planck Temperature')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (Arbitrary Units)")
plt.title("Entropy Behavior at Planck-Scale Phenomena")
plt.legend()
plt.grid()
plt.show()
