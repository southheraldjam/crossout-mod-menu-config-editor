#!/usr/bin/env python3
"""
Entry point / bootstrap for Crossout Mod Menu Config Editor.

This tool does not modify the game client directly - it reads and writes
the local configuration profiles used by the mod menu overlay (module
toggles, hotkey bindings, overlay layout) and validates them before they
are loaded by the injector at game launch.
"""
import sys

from crossout_menu_editor.app_bootstrap import launch_application


def main() -> int:
    return launch_application(sys.argv[1:])


if __name__ == "__main__":
    sys.exit(main())