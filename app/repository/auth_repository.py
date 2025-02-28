from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.student_model import Personal_detail
from db.database import get_db

class AuthRepository:
    
    def __init__(self, db_session: AsyncSession = Depends(get_db)):
        self.db_session = db_session
    
    async def authenticate(self, credential: Personal_detail):
        return await self.db_session.execute(select(Personal_detail).filter(credential.email == credential.email, credential.password == credential.password))