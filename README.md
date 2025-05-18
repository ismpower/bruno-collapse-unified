# Bruno Collapse Unified

A unified, end-to-end codebase and data archive for modeling and analyzing entropy-driven gravitational collapse and its multimessenger signatures (neutrinos, supernovae, GRBs).

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/ismpower/bruno-collapse-unified.git
cd bruno-collapse-unified

# (Optional) Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install bruno_core in editable mode
pip install -e .

#📁 Repository Structure

.
├── bruno_core/           # Core Python package (algorithms, utils, logging)
├── scripts/              # Standalone scripts: collapse models, parsers, matching, simulations
├── data/
│   ├── exports/          # Final processed outputs
│   │   ├── crossmatch/   #   ├── csv/  ├── schema/
│   │   ├── diagnostics/  #   └── images/
│   │   └── final/        #       ├── csv/  └── schema/
│   ├── raw/              # Original downloaded datasets (GRB, SN, IceCube, etc.)
│   └── registry/         # Central CSV registries + YAML schemas
├── notebooks/            # Jupyter analyses and examples
│   ├── analysis/
│   ├── simulation/
│   ├── visualization/
│   ├── examples/
│   └── legacy/
├── figures/              # Publication and diagnostic figures / media
│   ├── final/            # Paper-grade PNGs
│   ├── analysis/         # Exploration-grade plots
│   └── assets/           # Animations, videos
├── report/               # Paper source and assets
│   ├── latex/            # LaTeX source & figure includes
│   ├── markdown/         # Drafts & overviews (MD)
│   └── assets/           # Images/PDFs for the manuscript
├── results/              # Computed result tables & plots
│   ├── data/             # CSV, JSON, NPZ outputs
│   ├── plots/            # Result figures (PNG/PDF)
│   └── logs/             # Run logs, summaries
├── docs/                 # Developer/user documentation
│   ├── exports/          # Export folder structure guide
│   ├── pipeline/         # Data pipeline overview
│   ├── analysis/         # IceCube & highlighted-events reports
│   ├── registry/         # Dataset & schema documentation
│   └── dupe_history/     # Archived duplicate-scan logs
├── requirements.txt      # Python dependencies
└── LICENSE               # MIT License

#📦 Installing & Using bruno_core

from bruno_core import (
    integrate_fluence,
    compute_fluence_curve,
    compute_threshold_crossings,
    find_first_crossing,
    log_event,
    load_config,
    resolve_path,
    unit_convert,
    entropy_field_model,
    temperature_from_entropy,
    compare_model_to_data
)

# Example: integrate a flux time series
times = [0.0, 1.0, 2.0, 3.0]
flux  = [1e-5, 2e-5, 1.5e-5, 1e-5]
fluence = integrate_fluence(times, flux)
print(f"Total fluence: {fluence:.3e} J/m²")
