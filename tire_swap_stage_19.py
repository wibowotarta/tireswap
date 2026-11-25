# === Stage 19: Избранное ===
# Project: TireSwap
from typing import Dict, List, Set, Tuple


class FavoriteSet:
    """Tracks favorite kits by their identifier."""

    def __init__(self) -> None:
        self._favorites: Set[str] = set()

    def add_favorite(self, kit_id: str) -> None:
        """Mark a kit as favorite."""
        self._favorites.add(kit_id)

    def remove_favorite(self, kit_id: str) -> None:
        """Unmark a kit as favorite."""
        self._favorites.discard(kit_id)

    def is_favorite(self, kit_id: str) -> bool:
        """Check whether a given kit is marked as favorite."""
        return kit_id in self._favorites

    def favorites(self) -> List[str]:
        """Return the list of favorite kit identifiers."""
        return sorted(self._favorites)

    def __len__(self) -> int:
        return len(self._favorites)

    def __contains__(self, kit_id: str) -> bool:
        return kit_id in self._favorites


def load_favorites(storage: Dict[str, str]) -> FavoriteSet:
    """Build a FavoriteSet from a persistence dictionary."""
    favorites = FavoriteSet()
    for kit_id in storage:
        favorites.add_favorite(kit_id)
    return favorites


def save_favorites(favorites: FavoriteSet) -> Dict[str, str]:
    """Serialize a FavoriteSet into a persistence dictionary."""
    return {kit_id: "" for kit_id in favorites.favorites()}
