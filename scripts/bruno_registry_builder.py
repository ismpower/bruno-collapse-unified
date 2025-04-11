from pathlib import Path

# Set up the file save directory
base_dir = Path("/mnt/data")
script_dir = base_dir / "scripts"
script_dir.mkdir(parents=True, exist_ok=True)

import pandas as pd
from pathlib import Path

def build_bruno_registry(input_path, output_path, threshold=1e-5):
    df = pd.read_csv(input_path)
    if "Fluence (J/m²)" not in df.columns:
        raise ValueError("Missing 'Fluence (J/m²)' column")
    
    bruno_positive = df[df["Fluence (J/m²)"] >= threshold]
    bruno_positive.to_csv(output_path, index=False)
    print(f"✅ Saved {len(bruno_positive)} Bruno-positive events to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python bruno_registry_builder.py <input.csv> <output.csv>")
    else:
        build_bruno_registry(Path(sys.argv[1]), Path(sys.argv[2]))