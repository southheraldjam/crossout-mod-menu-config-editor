"""Unit tests for ConfigEngine load/save round-tripping."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from crossout_menu_editor.engine.config_engine import ConfigEngine
from crossout_menu_editor.models.profile_model import ProfileModel