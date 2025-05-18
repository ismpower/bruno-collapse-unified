import numpy as np
import h5py

# Load GW170817 LIGO H1 data (download from https://losc.ligo.org/events/GW170817/)
filename = "D:\Entropy-Collapse-Research\Entropy Notebook\BRUNO_GRCHOMBO_SIMULATION\L-L1_LOSC_CLN_4_V1-1187007040-2048.hdf5"
with h5py.File(filename, "r") as f:
    strain_data = f["strain"]["Strain"][:]

# Constants
sample_rate = 4096
total_duration = 4096  # seconds
gps_start = 1187007040  # Start time of this segment

# Known merger time
merger_time = 1187008882.4

# Time array and selection window (±1 sec)
time_array = np.linspace(0, total_duration, len(strain_data))
abs_time_array = gps_start + time_array
mask = (abs_time_array >= merger_time - 1) & (abs_time_array <= merger_time + 1)

# Extract 2-second window
strain_segment = strain_data[mask]
time_segment = abs_time_array[mask] - merger_time  # time relative to merger = 0

# Save to .npz for upload
np.savez("gw170817_strain_segment.npz", time=time_segment, strain=strain_segment)
print("✅ Saved: gw170817_strain_segment.npz (2-second GW170817 LIGO strain slice)")
