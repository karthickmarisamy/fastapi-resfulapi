from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class StudentSchema(BaseModel):
    
    id: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    age: Optional[int] = None
    updated_on: Optional[datetime] = None
    created_on: Optional[datetime] = None
    
class UserResponseSchema(BaseModel):
    
    id: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    updated_on: Optional[datetime] = None
    created_on: Optional[datetime] = None
        
    class Config:
        from_attributes = True