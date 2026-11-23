# === Stage 15: Быстрые фильтры ===
# Project: TireSwap
from datetime import date, timedelta


def today_filter(records):
    return [r for r in records if _is_today(r["date"])]


def this_week_filter(records):
    today = date.today()
    return [
        r
        for r in records
        if today - timedelta(days=7) <= _parse_date(r["date"]) <= today
    ]


def overdue_filter(records):
    return [r for r in records if r.get("due") and _parse_date(r["due"]) <= date.today()]


def _parse_date(value):
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value)[:10])


def _is_today(value):
    return _parse_date(value) == date.today()
