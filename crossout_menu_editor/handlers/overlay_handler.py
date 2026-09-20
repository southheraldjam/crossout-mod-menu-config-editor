"""
Manages overlay window layout defaults: anchor position, opacity, and
scale of the mod menu HUD panel drawn over the Crossout client.
"""
from crossout_menu_editor.models.profile_model import ProfileModel
from crossout_menu_editor.utils.logger import get_logger

log = get_logger(__name__)

DEFAULT_LAYOUT = {
    "anchor": "top-left",
    "opacity": 0.85,
    "scale": 1.0,
}


class OverlayHandler:
    def __init__(self, profile: ProfileModel):
        self.profile = profile

    def apply_layout_defaults(self) -> None:
        for key, value in DEFAULT_LAYOUT.items():
            self.profile.overlay_layout.setdefault(key, value)

    def set_opacity(self, value: float) -> None:
        clamped = max(0.1, min(1.0, value))
        self.profile.overlay_layout["opacity"] = clamped
        log.info("Overlay opacity set to %.2f", clamped)

    def set_anchor(self, anchor: str) -> None:
        valid_anchors = {"top-left", "top-right", "bottom-left", "bottom-right", "center"}
        if anchor not in valid_anchors:
            raise ValueError(f"Unsupported anchor '{anchor}'")
        self.profile.overlay_layout["anchor"] = anchor