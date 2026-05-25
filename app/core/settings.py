
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DB_URL: str = "sqlite:///./document_processor.db"


settings = Settings()
