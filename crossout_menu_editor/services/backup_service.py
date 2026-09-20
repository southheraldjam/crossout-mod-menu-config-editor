"""
Creates timestamped snapshots of profile files before they are edited,
so users can roll back a bad mod menu configuration.
"""
import shutil
import time
from pathlib import Path

from crossout_menu_editor.utils.logger import get_logger

log = get_logger(__name__)


class BackupService:
    def __init__(self, config_dir: Path, backup_subdir: str = "_backups"):
        self.config_dir = config_dir
        self.backup_dir = config_dir / backup_subdir
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def snapshot(self, filename: str) -> Path | None:
        source = self.config_dir / filename
        if not source.exists():
            log.debug("Skipping backup, source '%s' does not exist yet.", filename)
            return None

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        target = self.backup_dir / f"{source.stem}.{timestamp}{source.suffix}"
        shutil.copy2(source, target)
        log.info("Backed up '%s' -> '%s'", filename, target.name)
        return target

    def prune_old_backups(self, keep_last: int = 10) -> None:
        backups = sorted(self.backup_dir.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)
        for stale in backups[keep_last:]:
            stale.unlink(missing_ok=True)