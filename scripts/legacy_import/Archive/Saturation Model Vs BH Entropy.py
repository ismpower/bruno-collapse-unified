# Re-import necessary packages after code state reset
# Figure 49

import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11         # gravitational constant (m^3 kg^-1 s^-2)
c = 299792458           # speed of light (m/s)
hbar = 1.054571817e-34  # reduced Planck constant (J·s)
kB = 1.380649e-23       # Boltzmann constant (J/K)

# Bekenstein-Hawking entropy constant factor
S_bh_coeff = (4 * np.pi * G) / (hbar * c)

# Masses (kg) of two real black holes
black_holes = {
    "Sagittarius A* (Milky Way)": 4.3e6 * 1.989e30,  # 4.3 million solar masses
    "M87* (Messier 87)": 6.5e9 * 1.989e30            # 6.5 billion solar masses
}

# Our model's decay constant
k_model = 0.001005
S_inf = 1.0  # normalize to 1 for saturation model

# Evaluate for each BH
results = {}
tau_values = np.linspace(0, 7500, 300)

for name, M in black_holes.items():
    A = 16 * np.pi * (G * M / c**2)**2  # Horizon area
    S_bh = S_bh_coeff * A / kB          # Bekenstein-Hawking entropy (in units of k_B)
    tau = (S_bh / S_inf)                # use raw entropy as τ scale
    S_sat = S_inf * (1 - np.exp(-k_model * tau))  # entropy from saturation model

    results[name] = {
        "Mass (kg)": M,
        "Surface Area (m^2)": A,
        "Bekenstein-Hawking Entropy (S)": S_bh,
        "τ Estimate": tau,
        "Saturation Entropy": S_sat
    }

# Visualization
plt.figure(figsize=(10, 6))
for name, data in results.items():
    tau_curve = tau_values
    S_curve = S_inf * (1 - np.exp(-k_model * tau_curve))
    plt.plot(tau_curve, S_curve, label=f"{name}")

# BH entropy levels as horizontal lines
for name, data in results.items():
    plt.axhline(y=data["Saturation Entropy"], linestyle="--", label=f"{name} Saturation S ≈ {data['Saturation Entropy']:.4f}")

plt.title("Saturation Model vs Bekenstein-Hawking Entropy")
plt.xlabel("τ (Structural Steps)")
plt.ylabel("Entropy (normalized)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

results
