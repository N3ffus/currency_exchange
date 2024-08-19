from src.database import Base

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    username: Mapped[str] = mapped_column(String(255))
    password: Mapped[str]

