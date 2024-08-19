from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    TEST_DB_HOST: str
    TEST_DB_PORT: str
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str
    SECRET_KEY: str
    EXTERNAL_API_KEY: str

    @property
    def ASYNC_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()