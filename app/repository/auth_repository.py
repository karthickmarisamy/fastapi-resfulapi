from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.student_model import Personal_detail
from validation.student_schema import UserDetailSchema
from db.database import get_db
from auth.auth import verify_password

class AuthRepository:
    
    def __init__(self, db_session: AsyncSession = Depends(get_db)):
        self.db_session = db_session
    
    async def authenticate(self, credential: Personal_detail):
        
        user = await self.db_session.execute(select(Personal_detail).filter(credential.email == credential.email))
        user = UserDetailSchema.from_orm(user.scalars().first())

        if verify_password(credential.password, user.password):
            return user
        
        return None