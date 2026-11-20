# === Stage 7: Связи между сущностями ===
# Project: TireSwap
from datetime import datetime
from typing import List, Dict, Any


class TireSet:
    def __init__(self, name: str, size: str, season: str, mileage: float):
        self.name = name
        self.size = size
        self.season = season
        self.mileage = mileage
        self.id = self._generate_id("set")

    def _generate_id(self, prefix: str) -> str:
        return f"{prefix}-{int(datetime.now().timestamp())}"

    def __repr__(self):
        return (f"TireSet(id={self.id}, name={self.name!r}, size={self.size!r}, "
                f"season={self.season!r}, mileage={self.mileage})")


class TireChange:
    def __init__(self, tire_set: TireSet, date: str, from_mileage: float,
                 to_mileage: float, service_notes: str = ""):
        self.id = self._generate_id("change")
        self.tire_set = tire_set
        self.date = date
        self.from_mileage = from_mileage
        self.to_mileage = to_mileage
        self.service_notes = service_notes

    def _generate_id(self, prefix: str) -> str:
        return f"{prefix}-{int(datetime.now().timestamp())}"

    @property
    def distance_driven(self) -> float:
        return self.to_mileage - self.from_mileage

    def __repr__(self):
        return (f"TireChange(id={self.id}, tire_set={self.tire_set.name!r}, "
                f"date={self.date!r}, distance={self.distance_driven})")


class TireSwap:
    def __init__(self):
        self.tire_sets: List[TireSet] = []
        self.changes: List[TireChange] = []

    def add_tire_set(self, tire_set: TireSet) -> None:
        self.tire_sets.append(tire_set)

    def add_change(self, change: TireChange) -> None:
        self.changes.append(change)

    def get_changes_for_tire_set(self, tire_set: TireSet) -> List[TireChange]:
        return [change for change in self.changes if change.tire_set is tire_set]

    def check_integrity(self, tire_set: TireSet) -> bool:
        if tire_set not in self.tire_sets:
            return False
        return len(self.get_changes_for_tire_set(tire_set)) >= 0


if __name__ == "__main__":
    swap = TireSwap()
    summer_set = TireSet("Summer", "205/55 R16", "summer", 10000.0)
    winter_set = TireSet("Winter", "205/55 R16", "winter", 12000.0)
    swap.add_tire_set(summer_set)
    swap.add_tire_set(winter_set)

    change1 = TireChange(summer_set, "2024-05-10", 10000.0, 15000.0, "normal")
    change2 = TireChange(winter_set, "2024-10-05", 12000.0, 13500.0, "snowy")
    swap.add_change(change1)
    swap.add_change(change2)

    print("Summer changes:", swap.get_changes_for_tire_set(summer_set))
    print("Summer integrity:", swap.check_integrity(summer_set))
    print("Unknown set integrity:", swap.check_integrity(TireSet("X", "R16", "summer", 0)))
