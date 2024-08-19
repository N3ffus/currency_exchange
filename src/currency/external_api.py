import requests

from src.config import settings
from src.currency.exceptions import InvalidCurrencyError


def get_list():
    url = "https://api.apilayer.com/currency_data/list"

    headers = {
        "apikey": settings.EXTERNAL_API_KEY
    }

    response = requests.get(url, headers=headers).json()
    if not response.get("success"):
        raise
    return response


def exchange_currency(currency_to: str, currency_from: str, amount: int):
    url = f"https://api.apilayer.com/currency_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

    headers = {
        "apikey": "vsHPccKoPu3idiL0WeH9kVrM5Bd5TeVs"
    }

    response = requests.get(url, headers=headers).json()
    if not response.get("success"):
        raise InvalidCurrencyError
    return response.get("result")
