from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.student_schema import StudentSchema
from db.database import get_db
from models.student_model import Personal_detail
from utils.response_wrapper import api_response
from datetime import datetime

router = APIRouter()

@router.post('/student')
async def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    if db.query(Personal_detail).filter(Personal_detail.email == student.email).first():
        raise HTTPException(status_code = 400, detail = "Email Id is already registered")

    new_student = Personal_detail(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return api_response(data=new_student, message="New Student record is created successfully")

@router.get('/student')
async def get_all_students(db: Session = Depends(get_db)):
    students = db.query(Personal_detail).all()
    return api_response(data=students, message="All student personal details are retrieved successfully")

@router.get('/student/{student_id}')
async def get_student_info(student_id: str, db: Session = Depends(get_db)):
    student_info = db.query(Personal_detail).filter(Personal_detail.id == student_id).first()
    if student_info is None:
        raise HTTPException(status_code = 400, detail = "Invalid student id")
    return api_response(data = student_info, message = "Student record is retrieved successfully")

@router.put('/student/{student_id}')
async def update_student_info(student_id: str, student:StudentSchema, db: Session = Depends(get_db)):
    existing_record = db.query(Personal_detail).filter(Personal_detail.id == student_id).first()
    if not existing_record:
        raise HTTPException(status_code = 404, detail = "Student id is not found")        
    else:
        student.updated_on = datetime.now()
        for field, value in student.dict(exclude_unset= True).items():
            setattr(existing_record, field, value)
        db.commit()
        db.refresh(existing_record)
        return api_response(data = existing_record, message = "Student info has been updated successfully")

@router.delete('/student/{student_id}')
async def delete_student_info(student_id : str, db: Session = Depends(get_db)):
    existing_student = db.query(Personal_detail).filter(student_id == Personal_detail.id).first()
    if not existing_student:
        raise HTTPException(status_code = 404, detail = "Student is not found")
    db.delete(existing_student)
    db.commit()
    return api_response(message = "Sudent info is deleted successfully")