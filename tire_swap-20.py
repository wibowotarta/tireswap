# === Stage 20: Статусы записей ===
# Project: TireSwap
from enum import Enum


class KitLifecycleStatus(Enum):
    NEW = "new"
    WINTER = "winter"
    SUMMER = "summer"
    STORAGE = "storage"
    RETIRED = "retired"


LIFECYCLE_TRANSITIONS = {
    KitLifecycleStatus.NEW: {
        KitLifecycleStatus.WINTER,
        KitLifecycleStatus.SUMMER,
    },
    KitLifecycleStatus.WINTER: {
        KitLifecycleStatus.SUMMER,
        KitLifecycleStatus.STORAGE,
        KitLifecycleStatus.RETIRED,
    },
    KitLifecycleStatus.SUMMER: {
        KitLifecycleStatus.WINTER,
        KitLifecycleStatus.STORAGE,
        KitLifecycleStatus.RETIRED,
    },
    KitLifecycleStatus.STORAGE: {
        KitLifecycleStatus.WINTER,
        KitLifecycleStatus.SUMMER,
    },
    KitLifecycleStatus.RETIRED: set(),
}


def can_transition(from_status, to_status):
    return to_status in LIFECYCLE_TRANSITIONS.get(from_status, set())
