import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
from pathlib import Path

# --- Configurable inputs ---
GRB_PATH = "data/raw/fermi_swift_grb_catalog.csv"
ICECUBE_PATH = "data/raw/IceCube_Gold_Bronze_Events.csv"
OUTPUT_PATH = "data/exports/grb_icecube_crossmatch.csv"


# Match parameters
ANGULAR_TOLERANCE = 1.0 * u.deg  # can try 0.5 deg for tighter match
TIME_WINDOW = 86400  # ±1 day in seconds

def load_events():
    print("🔭 Loading datasets...")

    # Load GRB data
    grb = pd.read_csv("data/raw/fermi_swift_grb_catalog.csv")

    # Load IceCube data (corrected)
    ic = pd.read_csv("data/raw/IceCube_Gold_Bronze_Events.csv")

    # Rename for consistency
    ic.rename(columns={
        "RA [deg]": "ra",
        "Dec [deg]": "dec",
        "Date": "date",
        "Time UT": "time",
        "Energy": "energy",
        "Signalness": "signalness",
        "FAR [#/yr]": "far"
    }, inplace=True)

    # Combine date + time into single datetime
    ic["event_time"] = pd.to_datetime(
    ic["date"] + " " + ic["time"],
    format="%y/%m/%d %H:%M:%S.%f",  # Example: 21/06/08 03:41:00.97
    errors="coerce"
)
    print("❓Missing event_time rows:", ic["event_time"].isna().sum())


    # Drop bad rows
    ic = ic.dropna(subset=["ra", "dec", "event_time"])

    return grb, ic





def run_crossmatch(grb, ic):
    results = []
    grb["RA"] = pd.to_numeric(grb["RA"], errors="coerce")
    grb["Dec"] = pd.to_numeric(grb["Dec"], errors="coerce")
    ic["ra"] = pd.to_numeric(ic["ra"], errors="coerce")
    ic["dec"] = pd.to_numeric(ic["dec"], errors="coerce")


    grb_coords = SkyCoord(ra=grb["RA"].values * u.deg, dec=grb["Dec"].values * u.deg)
    ic_coords = SkyCoord(ra=ic["ra"].values * u.deg, dec=ic["dec"].values * u.deg)

    for i, (g_row, g_coord) in enumerate(zip(grb.itertuples(), grb_coords)):
        time_g = float(g_row.Trigger_Time)
        sep = g_coord.separation(ic_coords)
        close = sep < ANGULAR_TOLERANCE

        for j in ic[close].itertuples():
            time_diff = abs(float(j.event_time) - time_g)
            if time_diff <= TIME_WINDOW:
                results.append({
                    "GRB_ID": g_row.id if 'id' in grb.columns else i,
                    "GRB_RA": g_coord.ra.deg,
                    "GRB_Dec": g_coord.dec.deg,
                    "GRB_Time": time_g,
                    "Neutrino_ID": j.Index,
                    "Neutrino_RA": j.ra,
                    "Neutrino_Dec": j.dec,
                    "Neutrino_Time": j.event_time,
                    "Sep_Deg": g_coord.separation(SkyCoord(j.ra*u.deg, j.dec*u.deg)).deg,
                    "Δt_sec": time_diff
                })

    return pd.DataFrame(results)


if __name__ == "__main__":
    print("🔭 Loading datasets...")
    grb_df, ic_df = load_events()
    print(f"✓ GRBs: {len(grb_df)} | IceCube events: {len(ic_df)}")

    print("🔁 Running spatial-temporal crossmatch...")
    matched = run_crossmatch(grb_df, ic_df)
    print(f"✅ Matches found: {len(matched)}")

    Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    matched.to_csv(OUTPUT_PATH, index=False)
    print(f"📁 Results saved to: {OUTPUT_PATH}")

