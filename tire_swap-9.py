# === Stage 9: Фильтрация записей ===
# Project: TireSwap
from datetime import datetime

SIZE_FIELD = "size"
DATE_FIELD = "date"


def filter_sets_by_size(records, size):
    """Return only the records whose 'size' field equals the given value."""
    return [record for record in records if record.get(SIZE_FIELD) == size]


def parse_date(value):
    """Convert a recorded date string into a datetime object."""
    return datetime.strptime(value, "%Y-%m-%d")


def filter_sets_by_date_range(records, start_date, end_date):
    """Return records whose date falls within [start_date, end_date]."""
    start = parse_date(start_date)
    end = parse_date(end_date)
    return [
        record for record in records
        if start <= parse_date(record.get(DATE_FIELD)) <= end
    ]


def filter_sets_by_size_and_date(records, size, start_date, end_date):
    """Return records matching a size and a date range at the same time."""
    return filter_sets_by_date_range(
        filter_sets_by_size(records, size), start_date, end_date
    )


def find_nearest_size(records, wanted_size, tolerance=0.0):
    """Return the record whose size is closest to the wanted size."""
    closest = None
    closest_distance = None
    for record in records:
        try:
            distance = abs(float(record.get(SIZE_FIELD)) - float(wanted_size))
        except (TypeError, ValueError):
            continue
        if closest_distance is None or distance < closest_distance:
            closest_distance = distance
            closest = record
    return closest
