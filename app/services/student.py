from fastapi import Depends
from utils.response_wrapper import api_response
from repository.student_repository import StudentRepository
from validation.student_schema import StudentSchema
from models.student_model import Personal_detail

class StudentService:
    
    def __init__(self, student_repo: StudentRepository = Depends(StudentRepository)):
        
        self.student_repo = student_repo

    async def get_all_users(self):
        
        return api_response(
            data = await self.student_repo.get_all_users(), 
            message = "Success"
        )
    
    async def get_user(self, id: str):
        
        return api_response(
            data = await self.student_repo.get_user(id), 
            message = "Success"
        )
        
    async def create_user(self, student: StudentSchema):
        
        try:
            new_user = Personal_detail(
                name=student.name,
                phone_number=student.phone_number,
                email=student.email,
                age=student.age
            )
            new_user = await self.student_repo.save_user(new_user)
            
            if new_user.id:        
                return api_response(data = StudentSchema.from_orm(new_user), message = "New Student record is created successfully")
        
            return api_response(message="Failed to create student record", status=False)

        except ValueError as e:
            return api_response(message=str(e), status=False)

        except Exception as e:
            return api_response(message=f"An error occurred: {str(e)}", status=False)

    async def remove_user(self, id: str):
        
        result = await self.student_repo.remove_user(id)
        return api_response( 
            message = result['message'],
            status = result['status'],
            error = result['status'] == False
        )
    
    async def update_user(self, id: str, student: StudentSchema):
        
        result = await self.student_repo.update_user(id, student)
        return api_response(
            status = result['status'], 
            message = result['message'],
            error = result['status'] == False
        )