from validation.student_schema import StudentSchema
from models.student_model import Personal_detail
from utils.response_wrapper import api_response
from repository.student_repository import StudentRepository

class StudentService:
    
    def __init__(self, user_repo: StudentRepository):
        self.user_repo = user_repo
    
    async def create_user(self, student: StudentSchema):
        
        new_user = Personal_detail(student)
        await self.user_repo.save_user(new_user)
        
        if new_user.id != None:
            return api_response(data = new_user, message = "New Student record is created successfully")
        
        return api_response(message = "Failed", status = False)
    
    async def get_all_users(self):
        return api_response(
            data = await self.user_repo.get_all_users(), 
            message = "Success"
        )
    
    async def get_user(self, id: str):
        return api_response(
            data = await self.user_repo.get_user(id), 
            message = "Success"
        ) 
    
    async def update_user(self, id: str, student: StudentSchema):
        return api_response(
            data = await self.user_repo.update_user(id, student), 
            message = "Success"
        )
    
    async def remove_user(self, id: str):
        
        await self.user_repo.remove_user(id)
        return api_response( 
            message = "User info is removed successfully"
        )