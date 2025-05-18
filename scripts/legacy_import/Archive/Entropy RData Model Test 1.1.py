# Compare original decay model vs. saturation model
# Figure 38

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

# === Load entropy data from CSV ===
tau_data = []
entropy_data = []
with open("D:/entropy-research-library/entropy-hypothesis/scr/entropy_water_vapor.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header
    for row in reader:
        tau_data.append(float(row[0]))
        entropy_data.append(float(row[1]))

tau_data = np.array(tau_data)
entropy_data = np.array(entropy_data)

# === Original decay model ===
def entropy_decay_model(tau, S0, k):
    return (np.sqrt(S0) - (k * tau) / 2)**2

# === Saturation model ===
def entropy_saturation_model(tau, S_inf, k):
    return S_inf * (1 - np.exp(-k * tau))

# === Fit decay model with bounds ===
decay_bounds = ([0, 0], [np.inf, np.inf])
decay_guess = [1.0, 0.1]
decay_params, _ = curve_fit(entropy_decay_model, tau_data, entropy_data, p0=decay_guess, bounds=decay_bounds)
S0_fit, k_decay = decay_params

# === Fit saturation model ===
saturation_guess = [2.0, 0.005]
saturation_bounds = ([0, 0], [np.inf, np.inf])
saturation_params, _ = curve_fit(entropy_saturation_model, tau_data, entropy_data, p0=saturation_guess, bounds=saturation_bounds)
S_inf_fit, k_saturation = saturation_params

# === Generate predictions ===
decay_pred = entropy_decay_model(tau_data, S0_fit, k_decay)
saturation_pred = entropy_saturation_model(tau_data, S_inf_fit, k_saturation)

# === Plot ===
plt.plot(tau_data, entropy_data, 'ro-', label='Measured Data')
plt.plot(tau_data, decay_pred, 'b--', label='Decay Model Fit')
plt.plot(tau_data, saturation_pred, 'g--', label='Saturation Model Fit')
plt.xlabel('τ (structural iteration)')
plt.ylabel('Entropy')
plt.title('Entropy: Original vs. Saturation Model Fit')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Output ===
print(f"Decay model: S0 = {S0_fit:.4f}, k = {k_decay:.6f}")
print(f"Saturation model: S_inf = {S_inf_fit:.4f}, k = {k_saturation:.6f}")
