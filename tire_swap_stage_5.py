# === Stage 5: Удаление и восстановление ===
# Project: TireSwap
"""TireSwap — delete entity 'kit' with soft delete and restore capability."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class KitStatus(str, Enum):
    ACTIVE = "active"
    SOFT_DELETED = "soft_deleted"


@dataclass
class Kit:
    name: str
    size: str
    season: str
    mileage: int
    status: KitStatus = KitStatus.ACTIVE
    deleted_at: Optional[datetime] = field(default=None)
    deleted_by: Optional[str] = field(default=None)

    def soft_delete(self, deleted_by: str) -> None:
        """Mark the kit as removed while keeping the row for history."""
        if self.status is KitStatus.SOFT_DELETED:
            return
        self.status = KitStatus.SOFT_DELETED
        self.deleted_at = datetime.now()
        self.deleted_by = deleted_by

    def restore(self) -> None:
        """Bring a previously soft-deleted kit back to use."""
        if self.status is not KitStatus.SOFT_DELETED:
            return
        self.status = KitStatus.ACTIVE
        self.deleted_at = None
        self.deleted_by = None

    def is_available(self) -> bool:
        """Return True only for kits that are currently in use."""
        return self.status is KitStatus.ACTIVE


class KitRepository:
    """In-memory store that supports hard and soft deletion of kits."""

    def __init__(self) -> None:
        self._kits: dict[str, Kit] = {}

    def add(self, kit: Kit) -> None:
        self._kits[kit.name] = kit

    def get(self, name: str) -> Optional[Kit]:
        return self._kits.get(name)

    def hard_delete(self, name: str) -> bool:
        """Permanently remove a kit. Returns True if something was deleted."""
        return self._kits.pop(name, None) is not None

    def soft_delete(self, name: str, deleted_by: str) -> bool:
        """Soft-delete a kit, preserving it for future restore."""
        kit = self._kits.get(name)
        if kit is None:
            return False
        kit.soft_delete(deleted_by)
        return True

    def restore(self, name: str) -> bool:
        """Restore a soft-deleted kit. No-op for never-deleted kits."""
        kit = self._kits.get(name)
        if kit is None:
            return False
        kit.restore()
        return True

    def list_active(self) -> list[Kit]:
        return [kit for kit in self._kits.values() if kit.is_available()]

    def list_all(self) -> list[Kit]:
        return list(self._kits.values())
