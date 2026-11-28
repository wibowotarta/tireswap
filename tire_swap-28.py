# === Stage 28: Аномальные значения ===
# Project: TireSwap
"""Anomaly detection for the tire kit's numerical fields.

This module is self-contained and depends only on the standard library.
It implements a simple statistical outlier detector based on z-scores,
which can be reused from the main TireSwap application.
"""

from statistics import mean, pstdev


def _zscore(value, values):
    """Return the z-score of a value relative to a sample of values.

    A z-score measures how many standard deviations a value lies from
    the mean.  When the sample is too small to compute a meaningful
    deviation, the function returns 0.0 so callers treat everything as
    normal and simply skip the outlier check.
    """
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    spread = pstdev(values)
    if spread == 0:
        return 0.0
    return (value - avg) / spread


def find_anomalies(values, threshold=3.0):
    """Identify anomalous entries in a numeric list.

    Parameters
    ----------
    values : sequence of numbers
        The full set of values, including the one under inspection.
    threshold : float, optional
        A value is flagged as anomalous when its absolute z-score meets
        or exceeds this threshold.  Defaults to 3.0, the common rule of
        thumb for spotting outliers.

    Returns
    -------
    list of int
        Indices (into the input sequence) whose values look anomalous.
        The returned list is always a fresh list, never a view, so the
        caller can safely mutate the original data afterwards.
    """
    anomalies = []
    if len(values) < 2:
        return anomalies
    for index, value in enumerate(values):
        if abs(_zscore(value, values)) >= threshold:
            anomalies.append(index)
    return anomalies


def clamp_outliers(values, replacement, threshold=3.0):
    """Replace anomalous entries with a constant value.

    This is a convenience wrapper around :func:`find_anomalies`.  It is
    handy when you want to scrub bad mileage readings before persisting
    a kit record.  Every anomalous position is overwritten with
    ``replacement``; all other values pass through untouched.
    """
    result = list(values)
    for index in find_anomalies(values, threshold=threshold):
        result[index] = replacement
    return result
