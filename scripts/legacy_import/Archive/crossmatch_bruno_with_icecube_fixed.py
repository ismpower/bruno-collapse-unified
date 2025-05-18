import pandas as pd
from pathlib import Path
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.time import Time
from datetime import timedelta
import numpy as np
import os

# === CONFIG ===
project_root = Path("..").resolve() if "notebooks" in os.getcwd() else Path(".").resolve()
fluence_path = project_root / "data" / "raw" / "asassn_extracted_bruno_ready.csv"
icecube_path = project_root / "data" / "raw" / "Icecube_HESE.csv"
output_path = project_root / "data" / "exports" / "bruno_icecube_crossmatch.csv"

time_window_sec = 500       # ± window in seconds
angle_threshold_deg = 5.0   # max angular separation

# === Load Data ===
fluence_df = pd.read_csv(fluence_path)
icecube_df = pd.read_csv(icecube_path)

# Preprocess fluence table
fluence_df = fluence_df.dropna(subset=["Fluence (J/m²)", "RA (deg)", "Dec (deg)", "Discovery Date"])
fluence_df["Discovery Date"] = pd.to_datetime(fluence_df["Discovery Date"], errors="coerce")
fluence_df = fluence_df[fluence_df["Fluence (J/m²)"] > 1e-5]

# Convert to SkyCoord
sn_coords = SkyCoord(ra=fluence_df["RA (deg)"].astype(float).values * u.deg,
                     dec=fluence_df["Dec (deg)"].astype(float).values * u.deg)

# Parse MJD to UTC
icecube_df["Detection Time"] = Time(icecube_df["mjd"].values, format="mjd").to_datetime()
icecube_coords = SkyCoord(ra=icecube_df["ra"].astype(float).values * u.deg,
                          dec=icecube_df["dec"].astype(float).values * u.deg)

# === Match Loop ===
matches = []

for i, sn in fluence_df.iterrows():
    sn_time = sn["Discovery Date"]
    sn_coord = sn_coords[i]

    # Time match
    time_mask = (icecube_df["Detection Time"] >= sn_time - timedelta(seconds=time_window_sec)) &                 (icecube_df["Detection Time"] <= sn_time + timedelta(seconds=time_window_sec))
    nearby = icecube_df[time_mask]
    nearby_coords = icecube_coords[time_mask.values]

    if not nearby.empty:
        sep = sn_coord.separation(nearby_coords)
        for j, deg in enumerate(sep.deg):
            if deg <= angle_threshold_deg:
                row = nearby.iloc[j]
                matches.append({
                    "SN Name": sn["Name"],
                    "Discovery Date": sn_time,
                    "RA (deg)": sn["RA (deg)"],
                    "Dec (deg)": sn["Dec (deg)"],
                    "Fluence (J/m²)": sn["Fluence (J/m²)"],
                    "Neutrino Time": row["Detection Time"],
                    "IceCube ID": row["id"],
                    "Angular Separation (deg)": round(deg, 3),
                    "Energy (TeV)": row.get("energy", "N/A")
                })

# === Output Result ===
matches_df = pd.DataFrame(matches)
matches_df.to_csv(output_path, index=False)
print(f"✅ Match complete. {len(matches_df)} matches saved to: {output_path}")