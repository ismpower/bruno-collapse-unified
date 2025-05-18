# Real-Data vs. Model: Entropy Decay Comparison
# Requires: entropy_data.csv (tau, measured_entropy)
# Figure 36
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- Model Equation (analytical decay) ---
def entropy_model(tau, S0, k):
    return (np.sqrt(S0) - (k * tau) / 2)**2

# --- Load real measurement data from CSV ---
data_file = "D:/entropy-research-library/entropy-hypothesis/scr/entropy_water_vapor.csv"
tau_data = []
measured_entropy = []

with open(data_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header
    for row in reader:
        tau_data.append(float(row[0]))
        measured_entropy.append(float(row[1]))

tau_data = np.array(tau_data)
measured_entropy = np.array(measured_entropy)

# --- Fit model to real data ---
initial_guess = [1.0, 0.1]  # S0, k
tuned_params, covariance = curve_fit(entropy_model, tau_data, measured_entropy, p0=initial_guess)
S0_fit, k_fit = tuned_params

print(f"Fitted parameters: S0 = {S0_fit:.4f}, k = {k_fit:.4f}")

# --- Generate predictions ---
predicted_entropy = entropy_model(tau_data, S0_fit, k_fit)

# --- Plot ---
plt.plot(tau_data, measured_entropy, 'ro-', label='Measured Data')
plt.plot(tau_data, predicted_entropy, 'b--', label='Model Fit')
plt.xlabel('τ (structural iteration)')
plt.ylabel('Entropy')
plt.title('Entropy Decay: Real Data vs. Model Prediction')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Residual Analysis ---
residuals = measured_entropy - predicted_entropy
print("\nResiduals at each τ:")
for i in range(len(tau_data)):
    print(f"τ = {tau_data[i]:.1f} | Δ = {residuals[i]:+.5f}")
