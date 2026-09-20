"""
ConfigEngine centralizes reading/writing the mod menu's JSON/INI config
files and keeps an in-memory representation used by all handlers.
"""
import json
from pathlib import Path
from typing import Any, Dict

from crossout_menu_editor.models.profile_model import ProfileModel
from crossout_menu_editor.services.file_service import FileService
from crossout_menu_editor.services.validation_service import ValidationService
from crossout_menu_editor.utils.logger import get_logger

log = get_logger(__name__)


class ConfigEngine:
    """Reads/writes profile JSON and exposes a validated in-memory model."""

    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.file_service = FileService(self.config_dir)
        self.validator = ValidationService()

    def read_raw(self, filename: str) -> Dict[str, Any]:
        raw_text = self.file_service.read_text(filename)
        try:
            return json.loads(raw_text)
        except json.JSONDecodeError as exc:
            log.error("Malformed profile '%s': %s", filename, exc)
            raise

    def load_profile(self, filename: str) -> ProfileModel:
        raw = self.read_raw(filename)
        self.validator.validate_profile_schema(raw)
        return ProfileModel.from_dict(raw)

    def save_profile(self, profile: ProfileModel, filename: str) -> None:
        self.validator.validate_profile_schema(profile.to_dict())
        payload = json.dumps(profile.to_dict(), indent=2)
        self.file_service.write_text(filename, payload)
        log.info("Saved profile '%s' with %d module toggles", filename, len(profile.module_toggles))