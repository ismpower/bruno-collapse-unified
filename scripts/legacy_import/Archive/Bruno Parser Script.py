import os
import json
import pandas as pd
from pathlib import Path
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.cosmology import Planck18 as cosmo

# === CONFIG ===
json_root = Path("D:/DATASET DOWNLOAD/sne-2020-2024-main")
output_csv = Path("D:/Bruno_Entropy_Project/data/raw/asassn_extracted_bruno_ready.csv")
default_energy_erg = 1e51

# === Storage ===
records = []

# === Loop Through All JSON Files ===
for file in json_root.rglob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        event = list(data.values())[0]  # Top-level dict key (e.g., ASASSN-20ao)

        name = event.get("name", file.stem)
        ra_raw = event.get("ra", [{}])[0].get("value")
        dec_raw = event.get("dec", [{}])[0].get("value")
        z = event.get("redshift", [{}])[0].get("value")
        dist_mpc = event.get("lumdist", [{}])[0].get("value")
        disc_date = event.get("discoverdate", [{}])[0].get("value")
        max_date = event.get("maxdate", [{}])[0].get("value")
        type_ = event.get("claimedtype", [{}])[0].get("value", "Unknown")

        # Pick earliest date
        event_date = disc_date or max_date or None

        # RA/Dec conversion
        coord = SkyCoord(ra_raw, dec_raw, unit=(u.hourangle, u.deg))
        ra_deg = coord.ra.deg
        dec_deg = coord.dec.deg

        # Distance
        if dist_mpc:
            d_mpc = float(dist_mpc)
        elif z:
            d_mpc = cosmo.luminosity_distance(float(z)).value
        else:
            d_mpc = None

        # Fluence: E / (4π D²)
        fluence = None
        if d_mpc:
            d_m = d_mpc * 3.0857e22  # Mpc → meters
            fluence = default_energy_erg / (4 * 3.1416 * d_m**2)  # in J/m²

        # Record row
        records.append({
            "Name": name,
            "RA (deg)": round(ra_deg, 6),
            "Dec (deg)": round(dec_deg, 6),
            "Discovery Date": event_date,
            "Distance (Mpc)": round(d_mpc, 3) if d_mpc else None,
            "Redshift": float(z) if z else None,
            "Claimed Type": type_,
            "Fluence (J/m²)": round(fluence, 6) if fluence else None,
            "Source File": file.name
        })

    except Exception as e:
        print(f"⚠️ Skipped {file.name}: {e}")

# === Save Output ===
df = pd.DataFrame(records)
df.to_csv(output_csv, index=False)
print(f"✅ Parsed {len(df)} events → saved to: {output_csv}")
