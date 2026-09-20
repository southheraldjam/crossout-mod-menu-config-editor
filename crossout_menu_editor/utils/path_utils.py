"""Filesystem safety helpers to keep config IO scoped to expected dirs."""
from pathlib import Path


def ensure_within_directory(path: Path, base_dir: Path) -> None:
    """Raise if `path` would resolve outside of `base_dir` (defends
    against filenames like '..\\..\\something' leaking outside config/)."""
    resolved_path = path.resolve()
    resolved_base = base_dir.resolve()
    if resolved_base not in resolved_path.parents and resolved_path != resolved_base:
        raise ValueError(f"Refusing to access path outside of {base_dir}: {path}")