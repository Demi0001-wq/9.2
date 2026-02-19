def filter_by_state(records: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Filters a list of dictionaries by the 'state' key."""
    return [record for record in records if record.get('state') == state]


def sort_by_date(records: list[dict], reverse: bool = True) -> list[dict]:
    """Sorts a list of dictionaries by the 'date' key."""
    return sorted(records, key=lambda x: x['date'], reverse=reverse)
