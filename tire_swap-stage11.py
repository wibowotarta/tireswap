# === Stage 11: Поиск по нескольким словам ===
# Project: TireSwap
"""TireSwap stage 11: multi-word kit search with '-' exclusion prefixes.

A self-contained module that parses a query like
    "winter sport 205/55 -summer"
into a structured search request, splitting on whitespace, treating tokens
starting with '-' as exclusions, and keeping the rest as required words.
"""

from __future__ import annotations


class KitSearchRequest:
    """Structured result of parsing a search query.

    Attributes:
        required: lower-cased words that must appear in a kit.
        excluded: lower-cased words that must not appear in a kit.
    """

    def __init__(self, required: list[str], excluded: list[str]) -> None:
        self.required = required
        self.excluded = excluded

    def matches(self, kit_name: str) -> bool:
        """Return True if kit_name contains every required word and none of
        the excluded words (case-insensitive, whitespace-split)."""
        tokens = set(kit_name.lower().split())
        if not self.required:
            return not self.excluded
        if any(word not in tokens for word in self.required):
            return False
        return not any(word in tokens for word in self.excluded)

    def __repr__(self) -> str:
        return (
            f"KitSearchRequest(required={self.required!r}, "
            f"excluded={self.excluded!r})"
        )


def parse_query(query: str) -> KitSearchRequest:
    """Split a query string into required and excluded words.

    Tokens starting with '-' are treated as exclusions; the remaining
    whitespace-separated tokens are required words. Empty tokens are ignored.
    """
    query = query.strip()
    if not query:
        return KitSearchRequest([], [])

    required: list[str] = []
    excluded: list[str] = []

    for token in query.split():
        word = token[1:] if token.startswith("-") else token
        required.append(word.lower()) if token.startswith("-") is False else excluded.append(word.lower())

    return KitSearchRequest(required=required, excluded=excluded)


def search_kits(kits: list[str], query: str) -> list[tuple[str, int]]:
    """Return matching kit names with their match score.

    The score counts how many required words appear in the kit name. Kits are
    returned sorted by descending score, then alphabetically by name.
    """
    request = parse_query(query)
    if not request.required and not request.excluded:
        return [(name, 0) for name in kits]

    results: list[tuple[str, int]] = []
    for name in kits:
        tokens = set(name.lower().split())
        if not request.matches(name):
            continue
        score = sum(1 for word in request.required if word in tokens)
        results.append((name, score))

    results.sort(key=lambda item: (-item[1], item[0]))
    return results
