import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Converts transaction amount to RUB.
    Uses an external API for USD and EUR.
    """
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency_data = transaction.get("operationAmount", {}).get("currency", {})
    currency_code = currency_data.get("code")

    if currency_code == "RUB":
        return amount

    if currency_code in ["USD", "EUR"]:
        api_key = os.getenv("API_KEY")
        if not api_key:
            return 0.0

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        headers = {"apikey": api_key}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return float(data.get("result", 0.0))
        except Exception:
            return 0.0

    return 0.0
