from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.student_model import Personal_detail
from datetime import datetime
from db.database import get_db
from sqlalchemy import delete, update

class StudentRepository:
    
    def __init__(self, db_session: AsyncSession = Depends(get_db)):
        
        self.db_session = db_session
    
    async def get_all_users(self):
        
        result = await self.db_session.execute(select(Personal_detail))
        return result.scalars().all()
    
    async def get_user(self, id: str):
        
        result = await self.db_session.execute(select(Personal_detail).filter(id == Personal_detail.id))
        return result.scalars().first()

    async def user_exists(self, email: str):
        
        result = await self.db_session.execute(select(Personal_detail).filter(email == Personal_detail.email))
        return result.scalars().first() is not None
    
    async def save_user(self, user: Personal_detail):
    
        if await self.user_exists(user.email):
            raise ValueError(f"{user.email} is already exists")
       
        self.db_session.add(user)
        await self.db_session.commit()
        await self.db_session.refresh(user)
        
        return user
    
    async def remove_user(self, id: str):
        
        try:
            
            delete_smt = delete(Personal_detail).where(id == Personal_detail.id)
            result = await self.db_session.execute(delete_smt)
            await self.db_session.commit()
    
            if result.rowcount > 0:
                return {"message": "Delete successfully", "status": False}  
            else:
                return {"message": "Id is not found", "status": False}
            
        except Exception as e:
            return {"message": str(e), "status": False}
    
    async def update_user(self, id: str, data: Personal_detail):
        
        try:
            
            update_data = data.dict(exclude_unset = True)
            update_data['updated_on'] = datetime.now()  
            update_stmt = (
                            update(Personal_detail)
                        .where(id == Personal_detail.id)
                        .values(**update_data)
                        )      
            result = await self.db_session.execute(update_stmt)
            await self.db_session.commit()
            
            if result.rowcount > 0:
                return {
                    "message": "User info has been updated successfully",
                    "status": True
                    }
            else: 
                return {
                    "message": "User id is invalid",
                    "status": False
                    }
            
        except Exception as e:
            return {
                "message": "User update is failed",
                "status": False
                }