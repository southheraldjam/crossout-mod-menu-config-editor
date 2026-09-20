"""
crossout_menu_editor
=====================
Desktop configuration editor for the Crossout mod menu overlay.

Package layout:
    engine/    - core config parsing & profile lifecycle
    handlers/  - feature-specific UI/logic handlers (hotkeys, overlay, toggles)
    services/  - file IO, backups, validation
    models/    - dataclasses describing profile/module structures
    utils/     - shared helpers (paths, logging)
"""

__version__ = "1.4.2"
__app_name__ = "Crossout Mod Menu Config Editor"