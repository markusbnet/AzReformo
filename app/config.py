from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    # Azure
    client_id: str = os.getenv("CLIENT_ID", "NA")
    secret_id: str = os.getenv("CLIENT_SECRET", "NA")
    tenant_id: str = os.getenv("TENANT_ID", "NA")

    # Postgres
    postgres_url: str = os.getenv("POSTGRES_URL", "localhost")
    postgres_port: str = os.getenv("POSTGRES_PORT", "5432")
    postgres_user: str = os.getenv("POSTGRES_USER", "postgres")
    postgres_password = os.getenv("POSTGRES_PASSWORD", "NA")
    postgres_db = os.getenv("POSTGRES_DB", "azreformo")


settings = Settings()
