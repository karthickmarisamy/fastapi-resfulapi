from pydantic import BaseModel, EmailStr
from typing import Optional

class AuthSchema(BaseModel):
        
    email: EmailStr
    password: str
    
class AuthResponse(BaseModel):
    
    auth_token: Optional[str] = None
    
    class Config:
        from_attributes = True
        
class AuthTokenUserdata(BaseModel):
    
    id: str = None
    name: str = None
    email: str = None
    phone_number: str = None
    age: str = None