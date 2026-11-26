# === Stage 23: Просмотр истории ===
# Project: TireSwap
from datetime import datetime


def format_set_history(set_id, mileage, storage_days, last_change):
    """Return a compact one-line history record for a set."""
    return (
        f"set #{set_id} | {mileage} km | "
        f"stored {storage_days} days | last change {last_change}"
    )


def parse_date(value):
    """Parse a date string in ISO format (YYYY-MM-DD)."""
    return datetime.strptime(value, "%Y-%m-%d").date()


def build_set_history(set_id, mileage, storage_days, last_change):
    """Build a compact history view for a single set record."""
    return format_set_history(set_id, mileage, storage_days, last_change)


if __name__ == "__main__":
    print(
        build_set_history(
            set_id=42,
            mileage=15000,
            storage_days=85,
            last_change="2024-01-15",
        )
    )
