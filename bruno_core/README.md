# bruno\_core

`bruno_core` is the foundational Python package for the Bruno Collapse Unified project. It centralizes key algorithms, utilities, and data handling routines used across simulations, analyses, and paper generation.

## Installation

Install in editable mode from the project root:

```bash
git clone <repo-url>
cd bruno-collapse-unified
pip install -e .
```

## Quickstart

Import and call core routines:

```python
from bruno_core.fluence_engine import integrate_fluence
from bruno_core.bruno_threshold import compute_threshold_crossings
from bruno_core.registry_logger import log_event
from bruno_core.utils import load_config

# example: integrate a flux time series
times, flux = [...], [...]
fluence = integrate_fluence(times, flux)
```

## Package Structure

```
bruno_core/
├── __init__.py         # package initializer, version info
├── fluence_engine.py   # functions for numerical fluence integration
├── bruno_threshold.py  # entropy‐threshold and collapse logic
├── registry_logger.py  # standardized event logging into CSV registries
└── utils.py            # helper routines (config, filepaths, conversions)
```

### Module Overviews

#### `fluence_engine.py`

* `integrate_fluence(times: np.ndarray, flux: np.ndarray) -> float`
* `compute_fluence_curve(times, flux, resolution) -> pd.DataFrame`

#### `bruno_threshold.py`

* `compute_threshold_crossings(entropy_series: pd.Series, threshold: float) -> List[int]`

#### `registry_logger.py`

* `log_event(event: Dict[str, Any], csv_path: str) -> None`

#### `utils.py`

* `load_config(path: str) -> Dict[str, Any]`
* `resolve_path(*parts: str) -> str`
* `unit_convert(value: float, from_unit: str, to_unit: str) -> float`

## Contributing

* **Docstrings & Type Hints**: All functions should include Google‐style docstrings and annotations.
* **Tests**: Add unit tests under `tests/bruno_core/` for new functions.

## License

MIT © Bruno Project Team
