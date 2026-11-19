# === Stage 4: Редактирование записей ===
# Project: TireSwap
from typing import Dict, Any, Optional


ALLOWED_TIRE_FIELDS: Dict[str, Any] = {
    "name": str,
    "size": str,
    "season": str,
    "mileage": float,
}


def is_editable_tire_payload(payload: Dict[str, Any]) -> bool:
    return all(key in ALLOWED_TIRE_FIELDS for key in payload)


def edit_tire_by_id(tires: Dict[str, Dict[str, Any]], tire_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    if tire_id not in tires:
        return {"status": "not_found"}

    if not is_editable_tire_payload(payload):
        return {"status": "invalid_fields", "allowed": list(ALLOWED_TIRE_FIELDS.keys())}

    tires[tire_id].update(payload)
    return {"status": "updated", "tire_id": tire_id}
