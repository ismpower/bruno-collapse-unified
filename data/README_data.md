# 📂 Data Folder Structure — Bruno Entropy Project

This directory contains all data relevant to the Bruno Engine's detection, simulation, and validation processes. Data is structured into functional subfolders for clarity and reproducibility.

---

## 🔁 `/raw/`

Contains raw input datasets:
- Neutrino simulations (`.fits`, `.dat`)
- LIGO data (`.hdf5`)
- Source catalogs (e.g., `Kato_2017`, `Yoshida_2016`)
- No processing or filtering applied

🧠 This folder preserves **original data fidelity** and should remain untouched by scripts.

---

## 📊 `/exports/`

Includes curated, processed data exports:
- Entropy tables and validated collapse results
- Tagged analysis output from Jupyter notebooks
- Intermediate `.xlsx` / `.txt` used in reports

Used for analysis and post-simulation review.

---

## 🖼️ `/figures/`

Figure-specific reference data:
- Timeline scripts
- Equation maps and figure logic
- Plot timestamp alignment models

Supports graphical representation of entropy dynamics.

---

## 📝 `/notes/`

Contains core theoretical notes:
- Bruno constant derivation
- Thermodynamic framework assumptions
- Philosophical principles behind system modeling

💡 A human-readable log of foundational insights.

---

## 📘 `/registry/`

**Home of the Bruno Engine Registry:**
- `Bruno_Engine_Registry.csv` logs entropy collapse candidates
- Future entries include SN, neutrino, and silent BH collapse detections
- All registry actions are time-tracked and reproducible

---

## 📄 Naming Guidelines

| Prefix     | Meaning                 |
|------------|-------------------------|
| `entropy_` | Thermal/collapse analysis |
| `figure_`  | Visualization resources   |
| `Tagged_`  | Auto-annotated output     |

This structure is versioned and will evolve as the Bruno Project expands.

### Datasets

- `fermi_swift_grb_catalog.csv`: Extracted GRB metadata from Fermi/Swift, used for temporal + spatial crossmatch.
- `IceCube_Gold_Bronze_Events.csv`: High-confidence neutrino event list (Gold/Bronze tier).
- `IceCube_Events_Table.csv`: Full IceCube reconstructed event list.
- `IceCube_Neutrino_Alerts.csv`: IceCube alert stream dataset.
