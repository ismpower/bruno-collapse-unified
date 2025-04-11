# 📘 Bruno Engine Registry

This folder stores the **Bruno_Engine_Registry.csv** — the official, timestamped record of all thermodynamic entropy collapse candidates detected or simulated under the Bruno model.

---

## 🧠 Purpose

The registry serves as the **cumulative memory** of the Bruno Engine:

- Logs events that cross the Bruno fluence threshold (1e-5 J/m²)
- Tracks neutrino detections, simulated fluence curves, and SN events
- Preserves back-calculated collapse times, detection parameters, and source metadata

---

## 📄 Registry Format

| Field                      | Description                                                |
|---------------------------|------------------------------------------------------------|
| Event Name                | Name or identifier (e.g., IceCube ID, SN name)             |
| Detection Date (UTC)      | When neutrino or observation occurred                      |
| Source Galaxy             | Likely host of the collapse                                |
| RA / Dec (J2000)          | Sky coordinates                                            |
| Distance (Mpc)            | Distance to source in megaparsecs                         |
| Explosion Energy (erg)    | Estimated release energy used in fluence model             |
| Bruno Trigger Time (s)    | Time after collapse when Bruno threshold was crossed       |
| Collapse Time (UTC)       | Back-computed collapse moment (if applicable)              |
| Fluence at Earth (J/m²)   | Calculated entropy fluence                                 |
| Bruno Threshold Crossed   | `True` or `False`                                          |
| Neutrino Detected         | `True` or `False`, plus details if known                   |
| Neutrino Energy (TeV)     | Detected energy (if applicable)                            |
| Positional Match Confidence | High / Moderate / Simulated                              |
| Notes                     | Any relevant context, links to simulations or source files |

---

## 📝 Usage

New events should be appended programmatically or manually **only after full verification**, including:

- Fluence simulation using `bruno_core/fluence_engine.py`
- Bruno crossing time determination
- Optional correlation with IceCube, LIGO, or other detectors

---

## 🔐 Registry Integrity

This registry is version-controlled. Any additions must preserve timestamped integrity.  
Think of it as the **official logbook of the entropy universe**.

---

## 🧪 Future

This format will eventually support:

- Automatic entries via the Bruno Engine pipeline
- Registry indexing by SN type, distance, or confidence
- Publishing of confirmed entropy collapses for public databases

