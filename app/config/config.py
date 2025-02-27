from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings
import os

load_dotenv(dotenv_path = Path(__file__).resolve().parent.parent.parent / '.env')

class Settings(BaseSettings):
    
    DB_USERNAME: str = os.getenv('DB_USERNAME')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_PORT: int = os.getenv('DB_PORT')
    DB_HOST: str = os.getenv('DB_HOST')
    JWT_SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRES_IN_MINTUES: int = 2880
    
    class Config:
        env_file = ".env"

settings = Settings()