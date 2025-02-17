from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path = Path(__file__).resolve().parent.parent.parent / '.env')

class config():
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME= os.getenv('DB_NAME')
    DB_PORT= os.getenv('DB_PORT')
    DB_HOST= os.getenv('DB_HOST')

config = config()