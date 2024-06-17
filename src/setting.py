from enum import Enum
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from utils.path import get_env_path


class AppSettings(BaseSettings):
    APIKEY: str = "your_gemini_key"

    class Config:
        env_prefix: str = "GEMINI_"
        env_file = get_env_path(".env")
        env_file_encoding = "utf-8"


@lru_cache()
def load_settings() -> AppSettings:
    return AppSettings()
