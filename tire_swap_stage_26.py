# === Stage 26: Месячный отчёт ===
# Project: TireSwap
from datetime import datetime


def build_month_label(year: int, month: int) -> str:
    return datetime(year, month, 1).strftime("%Y-%m")


def summarize_set(set_name: str, mileage: float) -> dict:
    return {"set": set_name, "mileage": mileage}


def compare_with_previous(
    current: dict,
    previous: dict,
) -> dict:
    delta = current["mileage"] - previous["mileage"]
    if previous["mileage"] > 0:
        pct = (delta / previous["mileage"]) * 100
    else:
        pct = 0.0 if delta == 0 else float("inf")
    return {
        "mileage": current["mileage"],
        "delta": delta,
        "pct": round(pct, 2),
    }


def generate_month_report(records: list, year: int, month: int) -> dict:
    month_key = build_month_label(year, month)
    total_mileage = 0.0
    count = 0
    for record in records:
        if record["month"] == month_key:
            total_mileage += record["mileage"]
            count += 1
    return {
        "month": month_key,
        "records": count,
        "total_mileage": round(total_mileage, 2),
    }


def previous_month(year: int, month: int) -> tuple:
    if month == 1:
        return year - 1, 12
    return year, month - 1


def previous_month_label(year: int, month: int) -> str:
    py, pm = previous_month(year, month)
    return build_month_label(py, pm)


def report_with_comparison(records: list, year: int, month: int) -> dict:
    current = generate_month_report(records, year, month)
    py, pm = previous_month(year, month)
    previous = generate_month_report(records, py, pm)
    current_key = current["month"]
    previous_key = previous["month"]
    comparison = {}
    if current["records"] > 0 and previous["records"] > 0:
        for record in records:
            if record["month"] == current_key:
                current_entry = summarize_set(record["set"], record["mileage"])
                previous_entry = summarize_set(record["set"], record["mileage"])
                comparison[current_entry["set"]] = compare_with_previous(
                    current_entry, previous_entry
                )
    return {
        "current": current,
        "previous": previous,
        "comparison": comparison,
    }
