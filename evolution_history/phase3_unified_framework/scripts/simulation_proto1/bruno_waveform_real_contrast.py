
# bruno_waveform_real_contrast.py

import numpy as np
import torch
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# === Load real waveform data ===
def load_waveform_csv(file_path):
    data = np.loadtxt(file_path, delimiter=',')
    # Normalize for visual mapping
    normalized = data[:, 1] ** 2  # Use square for energy-like behavior
    normalized = normalized / np.max(normalized)
    return normalized

# === Entropy evolution based on real waveform ===
def simulate_entropy_waveform(waveform, grid_size=128, bruno_K=0.001005):
    field = torch.ones((grid_size, grid_size), device=device) * 0.3
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
        field = field - 0.015 * decay_zone * (decay_zone - bruno_K)
        field = torch.clamp(field, 0.0, 1.0)

        if i % 2 == 0 or i < 10:
            frames.append(field.detach().cpu().numpy())

    return frames

# === Animate with better contrast ===
def create_contrast_animation(frames, outfile="gw_entropy_real.mp4"):
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], cmap='plasma', vmin=0.0, vmax=0.5)
    ax.set_title("Real GW Entropy Collapse")
    plt.colorbar(im, label="Entropy S")

    def update(i):
        im.set_array(frames[i])
        ax.set_title(f"Step {i}")
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=len(frames), blit=True)
    ani.save(outfile, writer="ffmpeg", fps=6)
    plt.close()
    print(f"✅ Saved: {outfile}")

# === Full pipeline ===
def run():
    waveform = load_waveform_csv("gw150914_strain.csv")  # Make sure this file is present
    frames = simulate_entropy_waveform(waveform, grid_size=256)
    create_contrast_animation(frames)

if __name__ == "__main__":
    run()
