import pandas as pd
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
from datetime import timedelta

def load_events():
    print("🔭 Loading datasets...")

    # Load GRB catalog
    grb = pd.read_csv("data/raw/fermi_swift_grb_catalog.csv")
    grb = grb.rename(columns={"RA [deg]": "RA", "Dec [deg]": "Dec"})
    grb["event_time"] = pd.to_datetime(grb["Trigger_Time"], unit="s", origin="unix")

    # Load IceCube catalog
    ic = pd.read_csv("data/raw/IceCube_Gold_Bronze_Events.csv")
    ic = ic.rename(columns={
        "RA [deg]": "ra",
        "Dec [deg]": "dec",
        "Date": "date",
        "Time UT": "time"
    })

    ic["event_time"] = pd.to_datetime(ic["date"] + " " + ic["time"], format="%y/%m/%d %H:%M:%S.%f", errors="coerce")

    print("❓ Missing event_time rows (IC):", ic["event_time"].isna().sum())

    ic = ic.dropna(subset=["ra", "dec", "event_time"])
    grb = grb.dropna(subset=["RA", "Dec", "event_time"])

    print(f"✓ GRBs: {len(grb)} | IceCube events: {len(ic)}")
    return grb, ic

def run_crossmatch(grb, ic):
    print("🔁 Running spatial-temporal crossmatch (EXTRA WIDE)...")

    max_sep_deg = 20  # WIDE
    time_window = pd.Timedelta("5 days")  # WIDE

    matched_rows = []

    for _, g in grb.iterrows():
        grb_time = g["event_time"]
        grb_coord = SkyCoord(ra=g["RA"], dec=g["Dec"], unit=(u.hourangle, u.deg))


        for _, i in ic.iterrows():
            ic_time = i["event_time"]
            ic_coord = SkyCoord(ra=i["ra"] * u.deg, dec=i["dec"] * u.deg)

            time_diff = abs(grb_time - ic_time)
            sep = grb_coord.separation(ic_coord)

            if time_diff < time_window and sep < max_sep_deg * u.deg:
                matched_rows.append({
                    "GRB_time": grb_time,
                    "GRB_RA": g["RA"],
                    "GRB_Dec": g["Dec"],
                    "IC_time": ic_time,
                    "IC_RA": i["ra"],
                    "IC_Dec": i["dec"],
                    "Time_Diff_hr": time_diff.total_seconds() / 3600,
                    "Separation_deg": sep.deg
                })

    matched = pd.DataFrame(matched_rows)
    return matched

if __name__ == "__main__":
    grb_df, ic_df = load_events()
    matches = run_crossmatch(grb_df, ic_df)

    if not matches.empty:
        print(f"✅ Matches found: {len(matches)}")
        matches.to_csv("data/exports/grb_icecube_crossmatch_wide.csv", index=False)
        print("📁 Results saved to: data/exports/grb_icecube_crossmatch_wide.csv")
        print(matches)
    else:
        print("❌ No matches found even with WIDE spectrum thresholds.")
