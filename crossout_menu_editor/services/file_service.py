"""
Thin filesystem wrapper scoped to the config directory, so handlers and
the engine never build raw paths themselves.
"""
from pathlib import Path

from crossout_menu_editor.utils.path_utils import ensure_within_directory


class FileService:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _resolve(self, filename: str) -> Path:
        path = self.base_dir / filename
        ensure_within_directory(path, self.base_dir)
        return path

    def read_text(self, filename: str) -> str:
        path = self._resolve(filename)
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        return path.read_text(encoding="utf-8")

    def write_text(self, filename: str, content: str) -> None:
        path = self._resolve(filename)
        path.write_text(content, encoding="utf-8")

    def exists(self, filename: str) -> bool:
        return self._resolve(filename).exists()