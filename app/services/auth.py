from fastapi import Depends
from repository.auth_repository import AuthRepository
from validation.auth_schema import AuthSchema, AuthResponse
from auth.auth import pwd_context
from models.student_model import Personal_detail

class AuthService:
    
    def __init__(self, auth_repo: AuthRepository = Depends(AuthRepository)):
        self.auth_repo = auth_repo
        
    async def authenticate(self, credential: AuthSchema):
        
        try:
            
            auth = Personal_detail(
                email = credential.email,
                password = pwd_context.hash(credential.password)
            )
            
            user = await self.auth_repo.authenticate(auth)
        
            if user is None:
                return {"message": "Invalid credentials", "status": False}

            return {"message": "Success", "status": True, "data": pwd_context.hash(credential.password)}
            
        except Exception as e: 
            return {"message": f"An error occured : {str(e)}", "status": False}