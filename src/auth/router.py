from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated

from src.auth.security import create_jwt_token
from src.auth.exceptions import InvalidCredentialsError
from src.auth.schemas import UserScheme
from src.auth.models import User
from src.database import get_async_session


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth_router.post("/register")
async def register(user: UserScheme, session: AsyncSession = Depends(get_async_session)):
    new_user = User(**user.model_dump())
    session.add(new_user)
    await session.commit()
    return {"message": "Registration has been completed successfully!"}


@auth_router.post("/login")
async def login(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()],
                session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.username == user_credentials.username)
    user = await session.scalar(stmt)

    if user is None or user.password != user_credentials.password:
        raise InvalidCredentialsError
    return {"access_token": create_jwt_token({"sub": user_credentials.username})}

