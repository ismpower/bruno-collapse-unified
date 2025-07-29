
import torch
import numpy as np
import matplotlib.pyplot as plt
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# --- CONFIG ---
GRID_SIZE = 128
INITIAL_ENTROPY = 0.1
BRUNO_THRESHOLD = 0.001005
EXPANSION_FACTOR = 1.05
CONTRACTION_FACTOR = 0.90
STEPS = 30
OUTPUT_DIR = "./results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- INIT ENTROPY FIELD ---
entropy_field = INITIAL_ENTROPY * torch.ones((GRID_SIZE, GRID_SIZE, GRID_SIZE), device=device)
entropy_field += 0.05 * torch.rand((GRID_SIZE, GRID_SIZE, GRID_SIZE), device=device)

# Seed collapse core
center = GRID_SIZE // 2
entropy_field[center-5:center+5, center-5:center+5, center-5:center+5] = 0.0005

# --- TIMESTAMPING ---
# Tracks when each voxel collapses (0 = not yet collapsed)
collapse_time = torch.zeros_like(entropy_field, dtype=torch.int32, device=device)

# --- SURFACE ENTROPY ---
def compute_surface_entropy(field):
    surface = torch.cat([
        field[0, :, :], field[-1, :, :],
        field[:, 0, :], field[:, -1, :],
        field[:, :, 0], field[:, :, -1]
    ])
    return torch.mean(surface)

# --- SIMULATION LOOP ---
snap_triggered = False
snap_step = None
entropy_history = []
surface_history = []
K_history = []

for step in range(STEPS):
    s_vol = torch.mean(entropy_field)
    s_surf = compute_surface_entropy(entropy_field)
    K = s_vol / s_surf

    entropy_history.append(s_vol.item())
    surface_history.append(s_surf.item())
    K_history.append(K.item())

    print(f"Step {step:2d} | S_vol={s_vol:.6f}, S_surf={s_surf:.6f}, K={K:.4f}")

    if not snap_triggered and K <= 1.0:
        print(f"🧨 Snap threshold reached at step {step}! Beginning collapse...")
        snap_triggered = True
        snap_step = step

    # Update entropy field
    if not snap_triggered:
        entropy_field *= EXPANSION_FACTOR
    else:
        entropy_field *= CONTRACTION_FACTOR
        entropy_field = torch.clamp(entropy_field, 0.0, 1.0)

        # Timestamp voxels that cross Bruno threshold
        collapsed = (collapse_time == 0) & (entropy_field < BRUNO_THRESHOLD)
        collapse_time[collapsed] = step

# --- SAVE ---
np.save(f"{OUTPUT_DIR}/timestamped_entropy_field.npy", entropy_field.cpu().numpy())
np.save(f"{OUTPUT_DIR}/collapse_time_map.npy", collapse_time.cpu().numpy())

# --- PLOT GLOBAL ENTROPY CURVE ---
plt.plot(entropy_history, label='Volume Entropy')
plt.plot(surface_history, label='Surface Entropy')
plt.plot(K_history, label='K (Vol/Surf)')
if snap_step is not None:
    plt.axvline(snap_step, color='red', linestyle='--', label='Collapse Trigger')
plt.xlabel("Timestep")
plt.ylabel("Entropy")
plt.title("Bruno Threshold Snap Simulation w/ Timestamps")
plt.legend()
plt.grid(True)
plt.savefig(f"{OUTPUT_DIR}/entropy_snap_plot_timestamped.png")
