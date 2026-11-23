# === Stage 18: Массовое обновление ===
# Project: TireSwap
def preview_changes(kits, field, new_values):
    if field not in ("season", "mileage"):
        raise ValueError("Unsupported field for bulk update")
    updates = []
    for kit in kits:
        if kit[field] not in new_values:
            continue
        updates.append({
            "name": kit["name"],
            "old": kit[field],
            "new": new_values[kit[field]],
        })
    return updates


def apply_bulk_update(kits, field, new_values):
    for kit in kits:
        if kit[field] in new_values:
            kit[field] = new_values[kit[field]]
    return len(kits)


def bulk_update_menu():
    print("Bulk update selected kits")
    print("1. Season")
    print("2. Mileage")
    choice = input("Field to update: ")
    if choice not in ("1", "2"):
        print("Invalid choice")
        return False
    field = "season" if choice == "1" else "mileage"
    allowed = {"1": ["winter", "summer", "all-season"], "2": ["0", "1", "2", "3"]}
    mapping = {"1": {"winter": 0, "summer": 1, "all-season": 2},
               "2": {"0": 0, "1": 1, "2": 2, "3": 3}}
    print("Available values")
    for i, value in enumerate(allowed[choice], 1):
        print(f"{i}. {value}")
    selection = []
    while True:
        line = input("Values (blank to finish): ")
        if not line:
            break
        parts = line.split()
        for part in parts:
            if part in allowed[choice]:
                selection.append(mapping[choice][part])
        if not selection:
            print("No valid values selected")
    if not selection:
        print("Nothing to update")
        return False
    return preview_and_apply(kits, field, selection)


def preview_and_apply(kits, field, new_values):
    preview = preview_changes(kits, field, new_values)
    print("Preview of changes")
    if not preview:
        print("No kits match the selection")
        return False
    for item in preview:
        print(f"{item['name']}: {item['old']} -> {item['new']}")
    confirm = input("Apply changes? (y/n): ")
    if confirm.lower() != "y":
        print("Changes cancelled")
        return False
    apply_bulk_update(kits, field, new_values)
    print("Changes applied")
    return True
