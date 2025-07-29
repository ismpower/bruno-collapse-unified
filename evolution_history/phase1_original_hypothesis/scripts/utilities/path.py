# scripts/utils/paths.py
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
REGISTRY_DIR = DATA_DIR / "registry"
EXPORT_DIR = DATA_DIR / "exports"


### from utils.paths import RAW_DIR, REGISTRY_DIR ###
