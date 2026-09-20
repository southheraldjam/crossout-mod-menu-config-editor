"""
Validates and normalizes hotkey bindings stored in a profile (e.g. the
key used to toggle the overlay menu in-game).
"""
import re

from crossout_menu_editor.models.profile_model import ProfileModel
from crossout_menu_editor.utils.logger import get_logger

log = get_logger(__name__)

_VALID_KEY_PATTERN = re.compile(r"^(Ctrl\+|Alt\+|Shift\+)*[A-Z0-9F]{1,3}$")

RESERVED_KEYS = {"ESC", "ENTER", "TAB"}


class HotkeyHandler:
    def __init__(self, profile: ProfileModel):
        self.profile = profile

    def validate_bindings(self) -> None:
        for action, combo in self.profile.hotkeys.items():
            normalized = combo.strip().upper().replace(" ", "")
            if not _VALID_KEY_PATTERN.match(normalized):
                log.warning("Invalid hotkey '%s' for action '%s', resetting.", combo, action)
                normalized = "F1"
            if normalized in RESERVED_KEYS:
                log.warning("Hotkey '%s' is reserved, resetting action '%s'.", normalized, action)
                normalized = "F1"
            self.profile.hotkeys[action] = normalized

    def rebind(self, action: str, combo: str) -> None:
        self.profile.hotkeys[action] = combo
        self.validate_bindings()