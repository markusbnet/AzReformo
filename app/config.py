import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Azure
    client_id: str
    client_secret: str
    tenant_id: str

    # Postgres
    postgres_url: str = os.getenv(
        "POSTGRES_URL", "postgres"
    ) 
    postgres_user: str = os.getenv("POSTGRES_USER", "postgres")
    postgres_password: str
    postgres_db: str = os.getenv("POSTGRES_DB", "azreformo")

    # app config
    app_data_refresh: int = os.getenv("APP_DATA_REFRESH", "5")

    class Config:
        env_file = ".env"


settings = Settings()
