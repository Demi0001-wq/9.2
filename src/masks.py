def get_mask_card_number(card_number: str) -> str:
    """Masks a card number.

    Format: XXXX XX** **** XXXX
    First 6 and last 4 digits are visible.
    """
    masked = card_number[:6] + "*" * 6 + card_number[-4:]
    return f"{masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:]}"


def get_mask_account(account_number: str) -> str:
    """Masks an account number.

    Format: **XXXX
    Only the last 4 digits are visible.
    """
    return f"**{account_number[-4:]}"
