def get_mask_card_number(card_number: str) -> str:
    masked = card_number[:6] + "*" * 6 + card_number[-4:]
    return f"{masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:]}"


def get_mask_account(account_number: str) -> str:
    return f"**{account_number[-4:]}"
