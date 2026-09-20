"""
Schema validation for mod menu profile files, preventing the editor from
saving configurations that the overlay injector would reject at runtime.
"""
from typing import Any, Dict

REQUIRED_TOP_LEVEL_KEYS = ("profile_name", "module_toggles", "hotkeys", "overlay_layout")


class ValidationService:
    def validate_profile_schema(self, data: Dict[str, Any]) -> None:
        missing = [key for key in REQUIRED_TOP_LEVEL_KEYS if key not in data]
        if missing:
            raise ValueError(f"Profile is missing required keys: {missing}")

        if not isinstance(data["module_toggles"], list):
            raise ValueError("module_toggles must be a list")

        for entry in data["module_toggles"]:
            if "module_id" not in entry or "enabled" not in entry:
                raise ValueError(f"Malformed module toggle entry: {entry}")

        if not isinstance(data["hotkeys"], dict):
            raise ValueError("hotkeys must be a mapping of action -> key combo")

        if not isinstance(data["overlay_layout"], dict):
            raise ValueError("overlay_layout must be a mapping")