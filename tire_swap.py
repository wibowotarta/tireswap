# === Stage 1: Каркас модуля ===
# Project: TireSwap
from dataclasses import dataclass, field
from typing import List


@dataclass
class TireKit:
    name: str
    size: str
    season: str
    mileage: int


def create_demo_records() -> List[TireKit]:
    return [
        TireKit(name="Summer", size="205/55 R16", season="summer", mileage=25000),
        TireKit(name="Winter", size="195/65 R15", season="winter", mileage=31000),
        TireKit(name="AllSeason", size="215/45 R17", season="all-season", mileage=18500),
    ]


def main() -> None:
    kits = create_demo_records()
    for kit in kits:
        print(f"{kit.name} | {kit.size} | {kit.season} | {kit.mileage} km")


if __name__ == "__main__":
    main()
