
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# Load the 3D entropy field
field = np.load("snap_entropy_field.npy")

# Create a directory to store individual frames (if needed)
os.makedirs("frames", exist_ok=True)

# Setup the figure
fig, ax = plt.subplots()
cax = ax.imshow(field[:, :, 0], cmap='plasma', vmin=0, vmax=1)
fig.colorbar(cax)
ax.set_title("Entropy Collapse - Z Slice Animation")

# Update function
def update(frame):
    ax.clear()
    slice_ = field[:, :, frame]
    cax = ax.imshow(slice_, cmap='plasma', vmin=0, vmax=1)
    ax.set_title(f"Entropy Collapse - Z={frame}")
    return cax,

# Animate through Z-slices
ani = animation.FuncAnimation(fig, update, frames=field.shape[2], blit=False)

# Save as MP4
ani.save("entropy_collapse_animation.mp4", writer="ffmpeg", fps=5)

print("✅ Animation saved as entropy_collapse_animation.mp4")
