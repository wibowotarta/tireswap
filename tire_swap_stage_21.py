# === Stage 21: Смена статуса ===
# Project: TireSwap
from enum import Enum


class KitStatus(Enum):
    WINTER = "winter"
    SUMMER = "summer"
    STORAGE = "storage"


_TRANSITIONS = {
    KitStatus.WINTER: [KitStatus.SUMMER, KitStatus.STORAGE],
    KitStatus.SUMMER: [KitStatus.WINTER, KitStatus.STORAGE],
    KitStatus.STORAGE: [KitStatus.WINTER, KitStatus.SUMMER],
}


def transition_status(current, target, reason):
    if target not in _TRANSITIONS[current]:
        raise ValueError(
            f"Invalid transition from {current.value!r} to {target.value!r}"
        )
    return {
        "current": current.value,
        "target": target.value,
        "reason": reason,
    }
