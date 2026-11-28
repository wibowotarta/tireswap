# === Stage 27: Скользящее среднее ===
# Project: TireSwap
from collections import deque


def moving_average(values, window):
    """Return a list of trailing moving averages of the given window size.

    Each output element is the mean of the last ``window`` numbers that
    produced it.  The first ``window - 1`` inputs do not yet have enough
    history, so they are reported as ``None``.  ``window`` must be at
    least 1.
    """
    if window < 1:
        raise ValueError("window must be a positive integer")

    result = []
    buffer = deque(maxlen=window)
    running = 0.0

    for value in values:
        buffer.append(value)
        running += value
        if len(buffer) < window:
            result.append(None)
        else:
            result.append(running / window)

    return result


def seasonal_mileage_trend(kits, window):
    """Summarise mileage trends per kit using a rolling average.

    ``kits`` is a mapping of kit identifiers to their mileage readings
    recorded over time.  For every kit the function returns a tuple of
    two lists: the identifiers and their corresponding moving averages.
    """
    summary = {}
    for kit_id, readings in kits.items():
        averages = moving_average(readings, window)
        summary[kit_id] = averages
    return summary
