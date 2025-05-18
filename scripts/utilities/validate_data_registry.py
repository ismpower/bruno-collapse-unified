import os
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
REGISTRY_DIR = os.path.join(PROJECT_ROOT, 'data', 'registry')
RAW_DIR = os.path.join(PROJECT_ROOT, 'data', 'raw')

def print_header(file_path, df):
    print(f"\n📄 File: {os.path.basename(file_path)}")
    print(f"  ✅ Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    print(f"  🧩 Head:\n{df.head(2)}")
    print(f"  🧬 Dtypes: {df.dtypes.to_dict()}")
    missing = df.isnull().sum().sum()
    if missing > 0:
        print(f"  ⚠️ Missing values: {missing}")

def try_read_csv(filepath, **kwargs):
    try:
        return pd.read_csv(filepath, **kwargs)
    except Exception as e:
        print(f"  ❌ ERROR reading {os.path.basename(filepath)}: {e}")
        return None

def read_and_audit_file(filepath):
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()

    if ext not in ['.dat', '.txt']:
        print(f"  ⚠️ Skipped: {filename} (unsupported file type)")
        return

    if ext == '.dat':
        df = try_read_csv(filepath, sep=r'\s+', header=None, comment="#")
        if df is not None:
            print(f"\n📄 DAT File: {filename}")
            print(f"  ✅ Rows: {df.shape[0]} | Columns: {df.shape[1]}")
            print(f"  🧩 Head:\n{df.head(2)}")
            print(f"  🧬 Dtypes: {df.dtypes.to_dict()}")
    else:
        # For .txt files — attempt to split manually if 1 col
        df = try_read_csv(filepath, sep=r'\s+', header=None, comment="#")
        if df is not None:
            if df.shape[1] == 1:
                try:
                    df = df[0].str.split(expand=True)
                    print("  🔧 Auto-split 1 col →", df.shape[1], "columns")
                except Exception as e:
                    print(f"  ❌ Auto-split failed: {e}")
            print_header(filepath, df)

def audit_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    for root, _, files in os.walk(folder_path):
        for file in sorted(files):
            file_path = os.path.join(root, file)
            read_and_audit_file(file_path)

if __name__ == '__main__':
    print("🚀 Starting Data Integrity Audit...\n")
    audit_folder(REGISTRY_DIR)
    audit_folder(RAW_DIR)
    print("\n✅ Audit complete.")
    
