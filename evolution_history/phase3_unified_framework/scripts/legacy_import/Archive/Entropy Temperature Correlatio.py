import numpy as np
import matplotlib.pyplot as plt

# Define constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)

# Temperature range from 270K (room temperature) to near 0K (hypothetical absolute zero in current model)
temperatures = np.linspace(270, 0.1, 100)  # Avoiding exactly 0K to prevent division errors

# Entropy relation using statistical mechanics (S = k_B * ln(Ω))
# We assume Ω (number of microstates) follows an empirical relationship with temperature
# Here, we model Ω as a function where lower temperature leads to an exponential entropy drop
entropy_values = k_B * np.log(1 + np.exp(-temperatures / 10))  # Approximation based on statistical mechanics principles

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(temperatures, entropy_values, label='Entropy vs Temperature', color='blue')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("Entropy as a Function of Temperature (270K to 0K)")
plt.legend()
plt.grid(True)
plt.show()
