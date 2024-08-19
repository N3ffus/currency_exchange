import uvicorn
from fastapi import FastAPI

from src.auth.router import auth_router
from src.currency.router import currency_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(currency_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app")