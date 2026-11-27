# === Stage 24: Общая сводка ===
# Project: TireSwap
from collections import Counter


def summarize_sets(sets):
    """Return a summary over all tire sets.

    The result is a tuple with the total number of sets, a Counter of
    sizes and the most recent three swap records for the whole fleet.
    """
    total = len(sets)
    by_size = Counter(set["size"] for set in sets)
    recent = sorted(
        (swap for set in sets for swap in set["swaps"]),
        key=lambda record: record["date"],
        reverse=True,
    )[:3]
    return total, by_size, recent
