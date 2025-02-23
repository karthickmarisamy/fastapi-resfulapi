from fastapi import APIRouter, Depends
from services.student import StudentService
from validation.student_schema import StudentSchema

router = APIRouter()

@router.get("/student")
async def get_all_students(user_service: StudentService = Depends(StudentService)):
    return await user_service.get_all_users()

@router.get('/student/{id}')
async def get_student_info(id: str, user_service: StudentService = Depends(StudentService)):
    return await user_service.get_user(id) 

@router.post('/student')
async def create_student(student: StudentSchema, user_service: StudentService = Depends(StudentService)):
    return await user_service.create_user(student)

@router.delete('/student/{id}')
async def delete_student_info(id: str, user_service: StudentService = Depends(StudentService)):
    return await user_service.remove_user(id)

@router.put('/student/{id}')
async def update_student_info(id: str, student: StudentSchema, user_service: StudentService = Depends(StudentService)):
    return await user_service.update_user(id, student)