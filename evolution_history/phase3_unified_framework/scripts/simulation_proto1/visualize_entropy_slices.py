
import numpy as np
import matplotlib.pyplot as plt
import os

# Config
INPUT_PATH = "/home/winnay_proto1/bruno-simulator/scripts/results/snap_entropy_field.npy"
OUTPUT_DIR = "/home/winnay_proto1/bruno-simulator/scripts/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load field
field = np.load(INPUT_PATH)
z_mid = field.shape[2] // 2
y_mid = field.shape[1] // 2
x_mid = field.shape[0] // 2

# XY slice (Z fixed)
plt.imshow(field[:, :, z_mid], cmap='inferno')
plt.colorbar(label='Entropy')
plt.title('XY Slice (Z mid)')
plt.savefig(f"{OUTPUT_DIR}/slice_xy.png")
plt.clf()

# XZ slice (Y fixed)
plt.imshow(field[:, y_mid, :], cmap='inferno')
plt.colorbar(label='Entropy')
plt.title('XZ Slice (Y mid)')
plt.savefig(f"{OUTPUT_DIR}/slice_xz.png")
plt.clf()

# YZ slice (X fixed)
plt.imshow(field[x_mid, :, :], cmap='inferno')
plt.colorbar(label='Entropy')
plt.title('YZ Slice (X mid)')
plt.savefig(f"{OUTPUT_DIR}/slice_yz.png")
plt.clf()

print("✅ Slices saved to:", OUTPUT_DIR)
