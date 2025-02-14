from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class StudentSchema(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[str] = None
    updated_on: Optional[datetime] = None
        
    class config:
        orm_mode= True