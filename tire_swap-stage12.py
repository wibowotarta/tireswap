# === Stage 12: Теги ===
# Project: TireSwap
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Tag:
    name: str

    def __post_init__(self):
        if not self.name:
            raise ValueError("Tag name cannot be empty")
        self.name = self.name.strip().lower()


@dataclass
class TireSet:
    name: str
    size: str
    season: str
    mileage: float
    tags: List[Tag] = field(default_factory=list)

    def add_tag(self, tag_name: str) -> "TireSet":
        tag = Tag(tag_name)
        if tag.name in self.tags:
            return self
        self.tags.append(tag)
        return self

    def remove_tag(self, tag_name: str) -> "TireSet":
        target = Tag(tag_name)
        self.tags = [t for t in self.tags if t.name != target.name]
        return self

    def has_tag(self, tag_name: str) -> bool:
        return Tag(tag_name).name in self.tags

    def tag_names(self) -> List[str]:
        return [t.name for t in self.tags]


def find_by_tag(tire_sets: List[TireSet], tag_name: str) -> List[TireSet]:
    target = Tag(tag_name).name
    return [ts for ts in tire_sets if ts.has_tag(tag_name)]


def add_tags_to_set(set_obj: TireSet, tag_names: List[str]) -> TireSet:
    for name in tag_names:
        set_obj.add_tag(name)
    return set_obj


def remove_tags_from_set(set_obj: TireSet, tag_names: List[str]) -> TireSet:
    for name in tag_names:
        set_obj.remove_tag(name)
    return set_obj


if __name__ == "__main__":
    demo = TireSet(name="All-Season Pro", size="205/55 R16", season="all-season", mileage=12000.0)
    demo.add_tag("winter")
    demo.add_tag("summer")
    demo.add_tag("winter")
    print("tags:", demo.tag_names())
    demo.remove_tag("summer")
    print("after remove:", demo.tag_names())
    print("has winter:", demo.has_tag("WINTER"))
    print(find_by_tag([demo], "winter")[0].name)
