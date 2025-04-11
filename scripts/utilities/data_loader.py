# scripts/utilities/data_loader.py
import json
from pathlib import Path
from astropy.coordinates import SkyCoord
import astropy.units as u
import pandas as pd
from .astro_utils import hms_to_deg, redshift_to_distance, fluence_from_distance

def load_asassn_json_folder(json_folder, default_energy=1e51):
    records = []
    json_folder = Path(json_folder)

    for file in json_folder.rglob("*.json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
            event = list(data.values())[0]

            ra_raw = event.get("ra", [{}])[0].get("value")
            dec_raw = event.get("dec", [{}])[0].get("value")
            z = event.get("redshift", [{}])[0].get("value")
            dist = event.get("lumdist", [{}])[0].get("value")
            disc_date = event.get("discoverdate", [{}])[0].get("value")
            max_date = event.get("maxdate", [{}])[0].get("value")
            event_date = disc_date or max_date or None
            type_ = event.get("claimedtype", [{}])[0].get("value", "Unknown")
            name = event.get("name", file.stem)

            ra_deg, dec_deg = hms_to_deg(ra_raw, dec_raw)
            d_mpc = float(dist) if dist else redshift_to_distance(float(z)) if z else None
            fluence = fluence_from_distance(d_mpc, default_energy) if d_mpc else None

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
    return pd.DataFrame(records)
