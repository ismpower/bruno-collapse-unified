import pandas as pd
import yaml
import sys

def infer_column_type(series):
    if pd.api.types.is_integer_dtype(series):
        return "integer"
    elif pd.api.types.is_float_dtype(series):
        return "float"
    else:
        return "string"

def generate_schema(csv_path, dataset_name="Unnamed Dataset", output_path="schema.yaml"):
    df = pd.read_csv(csv_path)

    schema = {
        "dataset_name": dataset_name,
        "source": "UNSPECIFIED",
        "description": "AUTO-GENERATED SCHEMA. Fill in details.",
        "columns": [],
        "coordinate_frame": "UNSPECIFIED",
        "time_format": "UNSPECIFIED",
        "preprocessing_notes": "None"
    }

    for col in df.columns:
        col_type = infer_column_type(df[col])
        schema["columns"].append({
            "name": col,
            "description": "TBD",
            "type": col_type
        })

    with open(output_path, "w") as f:
        yaml.dump(schema, f, sort_keys=False)

    print(f"Schema saved to {output_path}")

# Example usage:
# python generate_schema.py data/raw/fermi_swift_grb_catalog.csv "Fermi + Swift GRBs"
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_schema.py <csv_path> <dataset_name>")
    else:
        csv_path = sys.argv[1]
        dataset_name = sys.argv[2]
        output = csv_path.replace(".csv", "_schema.yaml").replace("raw", "registry")
        generate_schema(csv_path, dataset_name, output)
