# === Stage 25: Недельный отчёт ===
# Project: TireSwap
def build_weekly_report(kits, swaps):
    """Return a weekly report as a string table for kits and swaps."""
    headers = ("Kit", "Size", "Season", "Mileage", "Swaps")
    rows = []
    for kit in kits:
        count = sum(1 for s in swaps if s["kit_id"] == kit["id"])
        rows.append((kit["name"], kit["size"], kit["season"], kit["mileage"], count))
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    def fmt(cells):
        return "  ".join(str(c).ljust(widths[i]) for i, c in enumerate(cells))
    lines = [fmt(headers)]
    lines.append("  ".join("-" * w for w in widths))
    for row in rows:
        lines.append(fmt(row))
    return "\n".join(lines)
