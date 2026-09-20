"""
Handles the "module toggles" section of the mod menu config - i.e. which
overlay features (radar, part highlighter, damage readout, etc.) are
enabled for the current profile.
"""
from crossout_menu_editor.models.profile_model import ProfileModel
from crossout_menu_editor.models.module_toggle import ModuleToggle
from crossout_menu_editor.utils.logger import get_logger

log = get_logger(__name__)

KNOWN_MODULES = (
    "radar_overlay",
    "part_highlighter",
    "damage_readout",
    "loadout_quickswitch",
    "fps_counter",
)


class MenuSettingsHandler:
    def __init__(self, profile: ProfileModel):
        self.profile = profile

    def sync_module_toggles(self) -> None:
        """Ensure every known module has a toggle entry, defaulting to off."""
        existing = {t.module_id for t in self.profile.module_toggles}
        for module_id in KNOWN_MODULES:
            if module_id not in existing:
                self.profile.module_toggles.append(ModuleToggle(module_id, enabled=False))
                log.debug("Added missing toggle for module '%s'", module_id)

    def set_module_state(self, module_id: str, enabled: bool) -> None:
        for toggle in self.profile.module_toggles:
            if toggle.module_id == module_id:
                toggle.enabled = enabled
                log.info("Module '%s' set to %s", module_id, enabled)
                return
        raise KeyError(f"Unknown module id: {module_id}")

    def enabled_modules(self):
        return [t.module_id for t in self.profile.module_toggles if t.enabled]