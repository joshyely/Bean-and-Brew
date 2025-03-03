from pydantic import (
    computed_field,
    AnyUrl,
    BeforeValidator,
)

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
from typing import Annotated, Any

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True, extra="ignore")

    PROJECT_NAME:str

    JWT_KEY:str
    JWT_ALGORITHM:str
    JWT_EXPIRY_MINUTES:int

    DB_URL:str

    ORIGINS:list[str]

    

settings = Settings()