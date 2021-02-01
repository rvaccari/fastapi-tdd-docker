import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl

log = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    environment: str = os.getenv('ENVIRONMENT', 'prod')
    testing: bool = os.getenv('TESTING', 1)
    database_url: AnyUrl = os.environ.get('DATABASE_URL')


@lru_cache()
def get_settings() -> BaseSettings:
    log.info('Loading config settings from the environment...')
    return Settings()
