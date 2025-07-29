## 📥 ASASSN to Bruno Fluence Extraction

**Script:** `scripts/extract_asassn_to_fluence.py`

**Input:**  
Directory: `sne-2020-2024-main/`  
Format: JSON (Open Supernova Catalog schema)

**Extracted Fields:**  
- RA / Dec (converted to decimal)
- Discovery Date or Max Date
- Luminosity distance or redshift
- Fluence computed using:  
  `fluence = E / (4π D²)` with default `E = 1e51 erg`

**Output:**  
Saved to `data/raw/asassn_extracted_bruno_ready.csv`  
→ Used for Bruno visibility threshold filtering and IceCube temporal/directional match

📊 [View highlight event table](docs/bruno_highlighted_events.md)
