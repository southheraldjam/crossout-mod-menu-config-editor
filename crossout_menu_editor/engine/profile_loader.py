"""
ProfileLoader resolves the requested profile file, falling back to the
bundled default when a user profile is missing or corrupt, and takes a
backup snapshot before any load that will be edited.
"""
from crossout_menu_editor.engine.config_engine import ConfigEngine
from crossout_menu_editor.models.profile_model import ProfileModel
from crossout_menu_editor.services.backup_service import BackupService
from crossout_menu_editor.utils.logger import get_logger

log = get_logger(__name__)

DEFAULT_PROFILE = "default_profile.json"


class ProfileLoader:
    def __init__(self, engine: ConfigEngine):
        self.engine = engine
        self.backup_service = BackupService(engine.config_dir)

    def load(self, filename: str) -> ProfileModel:
        try:
            profile = self.engine.load_profile(filename)
        except (FileNotFoundError, ValueError):
            log.warning("Profile '%s' unavailable, loading defaults instead.", filename)
            profile = self.engine.load_profile(DEFAULT_PROFILE)

        self.backup_service.snapshot(filename)
        return profile