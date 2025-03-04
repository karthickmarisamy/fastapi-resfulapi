from fastapi import Depends
from repository.auth_repository import AuthRepository
from validation.auth_schema import AuthSchema, AuthResponse, AuthTokenUserdata
from models.student_model import Personal_detail
from auth.auth import create_access_token

class AuthService:
    
    def __init__(self, auth_repo: AuthRepository = Depends(AuthRepository)):
        self.auth_repo = auth_repo
        
    async def authenticate(self, credential: AuthSchema):
        
        try:
            
            auth = Personal_detail(
                email = credential.email,
                password = credential.password
            )
            
            user = await self.auth_repo.authenticate(auth)
            
            if user is None:
                return {"message": "Invalid credentials", "status": False}

            auth_token = create_access_token({
                "sub": user.id,  # Or "sub": user.email if you prefer
                "name": user.name,
                "email": user.email,
                "phone": user.phone_number,
                "age": user.age
            })
            
            return {"message": "Success", "status": True, "data": {"auth_token": auth_token}}
            
        except Exception as e: 
            return {"message": f"An error occured : {str(e)}", "status": False}