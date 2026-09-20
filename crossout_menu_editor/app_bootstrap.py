"""
Application bootstrap. Wires together the engine, handlers, and services
before handing control to the (Tk-based) editor window.
"""
import argparse
import sys

from crossout_menu_editor.engine.config_engine import ConfigEngine
from crossout_menu_editor.engine.profile_loader import ProfileLoader
from crossout_menu_editor.handlers.menu_settings_handler import MenuSettingsHandler
from crossout_menu_editor.handlers.hotkey_handler import HotkeyHandler
from crossout_menu_editor.handlers.overlay_handler import OverlayHandler
from crossout_menu_editor.utils.logger import get_logger

log = get_logger(__name__)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="crossout-mod-menu-config-editor",
        description="Edit and validate Crossout mod menu config profiles.",
    )
    parser.add_argument(
        "--profile",
        default="default_profile.json",
        help="Name of the profile file under config/ to load on startup.",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run validation only, without opening the editor window.",
    )
    return parser


def launch_application(argv) -> int:
    args = build_arg_parser().parse_args(argv)
    log.info("Booting %s", "headless validator" if args.headless else "editor window")

    engine = ConfigEngine()
    loader = ProfileLoader(engine)
    profile = loader.load(args.profile)

    menu_handler = MenuSettingsHandler(profile)
    hotkey_handler = HotkeyHandler(profile)
    overlay_handler = OverlayHandler(profile)

    menu_handler.sync_module_toggles()
    hotkey_handler.validate_bindings()
    overlay_handler.apply_layout_defaults()

    if args.headless:
        log.info("Headless validation complete for profile '%s'", args.profile)
        return 0

    try:
        from crossout_menu_editor.ui.editor_window import EditorWindow
    except ImportError:
        log.error("UI module not available in this build; falling back to headless mode.")
        return 0

    window = EditorWindow(profile, menu_handler, hotkey_handler, overlay_handler)
    window.run()
    return 0