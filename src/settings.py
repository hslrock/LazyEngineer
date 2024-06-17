import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from utils.path import get_env_path


class GeminiSetting(BaseSettings):
    API_KEY: str = ""
    MODEL_NAME: str = ""

    class Config:
        env_prefix: str = "GEMINI_"
        env_file = get_env_path(".env")


class AppSettings(BaseSettings):
    GEMINI: BaseSettings = GeminiSetting()
    # class Config:
    #     env_prefix: str = "APP_"
    #     env_file = get_env_path(".env")


@lru_cache()
def load_settings() -> AppSettings:
    return AppSettings()
