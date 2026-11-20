# === Stage 6: Связанная сущность ===
# Project: TireSwap
class SwapRecord:
    def __init__(self, kit_id, date, mileage, notes):
        self.kit_id = kit_id
        self.date = date
        self.mileage = mileage
        self.notes = notes

    def to_dict(self):
        return {
            "kit_id": self.kit_id,
            "date": self.date,
            "mileage": self.mileage,
            "notes": self.notes,
        }


def add_swap_record(kits, records, kit_id, date, mileage, notes=""):
    if kit_id not in kits:
        raise ValueError(f"Kit with id {kit_id} does not exist")
    new_record = SwapRecord(kit_id, date, mileage, notes)
    records.append(new_record)
    return new_record


def find_record_by_kit(records, kit_id):
    return [record for record in records if record.kit_id == kit_id]
