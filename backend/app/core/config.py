# backend/app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Webhook Açaí Guarima"
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"
        # Permite que o Pydantic ignore variáveis extras do .env (como MYSQL_ROOT_PASSWORD)
        extra = "ignore" 

settings = Settings()