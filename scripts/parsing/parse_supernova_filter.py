import os
import json
import pandas as pd
from pathlib import Path
from astropy.coordinates import Angle
import astropy.units as u

def parse_ra_dec(ra_str, dec_str):
    try:
        ra_deg = Angle(ra_str, unit=u.hourangle).degree
        dec_deg = Angle(dec_str, unit=u.deg).degree
        return ra_deg, dec_deg
    except Exception:
        return None, None

def parse_single_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    root = list(data.keys())[0]
    sn = data[root]

    ra = sn.get("ra", [{}])[0].get("value")
    dec = sn.get("dec", [{}])[0].get("value")
    ra_deg, dec_deg = parse_ra_dec(ra, dec) if ra and dec else (None, None)

    return {
        "name": sn.get("name", root),
        "ra_deg": ra_deg,
        "dec_deg": dec_deg,
        "redshift": sn.get("redshift", [{}])[0].get("value") if "redshift" in sn else None,
        "lumdist_mpc": sn.get("lumdist", [{}])[0].get("value") if "lumdist" in sn else None,
        "type": sn.get("claimedtype", [{}])[0].get("value") if "claimedtype" in sn else None,
        "discover_date": sn.get("discoverdate", [{}])[0].get("value") if "discoverdate" in sn else None
    }

def crawl_and_parse(root_folder, output_csv):
    records = []
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".json"):
                try:
                    record = parse_single_file(Path(dirpath) / filename)
                    records.append(record)
                except Exception as e:
                    print(f"Failed to parse {filename}: {e}")
    df = pd.DataFrame(records)
    df.to_csv(output_csv, index=False)
    print(f"Parsed {len(df)} supernovae into {output_csv}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python parse_supernova_folders.py <input_folder> <output_csv>")
    else:
        crawl_and_parse(sys.argv[1], sys.argv[2])
