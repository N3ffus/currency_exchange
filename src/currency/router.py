from fastapi import APIRouter, Depends

from src.auth.security import get_user_from_token
from src.currency.external_api import exchange_currency, get_list
from src.currency.schemas import ExchangeScheme, ExchangeOutput, CurrencyList


currency_router = APIRouter(
    prefix="/currency",
    tags=["Currency"],
    dependencies=[Depends(get_user_from_token)]
)


@currency_router.post("/exchange", response_model=ExchangeOutput)
async def get_exchange(exchange: ExchangeScheme):
    result = exchange_currency(**exchange.model_dump())
    return ExchangeOutput(result=result)


@currency_router.get("/list", response_model=CurrencyList)
async def currency_list():
    return get_list()
