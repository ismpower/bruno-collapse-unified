import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import log
import seaborn as sns

# Sample real superconductor entropy-like data (approximate, for test only)
# Values represent entropy (arbitrary units) at decreasing temperatures (K)
temperatures = np.array([300, 150, 77, 50, 30, 20, 10, 5, 2, 1])  # Kelvin
entropy_data = np.array([1.0, 0.8, 0.6, 0.45, 0.30, 0.22, 0.10, 0.05, 0.01, 0.005])

# Normalize entropy for fitting
entropy_data /= entropy_data[0]

# Invert temperature for structural interpretation (lower T = higher τ)
tau_data = 1 / temperatures

# Saturation model function
def entropy_saturation(tau, k):
    return 1 - np.exp(-k * tau)

# Fit the model
popt, _ = curve_fit(entropy_saturation, tau_data, entropy_data)
k_fit = popt[0]

# Generate model prediction
tau_fit = np.linspace(min(tau_data), max(tau_data), 200)
entropy_fit = entropy_saturation(tau_fit, k_fit)

# Plot
plt.figure(figsize=(10, 5))
sns.set(style="whitegrid")
plt.plot(1 / tau_data, entropy_data, 'ro', label="Measured Data")
plt.plot(1 / tau_fit, entropy_fit, 'b--', label=f"Saturation Model Fit (k = {k_fit:.4f})")
plt.xlabel("Temperature (K)")
plt.ylabel("Normalized Entropy")
plt.title("Superconductivity Entropy Saturation Fit")
plt.legend()
plt.tight_layout()
plt.gca().invert_xaxis()  # Higher temp to lower temp
plt.grid(True)

#print(df)  # or whatever your dataframe variable is

