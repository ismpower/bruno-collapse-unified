from pathlib import Path

# Set up the file save directory
base_dir = Path("/mnt/data")
script_dir = base_dir / "scripts"
script_dir.mkdir(parents=True, exist_ok=True)

import pandas as pd
from pathlib import Path

def integrate_flux_timecurve(file_path):
    df = pd.read_csv(file_path)
    if "Time" not in df.columns or "Flux" not in df.columns:
        raise ValueError("CSV must contain 'Time' and 'Flux' columns")

    df["Integrated_Fluence"] = df["Flux"].cumsum() * (df["Time"].diff().fillna(0))
    print(df[["Time", "Integrated_Fluence"]].tail())

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python nakazato_flux_integrator.py <flux_file.csv>")
    else:
        integrate_flux_timecurve(Path(sys.argv[1]))