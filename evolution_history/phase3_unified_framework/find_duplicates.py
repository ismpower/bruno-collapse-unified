import os
import sys
from collections import defaultdict

def list_duplicates(root):
    by_name = defaultdict(list)
    for dirpath, _, files in os.walk(root):
        for f in files:
            by_name[f].append(os.path.join(dirpath, f))
    # keep only names with more than one path
    return {name: paths for name, paths in by_name.items() if len(paths) > 1}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_duplicates.py <root_folder>")
        sys.exit(1)

    root = sys.argv[1]
    dups = list_duplicates(root)
    if not dups:
        print("No duplicate filenames found.")
    else:
        for name, paths in dups.items():
            print(f"\n== {name} ==")
            for p in paths:
                print(p)
