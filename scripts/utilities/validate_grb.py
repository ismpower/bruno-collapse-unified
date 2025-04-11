import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from bruno_core.registry_logger import validate_schema


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_grb.py <csv_path> <schema_path>")
        sys.exit(1)

    csv_path = sys.argv[1]
    schema_path = sys.argv[2]

    print(f"🔍 Validating: {csv_path} against {schema_path}")
    validate_schema(csv_path, schema_path)
    print("✅ Validation complete. No schema mismatches found.")