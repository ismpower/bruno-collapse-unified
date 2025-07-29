import numpy as np
import matplotlib.pyplot as plt

# Define temperature range (-0.5K to 10K)
T = np.linspace(-0.5, 10, 500)

# Standard entropy model: Linear with temperature (for reference)
def entropy_standard(T):
    return np.where(T > 0, 1e-22 * T, 0)

# Hypothetical entropy model incorporating Bose-Einstein condensate behavior
# Assuming a sharp transition at Tc = 0.5K
T_critical = 0.5
entropy_bec = np.where(T > T_critical, 1e-22 * T, np.exp(-20 * (T - T_critical)) * 1e-22)

# Plot results
plt.figure(figsize=(8,5))
plt.plot(T, entropy_standard(T), 'b-', label='Standard Model (S ∝ T)')
plt.plot(T, entropy_bec, 'r--', label='Bose-Einstein Condensate Model')
plt.axvline(T_critical, color='k', linestyle='dotted', label=f'BEC Transition ({T_critical}K)')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("Entropy Behavior Near Bose-Einstein Condensate Transition")
plt.legend()
plt.grid()
plt.show()
