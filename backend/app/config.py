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


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True, extra="ignore")

    PROJECT_NAME:str

    JWT_KEY:str
    JWT_ALGORITHM:str
    JWT_EXPIRY_MINUTES:int

    DB_URL:str

    # FRONTEND_HOST: str = "https://localhost:3000"
    # BACKEND_CORS_ORIGINS: Annotated[
    #     list[AnyUrl] | str, BeforeValidator(parse_cors)
    # ] = []

    # @computed_field 
    # @property
    # def all_cors_origins(self) -> list[str]:
    #     return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
    #         self.FRONTEND_HOST
    #     ]

settings = Settings()