
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

INPUT_FILE = "collapse_time_map.npy"
OUTPUT_FILE = "collapse_time_animation.mp4"

# Load collapse time map
collapse_time = np.load(INPUT_FILE)

# Normalize for color mapping
max_step = np.max(collapse_time)
if max_step == 0:
    max_step = 1  # prevent divide-by-zero if no collapse occurred

# Setup figure
fig, ax = plt.subplots()
cax = ax.imshow(collapse_time[:, :, 0], cmap='plasma', vmin=0, vmax=max_step)
fig.colorbar(cax)
ax.set_title("Collapse Timestamp - Z slice")

# Animation update
def update(frame):
    ax.clear()
    ax.imshow(collapse_time[:, :, frame], cmap='plasma', vmin=0, vmax=max_step)
    ax.set_title(f"Collapse Timestamp - Z={frame}")
    return ax

# Animate through Z-axis
ani = animation.FuncAnimation(fig, update, frames=collapse_time.shape[2], blit=False)

# Save animation
ani.save(OUTPUT_FILE, writer="ffmpeg", fps=5)

print(f"✅ Animation saved to {OUTPUT_FILE}")
