import jwt

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.config import settings
from src.auth.constants import ALGORITHM
from src.auth.exceptions import TokenExpiredError, InvalidTokenError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_jwt_token(data: dict) -> str:
    return jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)


def get_user_from_token(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise TokenExpiredError
    except jwt.InvalidSignatureError:
        raise InvalidTokenError
