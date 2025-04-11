import pandas as pd
import numpy as np
from pathlib import Path

def compute_fluence(df, energy_joule=1e44):
    if "lumdist_mpc" not in df.columns:
        raise ValueError("Missing 'lumdist_mpc' column in input CSV.")

    # Convert distance from Mpc to meters
    D_m = df["lumdist_mpc"].astype(float) * 3.086e22  # 1 Mpc = 3.086e22 meters

    # Avoid division by zero or NaNs
    with np.errstate(divide='ignore', invalid='ignore'):
        fluence = energy_joule / (4 * np.pi * D_m**2)
        fluence = fluence.replace([np.inf, -np.inf], np.nan)

    return fluence

def main(input_csv, output_csv, threshold=1e-5):
    df = pd.read_csv(input_csv)
    df["fluence_j_m2"] = compute_fluence(df)
    df["Bruno_Trigger"] = df["fluence_j_m2"] >= threshold

    df.to_csv(output_csv, index=False)
    print(f"✅ Fluence & trigger computed. Output: {output_csv}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python compute_fluence_trigger.py <input.csv> <output.csv>")
    else:
        main(sys.argv[1], sys.argv[2])
