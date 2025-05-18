
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Physical constants
a = 7.5657e-16  # radiation constant [J/m³/K⁴]
R_star = 12000  # star radius [m]
M_sun = 1.9885e30  # solar mass [kg]
c = 299792458  # speed of light [m/s]

# Collapse shell volume (outer 10% of star)
r_outer = R_star
r_inner = 0.9 * R_star
shell_volume = (4/3) * np.pi * (r_outer**3 - r_inner**3)

# Parameter grid
kappa_vals = np.linspace(100, 1500, 100)
T_vals = np.logspace(11, 13, 100)
energy_matrix = np.zeros((len(kappa_vals), len(T_vals)))

# Compute energy at each (kappa, T)
for i, kappa in enumerate(kappa_vals):
    for j, T in enumerate(T_vals):
        T_used = min(T, 1e13)  # Use T directly, clip if needed
        u = a * T_used**4      # energy density
        energy_matrix[i, j] = u * shell_volume / 1e-7  # Convert to erg

# ✅ Confirm energy range
print("Energy min (erg):", np.min(energy_matrix))
print("Energy max (erg):", np.max(energy_matrix))

# Plot energy map with contours and detection lines
plt.figure(figsize=(10, 6))
contourf_plot = plt.contourf(
    T_vals, kappa_vals, energy_matrix,
    levels=np.logspace(48, 54, 40, base=10),
    cmap="inferno",
    norm=mcolors.LogNorm(vmin=1e48, vmax=1e54)
)

# Add white isocontours
contour_lines = plt.contour(
    T_vals, kappa_vals, energy_matrix,
    levels=[1e49, 1e50, 1e51, 1e52, 1e53],
    colors='white', linewidths=0.8
)
plt.clabel(contour_lines, fmt="%.0e", inline=True, fontsize=8)

# Overlay neutrino detection thresholds
thresholds = [5e50, 1e51]
colors = ['cyan', 'lime']
labels = ['Hyper-Kamiokande', 'IceCube']

for threshold, color, label in zip(thresholds, colors, labels):
    cs = plt.contour(
        T_vals, kappa_vals, energy_matrix,
        levels=[threshold],
        colors=color,
        linewidths=1.5
    )
    if len(cs.allsegs[0]) > 0:
        plt.clabel(cs, fmt={threshold: label}, inline=True, fontsize=9)

# Final plot setup
plt.xscale("log")
plt.colorbar(contourf_plot, label="Energy Released (erg)")
plt.xlabel("Peak Temperature T (K)")
plt.ylabel("Bruno Constant κ")
plt.title("Bruno Collapse Flash Energies with Neutrino Detection Thresholds")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("D:\Entropy-Collapse-Research\Entropy Notebook\BRUNO_GRCHOMBO_SIMULATION\bruno_flash_map_fixed.png", dpi=300)
plt.show()
