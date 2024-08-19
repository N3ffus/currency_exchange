from fastapi import HTTPException


class InvalidCurrencyError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail={"message": "Invalid currency name or amount"})


class InvalidCurrencyListError(HTTPException):
    def __init__(self):
        super().__init__(status_code=500, detail={"message": "Error loading the list of currencies"})
