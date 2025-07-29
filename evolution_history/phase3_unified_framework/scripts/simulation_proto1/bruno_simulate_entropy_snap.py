
import torch
import numpy as np
import matplotlib.pyplot as plt
import os

# Setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Config
GRID_SIZE = 128
INITIAL_ENTROPY = 0.1
BRUNO_THRESHOLD = 0.001005
EXPANSION_FACTOR = 1.05
CONTRACTION_FACTOR = 0.90
OUTPUT_DIR = "/home/winnay_proto1/bruno-simulator/scripts/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize 3D entropy field
entropy_field = INITIAL_ENTROPY * torch.ones((GRID_SIZE, GRID_SIZE, GRID_SIZE), device=device)

# Simulate outer shell entropy as 'surface'
def compute_surface_entropy(field):
    surface = torch.cat([
        field[0, :, :], field[-1, :, :],
        field[:, 0, :], field[:, -1, :],
        field[:, :, 0], field[:, :, -1]
    ])
    return torch.mean(surface)

# Time loop
snap_triggered = False
entropy_history = []
surface_history = []
K_history = []
snap_step = None

for step in range(30):
    surface_entropy = compute_surface_entropy(entropy_field)
    volume_entropy = torch.mean(entropy_field)
    K = volume_entropy / surface_entropy

    # Log metrics
    entropy_history.append(volume_entropy.item())
    surface_history.append(surface_entropy.item())
    K_history.append(K.item())

    print(f"Step {step:2d} | S_vol={volume_entropy:.6f}, S_surf={surface_entropy:.6f}, K={K:.4f}")

    # Check for Bruno collapse threshold
    if not snap_triggered and K <= 1.0:
        print(f"🧨 Snap threshold reached at step {step}! Beginning collapse...")
        snap_triggered = True
        snap_step = step

    # Apply expansion or collapse
    if not snap_triggered:
        entropy_field *= EXPANSION_FACTOR
    else:
        entropy_field *= CONTRACTION_FACTOR
        entropy_field = torch.clamp(entropy_field, 0.0, 1.0)

# Save final field and plot
np.save(f"{OUTPUT_DIR}/snap_entropy_field.npy", entropy_field.cpu().numpy())

plt.plot(entropy_history, label='Volume Entropy')
plt.plot(surface_history, label='Surface Entropy')
plt.plot(K_history, label='K (Vol/Surf)')
if snap_step is not None:
    plt.axvline(snap_step, color='red', linestyle='--', label='Collapse Trigger')
plt.xlabel("Timestep")
plt.ylabel("Entropy")
plt.title("Bruno Threshold Snap Simulation")
plt.legend()
plt.grid(True)
plt.savefig(f"{OUTPUT_DIR}/entropy_snap_plot.png")
