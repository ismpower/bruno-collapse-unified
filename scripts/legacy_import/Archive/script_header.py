# top of every script
from pathlib import Path
import sys

# Dynamically resolve the project root no matter where this script is run
CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[2]  # Adjust based on script depth

# Add to sys.path so you can import utils, modules, etc.
sys.path.append(str(PROJECT_ROOT))

# Define paths (standardized)
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
REGISTRY_DIR = DATA_DIR / "registry"
EXPORT_DIR = DATA_DIR / "exports"
