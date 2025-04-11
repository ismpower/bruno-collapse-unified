import pandas as pd
import yaml

def validate_schema(csv_path, schema_path):
    df = pd.read_csv(csv_path)
    with open(schema_path) as f:
        schema = yaml.safe_load(f)

    columns = [col["name"] for col in schema["columns"]]
    missing = set(columns) - set(df.columns)
    
    if missing:
        print("❌ Missing columns:", missing)
    else:
        print("✅ Schema validation passed!")

    ...
validate_schema("data/raw/fermi_swift_grb_catalog.csv",
                "data/registry/fermi_swift_grb_catalog_schema.yaml")
