"""Represents a single togglable mod menu feature/module."""
from dataclasses import dataclass


@dataclass
class ModuleToggle:
    module_id: str
    enabled: bool = False

    def to_dict(self) -> dict:
        return {"module_id": self.module_id, "enabled": self.enabled}