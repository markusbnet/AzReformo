from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    # Azure
    client_id: str
    client_secret: str
    tenant_id: str

    # Postgres
    postgres_url: str = os.getenv(
        "POSTGRES_URL", "postgres"
    )  # postgres defined in docker-compose for networking
    postgres_user: str = os.getenv("POSTGRES_USER", "postgres")
    postgres_password: str
    postgres_db: str = os.getenv("POSTGRES_DB", "azreformo")

    class Config:
        env_file = ".env"


settings = Settings()
