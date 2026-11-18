# === Stage 3: Хранилище в памяти ===
# Project: TireSwap
"""In-memory storage for tire sets in the TireSwap project."""


class TireSet:
    """A seasonal tire set with its basic attributes and mileage."""

    def __init__(self, identifier, name, size, season, mileage):
        self.identifier = identifier
        self.name = name
        self.size = size
        self.season = season
        self.mileage = mileage

    def __repr__(self):
        return (
            f"TireSet(identifier={self.identifier!r}, "
            f"name={self.name!r}, size={self.size!r}, "
            f"season={self.season!r}, mileage={self.mileage!r})"
        )


class TireSetStore:
    """A simple in-memory registry of tire sets."""

    def __init__(self):
        self._sets = {}

    def add(self, tire_set):
        """Add a tire set to the store, keyed by its identifier."""
        if not isinstance(tire_set, TireSet):
            raise TypeError("Only TireSet instances can be stored.")
        self._sets[tire_set.identifier] = tire_set
        return tire_set

    def get(self, identifier):
        """Return the tire set with the given identifier or None."""
        return self._sets.get(identifier)

    def list(self):
        """Return all stored tire sets."""
        return list(self._sets.values())
