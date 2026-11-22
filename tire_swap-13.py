# === Stage 13: Группировка ===
# Project: TireSwap
"""TireSwap stage 13: group kits by size and count kits in each group."""


def group_kits_by_size(kits):
    """Group tire kits by their size and return the count per group.

    Args:
        kits: an iterable of kit-like items. Each item must expose a
            ``size`` attribute or ``size`` key.

    Returns:
        A dict mapping each distinct size to the number of kits having
        that size.
    """
    counts = {}
    for kit in kits:
        size = kit.size
        counts[size] = counts.get(size, 0) + 1
    return counts


def group_kits_by_size_keys(kits):
    """Group tire kits by their size using a ``size`` key access.

    Useful when kits are represented as mappings (e.g. dicts) instead of
    objects with attributes.

    Args:
        kits: an iterable of mapping-like items, each carrying a
            ``size`` key.

    Returns:
        A dict mapping each distinct size to the number of kits having
        that size.
    """
    counts = {}
    for kit in kits:
        size = kit["size"]
        counts[size] = counts.get(size, 0) + 1
    return counts


def find_largest_group(kits):
    """Return the size with the highest number of kits.

    Args:
        kits: an iterable of kit-like items, each exposing a ``size``
            attribute or ``size`` key.

    Returns:
        The size associated with the largest group. Returns ``None``
        when there are no kits to group.
    """
    counts = group_kits_by_size(kits)
    if not counts:
        return None
    return max(counts, key=counts.get)


def summarize_kits(kits):
    """Build a human-readable summary of kits grouped by size.

    Args:
        kits: an iterable of kit-like items, each exposing a ``size``
            attribute or ``size`` key.

    Returns:
        A list of strings formatted as ``"<size>: <count>"`` lines, one
        per group, sorted by descending count.
    """
    counts = group_kits_by_size(kits)
    summary = []
    for size, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        summary.append(f"{size}: {count}")
    return summary


if __name__ == "__main__":
    sample = [
        {"name": "Set A", "size": "R17", "season": "Winter", "mileage": 10000},
        {"name": "Set B", "size": "R19", "season": "Summer", "mileage": 5000},
        {"name": "Set C", "size": "R17", "season": "Winter", "mileage": 12000},
        {"name": "Set D", "size": "R19", "season": "Summer", "mileage": 8000},
        {"name": "Set E", "size": "R17", "season": "Winter", "mileage": 3000},
    ]
    print(summarize_kits(sample))
    print(find_largest_group(sample))
