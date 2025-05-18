# Bruno Entropy Export Structure

This document outlines the organization of the data exports for the Bruno Collapse Unified project.

* **`crossmatch/`**: Pairwise matches between GRB/SN/Neutrino events.
* **`diagnostics/`**: Visual diagnostics — plots, sky maps, error ellipses, and other figures.
* **`entropy_tables/`**: Model output tables used for prediction, validation, and intermediate analysis.
* **`final/`**: Curated candidate events suitable for reporting and publication.
* **`schemas/`**: YAML column schemas for each CSV, used for automated validation of registry and export files.

Each directory contains two subfolders (where applicable):

```
data/exports/
├── crossmatch/
│   ├── csv/
│   └── schema/
├── diagnostics/
│   └── images/
├── entropy_tables/
│   ├── csv/
│   └── schema/
├── final/
│   ├── csv/
│   └── schema/
└── schemas/  # global or miscellaneous schemas
```

Use this structure as your guide when adding new exports or schemas to keep the repository consistent and easy to navigate.
