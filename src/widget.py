from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Masks a card or account info string.

    Example input: "Visa Platinum 7000792289606361" or "Счет 73654108430135874305"
    """
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower().startswith("счет") or name.lower().startswith("account"):
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Converts a date string to the format DD.MM.YYYY.

    Example input: "2024-03-11T02:26:18.671407"
    """
    # Simple slicing since we just need DD.MM.YYYY
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
