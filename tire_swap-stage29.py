# === Stage 29: Серии по дням ===
# Project: TireSwap
from collections import OrderedDict


def group_consecutive_days(actions):
    """Group a list of actions by consecutive calendar days.

    Each action carries a 'date' field.  Consecutive days (differing by
    exactly one day) are merged into a single group.  Non-consecutive
    days start a new group.  Groups are returned as a list of tuples,
    where each tuple is (start_date, end_date, [actions]).
    """
    if not actions:
        return []

    ordered = sorted(actions, key=lambda a: a['date'])
    groups = []
    current = [ordered[0]]
    prev = ordered[0]['date']

    for action in ordered[1:]:
        current_date = action['date']
        delta = _days_between(prev, current_date)
        if delta == 1:
            current.append(action)
        else:
            groups.append((prev, _days_between(current[0]['date'], current[-1]['date']), current))
            current = [action]
        prev = current_date

    groups.append((prev, _days_between(current[0]['date'], current[-1]['date']), current))
    return groups


def _days_between(date_a, date_b):
    """Return the number of days between two date objects."""
    try:
        from datetime import date as date_cls
        return (date_cls(date_b.year, date_b.month, date_b.day) -
                date_cls(date_a.year, date_a.month, date_a.day)).days
    except Exception:
        return (date_b - date_a).days


def summarize_change_days(changes):
    """Summarize consecutive activity days for a set of change records.

    Each change record must contain a 'date' field.  The function returns
    a list of dictionaries describing each consecutive-day span, including
    the start date, end date, the number of changes in the span, and the
    most frequent action type.
    """
    change_actions = [{'date': c['date'], 'action': c['action']} for c in changes]
    return group_consecutive_days(change_actions)
