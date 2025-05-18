#!/usr/bin/env python3
import os, json, time

root = "data"
manifest = []

for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        full = os.path.join(dirpath, fn)
        st = os.stat(full)
        manifest.append({
            "path": os.path.relpath(full, root),
            "size": st.st_size,
            "mtime": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(st.st_mtime))
        })

with open("data_manifest.json","w") as f:
    json.dump(manifest, f, indent=2)
print(f"Wrote {len(manifest)} entries to data_manifest.json")
