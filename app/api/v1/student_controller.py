from fastapi import APIRouter, Depends, status
from services.student import StudentService
from validation.student_schema import StudentSchema
from validation.standard_schema import StandardResponse

router = APIRouter()

@router.get("/student")
async def get_all_students(user_service: StudentService = Depends(StudentService)):
    return await user_service.get_all_users()

@router.get('/student/{id}', response_model = StudentSchema)
async def get_student_info(id: str, user_service: StudentService = Depends(StudentService)):
    
    user = await user_service.get_user(id)
    
    if user is None:
        
        return StandardResponse(
            status = False,
            data = None,
            message = "User info is not found"
        ), status.HTTP_404_NOT_FOUND
    
    return StandardResponse(
            status = True,
            data = user,
            message = "Success"
        )

@router.post('/student')
async def create_student(student: StudentSchema, user_service: StudentService = Depends(StudentService)):
    return await user_service.create_user(student)

@router.delete('/student/{id}')
async def delete_student_info(id: str, user_service: StudentService = Depends(StudentService)):
    return await user_service.remove_user(id)

@router.put('/student/{id}')
async def update_student_info(id: str, student: StudentSchema, user_service: StudentService = Depends(StudentService)):
    return await user_service.update_user(id, student)