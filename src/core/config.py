from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the application"""

    APP_NAME: str = "sample-app"
    MODEL_NAME: str = "gpt-4.1-nano"
    OPENAI_API_KEY: str = ""
    CLOUD_LOGGING: bool = False


@lru_cache
def get_settings() -> Settings:
    """Get the settings

    Returns:
        Settings: The settings
    """
    return Settings()


settings = get_settings()
