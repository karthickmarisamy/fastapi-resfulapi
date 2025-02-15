from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from schemas.student_schema import StudentSchema
from db.database import get_db
from models.student_model import Personal_detail
from utils.response_wrapper import api_response
from datetime import datetime

router = APIRouter()

@router.post('/student')
async def create_student(student: StudentSchema, db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(Personal_detail).filter(Personal_detail.email == student.email))
    exists = result.scalars().first()
    
    if exists:
        raise HTTPException(status_code = 400, detail = "Email Id is already registered")

    new_student = Personal_detail(**student.dict())
    
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    
    return api_response(data=new_student, message="New Student record is created successfully")

@router.get('/student')
async def get_all_students(db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(Personal_detail))
    student_info = result.scalars().all()
    return api_response(data=student_info, message="All student personal details are retrieved successfully")

@router.get('/student/{student_id}')
async def get_student_info(student_id: str, db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(Personal_detail).filter(Personal_detail.id == student_id))
    student_info = result.scalars().first()
    
    if student_info is None:
        raise HTTPException(status_code = 400, detail = "Invalid student id")
    
    return api_response(data = student_info, message = "Student record is retrieved successfully")

@router.put('/student/{student_id}')
async def update_student_info(student_id: str, student:StudentSchema, db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(Personal_detail).filter(Personal_detail.id == student_id))
    existing_record = result.scalars().first()
    
    if not existing_record:
        raise HTTPException(status_code = 404, detail = "Student id is not found")        
    
    student.updated_on = datetime.now()
    
    for field, value in student.dict(exclude_unset= True).items():
        setattr(existing_record, field, value)
    
    db.add(existing_record)
    await db.commit()
    await db.refresh(existing_record)
    
    return api_response(data = existing_record, message = "Student info has been updated successfully")

@router.delete('/student/{student_id}')
async def delete_student_info(student_id : str, db: AsyncSession = Depends(get_db)):
    
    existing_student = await db.execute(select(Personal_detail).filter(student_id == Personal_detail.id))
    existing_student = existing_student.scalars().first()
    
    if not existing_student:
        raise HTTPException(status_code = 404, detail = "Student is not found")
    
    await db.delete(existing_student)
    await db.commit()
    
    return api_response(message = "Sudent info is deleted successfully")