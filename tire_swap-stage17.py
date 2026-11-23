# === Stage 17: Слияние записей ===
# Project: TireSwap
def combine_tuples(tuples, fields, winners):
    """Combine two records on the given fields, choosing the winner per field."""
    if len(tuples) != 2:
        raise ValueError("Expected exactly two tuples to combine.")
    if len(fields) != len(winners):
        raise ValueError("Number of fields must match number of winners.")
    for key in fields:
        if key not in tuples[0] or key not in tuples[1]:
            raise KeyError(f"Field {key} missing in one of the tuples.")
    combined = {}
    for key, index in zip(fields, winners):
        combined[key] = tuples[index][key]
    return combined
