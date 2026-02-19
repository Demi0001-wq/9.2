import json
import os
from typing import Any


def get_transactions(path: str) -> list[dict[str, Any]]:
    """
    Reads financial transaction data from a JSON file.
    Returns a list of dictionaries.
    If the file is not found, empty, or not a list, returns an empty list.
    """
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        return []
