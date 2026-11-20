# === Stage 8: Генерация идентификаторов ===
# Project: TireSwap
import uuid
import re

PROJECT_PREFIX = "ts"

def generate_id():
    while True:
        raw = uuid.uuid4().hex
        candidate = f"{PROJECT_PREFIX}-{raw}"
        if not re.fullmatch(r"[a-zA-Z0-9-]+", candidate):
            continue
        if candidate in _seen:
            continue
        _seen.add(candidate)
        return candidate

_seen = set()
