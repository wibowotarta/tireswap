# === Stage 22: История изменений ===
# Project: TireSwap
from datetime import datetime


class TireKitChange:
    def __init__(self, field, old_value, new_value, changed_at):
        self.field = field
        self.old_value = old_value
        self.new_value = new_value
        self.changed_at = changed_at

    def __repr__(self):
        return (
            f"TireKitChange(field={self.field!r}, old={self.old_value!r}, "
            f"new={self.new_value!r}, changed_at={self.changed_at!r})"
        )


class TireKitHistory:
    def __init__(self):
        self._changes = []

    def add(self, field, old_value, new_value, changed_at=None):
        if changed_at is None:
            changed_at = datetime.now().isoformat()
        self._changes.append(TireKitChange(field, old_value, new_value, changed_at))
        return self._changes[-1]

    def get(self, index):
        return self._changes[index]

    def __len__(self):
        return len(self._changes)

    def __iter__(self):
        return iter(self._changes)

    def __repr__(self):
        return f"TireKitHistory(changes={self._changes!r})"
