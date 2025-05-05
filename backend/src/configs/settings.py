from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    TITLE: str
    SECRET_KEY: str
    DEBUG: bool
    ENVIRONMENT: Literal["DEV", "STAGING", "PRODUCTION"] = "DEV"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_ACCESS_SECRET_KEY: str
    REFRESH_TOKEN_EXPIRE_HOURS: int
    JWT_REFRESH_SECRET_KEY: str
    POSTGRES_SERVER: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    DATABASE_URL: str | None = None

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        uri = (
            self.DATABASE_URL
            if self.DATABASE_URL
            else f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
        print(f"DATABASE_URI: {uri}")
        return uri


settings = Settings()  # type: ignore
