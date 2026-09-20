"""
ProfileModel is the in-memory representation of a single mod menu config
profile: its module toggles, hotkey bindings, and overlay layout.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, List

from crossout_menu_editor.models.module_toggle import ModuleToggle


@dataclass
class ProfileModel:
    profile_name: str
    module_toggles: List[ModuleToggle] = field(default_factory=list)
    hotkeys: Dict[str, str] = field(default_factory=dict)
    overlay_layout: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProfileModel":
        toggles = [ModuleToggle(**entry) for entry in data.get("module_toggles", [])]
        return cls(
            profile_name=data["profile_name"],
            module_toggles=toggles,
            hotkeys=dict(data.get("hotkeys", {})),
            overlay_layout=dict(data.get("overlay_layout", {})),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "profile_name": self.profile_name,
            "module_toggles": [t.to_dict() for t in self.module_toggles],
            "hotkeys": self.hotkeys,
            "overlay_layout": self.overlay_layout,
        }