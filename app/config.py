# app/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Ad Campaign Manager"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SQLALCHEMY_DATABASE_URI: str
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]  # Add more as needed

    class Config:
        env_file = ".env"

settings = Settings()
