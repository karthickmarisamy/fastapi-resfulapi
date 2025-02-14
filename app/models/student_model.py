import uuid
import datetime
from sqlalchemy import Column, String, Integer, DateTime, CHAR
from db.database import base_model

class Personal_detail(base_model):
   
    __tablename__ = 'personal_detail'
    
    id = Column(CHAR(30), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    phone_number = Column(String(12), nullable=False)
    email = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.now)
    updated_on = Column(DateTime, nullable=True)