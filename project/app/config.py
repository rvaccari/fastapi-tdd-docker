import logging
from functools import lru_cache

from decouple import config
from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = config("ENVIRONMENT", default="dev")
    testing: bool = config("TESTING", default=False, cast=bool)
    database_url: AnyUrl = config("DATABASE_URL_SSL", default="sqlite://sqlite.db")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
