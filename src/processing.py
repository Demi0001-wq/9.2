def filter_by_state(records: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Filters a list of dictionaries by the 'state' key."""
    return [record for record in records if record.get('state') == state]
