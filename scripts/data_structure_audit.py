from pathlib import Path

# Set up the file save directory
base_dir = Path("/mnt/data")
script_dir = base_dir / "scripts"
script_dir.mkdir(parents=True, exist_ok=True)

import pandas as pd
from pathlib import Path

def audit_file(filepath):
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        return f"❌ Failed to read {filepath.name}: {e}"

    report = [f"📁 {filepath.name}"]
    report.append(f"Columns: {df.columns.tolist()}")
    report.append(f"Nulls (%):\\n{(df.isnull().mean() * 100).round(2)}")
    report.append(f"Dtypes:\\n{df.dtypes}")
    return "\\n".join(report)

def audit_directory(directory):
    directory = Path(directory)
    for file in directory.glob("*.csv"):
        print(audit_file(file))
        print("-" * 50)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        audit_directory(sys.argv[1])
    else:
        print("Usage: python data_structure_audit.py <directory>")
