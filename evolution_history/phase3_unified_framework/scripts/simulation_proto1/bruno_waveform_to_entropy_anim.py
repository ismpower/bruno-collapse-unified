
# bruno_waveform_to_entropy_anim.py

import numpy as np
import torch
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --- Load GW waveform data ---
# Replace this with real LIGO data CSV if available
# For now, simulate a chirp-like waveform
def generate_mock_waveform(steps):
    t = np.linspace(0, 1, steps)
    waveform = np.sin(30 * t**2) * np.exp(-4 * t)  # chirp + damping
    waveform = waveform**2
    return waveform / np.max(waveform)  # normalize

# --- Entropy field evolution based on waveform amplitude ---
def simulate_entropy_evolution(waveform, grid_size=128, bruno_K=0.001005):
    field = torch.ones((grid_size, grid_size), device=device) * 0.2
    center = grid_size // 2
    frames = []

    for i, amp in enumerate(waveform):
        radius = int(amp * grid_size // 2)
        mask = torch.zeros_like(field)
        y, x = torch.meshgrid(torch.arange(grid_size), torch.arange(grid_size), indexing='ij')
        dist = torch.sqrt((x - center)**2 + (y - center)**2)
        mask[dist < radius] = 1.0

        # Collapse zone triggered by waveform amplitude
        decay_zone = mask * field
        field = field - 0.01 * decay_zone * (decay_zone - bruno_K)
        field = torch.clamp(field, 0.0, 1.0)

        if i % 3 == 0 or i < 10:
            frames.append(field.detach().cpu().numpy())

    return frames

# --- Animate result ---
def create_entropy_animation(frames, outfile="gw_entropy_animation.mp4"):
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], cmap='inferno', vmin=0, vmax=1.0)
    ax.set_title("Entropy Collapse from GW Input")
    plt.colorbar(im)

    def update(i):
        im.set_array(frames[i])
        ax.set_title(f"Frame {i}")
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=len(frames), blit=True)
    ani.save(outfile, writer="ffmpeg", fps=5)
    plt.close()

# --- Run full process ---
waveform = generate_mock_waveform(200)
frames = simulate_entropy_evolution(waveform, grid_size=256)
create_entropy_animation(frames)
print("✅ Animation complete: gw_entropy_animation.mp4")
