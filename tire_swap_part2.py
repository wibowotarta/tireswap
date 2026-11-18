# === Stage 2: Проверка полей ===
# Project: TireSwap
def normalize_input(raw):
    value = raw.strip()
    if value.lower() == "":
        return ""
    return value.capitalize()


def validate_name(name):
    if not name:
        return "Название комплекта не может быть пустым."
    if len(name) > 100:
        return "Название слишком длинное (максимум 100 символов)."
    if not any(char.isalnum() or char in "- / " for char in name):
        return "Название должно содержать только буквы, цифры и символы ' - / '."
    return None


def validate_size(size):
    if not size:
        return "Размер не может быть пустым."
    if not any(char.isdigit() for char in size):
        return "Размер должен содержать цифры (например: 205/55 R16)."
    if len(size) > 30:
        return "Размер слишком длинный."
    return None


def validate_season(season):
    valid = {"Лето", "Зима", "Всесезон"}
    if not season:
        return "Сезон не может быть пустым."
    if season not in valid:
        return "Сезон должен быть одним из: Лето, Зима, Всесезон."
    return None


def validate_mileage(mileage):
    if mileage is None:
        return None
    if not str(mileage).isdigit():
        return "Пробег должен быть числом (например: 45000)."
    if int(mileage) < 0:
        return "Пробег не может быть отрицательным."
    if int(mileage) > 999999:
        return "Пробег превышает разумный предел (максимум 999999 км)."
    return None


def validate_set(name, size, season, mileage):
    errors = []
    errors.append(validate_name(name))
    errors.append(validate_size(size))
    errors.append(validate_season(season))
    errors.append(validate_mileage(mileage))
    return errors
