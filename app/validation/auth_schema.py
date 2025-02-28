from pydantic import BaseModel, EmailStr
from typing import Optional

class AuthSchema(BaseModel):
        
    email: EmailStr
    password: str
    
class AuthResponse(BaseModel):
    
    auth_token: Optional[str] = None
    
    class Config:
        from_attributes = True