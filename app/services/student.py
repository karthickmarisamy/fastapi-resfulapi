from fastapi import Depends
from utils.response_wrapper import api_response
from repository.student_repository import StudentRepository
from validation.student_schema import StudentSchema
from models.student_model import Personal_detail
from auth.auth import pwd_context

class StudentService:
    
    def __init__(self, student_repo: StudentRepository = Depends(StudentRepository)):
        self.student_repo = student_repo

    async def get_all_users(self):
        return await self.student_repo.get_all_users()        
    
    async def get_user(self, id: str):    
        return await self.student_repo.get_user(id)
        
    async def create_user(self, student: StudentSchema):
        
        try:
            new_user = Personal_detail(
                name=student.name,
                phone_number=student.phone_number,
                email=student.email,
                hashed_password = pwd_context.hash(student.hashed_password),
                age=student.age
            )
            new_user = await self.student_repo.save_user(new_user)
            
            if new_user.id:        
                return { "data": new_user, "message": "New Student record is created successfully", "status": True }
        
            return { "message": "Failed to create student record", "status": False }

        except ValueError as e:
            return { "message": str(e), "status": False }

        except Exception as e:
            return { "message": f"An error occurred: {str(e)}", "status": False }

    async def remove_user(self, id: str):    
        return await self.student_repo.remove_user(id)
    
    async def update_user(self, id: str, student: StudentSchema):
        return await self.student_repo.update_user(id, student)