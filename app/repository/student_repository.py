from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.student_model import Personal_detail
from datetime import datetime

class StudentRepository:
    
    def __init__(self, db_session: AsyncSession):
        
        self.db_session = db_session
        
    async def user_exists(self, email: str):
        
        result = await self.db_session(select(Personal_detail).filter(email = Personal_detail.email))
        
        return result.scalars().first() is not None
    
    async def save_user(self, user: Personal_detail):
    
        if await self.user_exists(self, user.email):
            raise ValueError(f"{user.email} is already exists")
       
        self.db_session.add(user)
        
        return await self.db_session.commit()
    
    async def get_all_users(self):
        
        result = self.db_session(select(Personal_detail))
        
        return result.scalars().all()
    
    async def get_user(self, id: str):
        
        result = await self.db_session(select(Personal_detail).filter(id = Personal_detail.id))
        
        return result.scalars().first()
    
    async def remove_user(self, id: str):
        
        await self.db_session(Personal_detail).where(id = Personal_detail.id)
        
        return await self.db_session.commit()
    
    async def update_user(self, id: str, data: Personal_detail):
        
        data.updated_on = datetime.now()        
        await self.db_session(Personal_detail).where(id = Personal_detail.id).values(**data)
        
        return await self.db_session.commit()