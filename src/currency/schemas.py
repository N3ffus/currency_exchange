from pydantic import BaseModel, PositiveFloat
from enum import Enum


class ExchangeScheme(BaseModel):
    currency_to: str
    currency_from: str
    amount: int = 1


class ExchangeOutput(BaseModel):
    result: PositiveFloat


class CurrencyList(BaseModel):
    currencies: dict[str, str]




