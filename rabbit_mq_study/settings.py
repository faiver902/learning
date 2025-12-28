from __future__ import annotations

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitMQSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    user_name: str = Field(alias="RABBITMQ_USERNAME")
    password: str = Field(alias="RABBITMQ_PASSWORD")
    host: str = Field(alias="RABBITMQ_HOST")
    port: int = Field(default=5672, alias="RABBITMQ_PORT")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    rabbit: RabbitMQSettings = RabbitMQSettings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
