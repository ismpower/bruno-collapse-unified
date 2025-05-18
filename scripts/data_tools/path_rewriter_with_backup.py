
import os
import json
import re
import shutil

def load_manifest(manifest_path):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def rewrite_paths_in_file(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = content
    for old_path, new_path in replacements.items():
        updated = re.sub(re.escape(old_path), new_path, updated)

    if updated != content:
        # Create a backup
        backup_path = file_path + ".bak"
        shutil.copy(file_path, backup_path)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Patched and backed up: {file_path} → {backup_path}")

def collect_replacements(manifest):
    replacements = {}
    if 'snapshots' in manifest:
        for entry in manifest['snapshots']:
            original = entry.get('original_path', entry['file'])
            new = entry['file']
            replacements[original] = new
    return replacements

def patch_repository_files(base_dir, replacements):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(('.ipynb', '.py', '.json', '.txt')):
                file_path = os.path.join(root, file)
                rewrite_paths_in_file(file_path, replacements)

if __name__ == "__main__":
    manifest_path = "scripts/utilities/registry/notebook_data_manifest.json"
    repo_root = "."  # Change this path if running from elsewhere

    manifest = load_manifest(manifest_path)
    replacements = collect_replacements(manifest)
    patch_repository_files(repo_root, replacements)
