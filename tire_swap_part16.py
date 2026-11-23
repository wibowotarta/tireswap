# === Stage 16: Поиск дубликатов ===
# Project: TireSwap
from typing import Dict, Iterable, List, Tuple


def normalize_value(value: str) -> str:
    text = value.strip().lower()
    return "".join(char for char in text if char.isalnum())


def normalize_size(size: str) -> str:
    normalized = normalize_value(size)
    return normalized.replace("r16", "r16").replace("r17", "r17")


def normalize_season(season: str) -> str:
    normalized = normalize_value(season)
    mapping = {
        "лето": "summer",
        "summer": "summer",
        "зима": "winter",
        "winter": "winter",
        "весна": "spring",
        "spring": "spring",
        "осень": "autumn",
        "autumn": "autumn",
    }
    return mapping.get(normalized, normalized)


def normalize_mileage(mileage: str) -> int:
    digits = "".join(char for char in str(mileage) if char.isdigit())
    return int(digits) if digits else 0


def build_signature(set_name: str, size: str, season: str, mileage: str) -> str:
    return "|".join([
        normalize_value(set_name),
        normalize_size(size),
        normalize_season(season),
        str(normalize_mileage(mileage)),
    ])


def find_duplicate_sets(
    sets: Iterable[Dict[str, str]],
    min_mileage_gap: int = 0,
) -> List[Tuple[str, str]]:
    normalized: Dict[str, Tuple[str, str, str, int]] = {}
    for entry in sets:
        name = entry.get("name", "")
        size = entry.get("size", "")
        season = entry.get("season", "")
        mileage = entry.get("mileage", "")
        if not name or not size or not season:
            continue
        signature = build_signature(name, size, season, mileage)
        parts = signature.split("|")
        normalized[signature] = (
            normalize_value(name),
            normalize_size(size),
            normalize_season(season),
            normalize_mileage(mileage),
        )

    duplicates: List[Tuple[str, str]] = []
    entries = list(normalized.items())
    for index, first in enumerate(entries):
        first_name, first_size, first_season, first_mileage = first[1]
        for later in entries[index + 1:]:
            later_name, later_size, later_season, later_mileage = later[1]
            if (
                first_size != later_size
                or first_season != later_season
                or abs(first_mileage - later_mileage) > max(min_mileage_gap, 1)
            ):
                continue
            duplicates.append((first_name, later_name))
    return duplicates
