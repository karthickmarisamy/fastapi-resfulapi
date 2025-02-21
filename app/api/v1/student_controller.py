from fastapi import APIRouter
from validation.student_schema import StudentSchema
from services.student import StudentService
router = APIRouter()

@router.post('/student', response_model = StudentSchema)
async def create_student(student: StudentSchema, user_service: StudentService = Depends()):
    return await user_service.create_user(student)

@router.get('/student')
async def get_all_students(id: str, user_service: StudentService = Depends()):
    return await user_service.get_all_users(id)

@router.get('/student/{student_id}')
async def get_student_info(id: str, user_service: StudentService = Depends()):
    return await user_service.get_user(id)    

@router.put('/student/{student_id}')
async def update_student_info(id: str, student: StudentSchema, user_service: StudentService = Depends()):
    return await user_service.update_user(id, student)

@router.delete('/student/{student_id}')
async def delete_student_info(id: str, student: StudentSchema, user_service: StudentService = Depends()):
    return await user_service.update_user(id, student)