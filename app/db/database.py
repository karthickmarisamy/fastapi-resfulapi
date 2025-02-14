from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import os

DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@localhost:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
base_model = declarative_base()

def get_db():
    db = sessionLocal()
    try: 
        yield db
    finally:
        db.close()