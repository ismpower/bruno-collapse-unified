from pathlib import Path

# Set up the file save directory
base_dir = Path("/mnt/data")
script_dir = base_dir / "scripts"
script_dir.mkdir(parents=True, exist_ok=True)

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_sky_map(csv_path):
    df = pd.read_csv(csv_path)
    if "RA" not in df.columns or "Dec" not in df.columns or "Fluence (J/m²)" not in df.columns:
        raise ValueError("CSV must include 'RA', 'Dec', 'Fluence (J/m²)'")

    is_positive = df["Fluence (J/m²)"] >= 1e-5
    plt.figure(figsize=(10, 5))
    plt.scatter(df["RA"], df["Dec"], c=is_positive.map({True: 'red', False: 'blue'}), alpha=0.6, label='SNe')
    plt.xlabel("Right Ascension (deg)")
    plt.ylabel("Declination (deg)")
    plt.title("Bruno Sky Map (Red = Bruno-positive)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python plot_bruno_sky_map.py <supernovae.csv>")
    else:
        plot_sky_map(Path(sys.argv[1]))


