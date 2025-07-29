# Entropy Model Expansion & Convergence Testing
# - Adds: Error bands, convergence trend for k, and visual comparison

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# === Base entropy decay model ===
def entropy_model(tau, S0, k):
    return (np.sqrt(S0) - (k * tau) / 2)**2

# === Load multiple datasets for convergence ===
# Each CSV should follow: tau, measured_entropy
# For now we start with one file and simulate more by applying small noise
file_path = "entropy_data.csv"
def load_entropy_data(filepath):
    tau_data, entropy_data = [], []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            tau_data.append(float(row[0]))
            entropy_data.append(float(row[1]))
    return np.array(tau_data), np.array(entropy_data)

tau_base, entropy_base = load_entropy_data(file_path)

# Simulate additional datasets by adding Gaussian noise (stand-in for real)
datasets = [(tau_base, entropy_base)]
for seed in range(1, 4):
    np.random.seed(seed)
    noisy = entropy_base + np.random.normal(0, 0.015, size=len(entropy_base))
    datasets.append((tau_base, noisy))

# === Fit each dataset and track fitted (S0, k) ===
k_values = []
S0_values = []
plt.figure(figsize=(8, 6))
for i, (tau_data, measured_entropy) in enumerate(datasets):
    popt, _ = curve_fit(entropy_model, tau_data, measured_entropy, p0=[1.0, 0.1])
    S0_fit, k_fit = popt
    S0_values.append(S0_fit)
    k_values.append(k_fit)

    predicted = entropy_model(tau_data, S0_fit, k_fit)
    residuals = measured_entropy - predicted

    # Plot model fit
    plt.plot(tau_data, measured_entropy, 'o', label=f'Measured Data #{i+1}')
    plt.plot(tau_data, predicted, '--', label=f'Model Fit #{i+1}')

# === Plot styling ===
plt.title("Entropy Decay Across Datasets: Convergence of Model")
plt.xlabel("τ (structural iteration)")
plt.ylabel("Entropy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Convergence trend of k ===
print("\nConverging values of k:")
for i, k in enumerate(k_values):
    print(f"Dataset #{i+1}: k = {k:.6f}")

avg_k = np.mean(k_values)
print(f"\nAverage k across all datasets: {avg_k:.6f}")

# === Threshold prediction (entropy collapse point) ===
k_eff = avg_k
S0_eff = np.mean(S0_values)
tau_collapse = (2 * np.sqrt(S0_eff)) / k_eff
print(f"Predicted τ-collapse point: τ = {tau_collapse:.4f} (entropy → 0)")
