from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import settings
from sqlalchemy.engine.url import URL

DATABASE_URL = URL.create(
    drivername = "mysql+asyncmy",
    username = settings.DB_USERNAME,
    password = settings.DB_PASSWORD,
    host = settings.DB_HOST,
    port = settings.DB_PORT,
    database = settings.DB_NAME
)

engine = create_async_engine(
    DATABASE_URL,
    pool_size = 5,
    max_overflow = 10,
    pool_timeout = 30,
    pool_recycle = 1800, ## in seconds
    echo = False
)

sessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False)
base_model = declarative_base()

async def get_db():
    
    db = sessionLocal()
    
    try: 
        yield db
    finally:
        await db.close()