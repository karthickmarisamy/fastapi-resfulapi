from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from services.student import StudentService
from validation.student_schema import StudentSchema
from validation.standard_schema import StandardResponse

router = APIRouter()

@router.get("/student", response_model = StandardResponse)
async def get_all_students(user_service: StudentService = Depends(StudentService)):
    
    users = await user_service.get_all_users()
    users_serialized = [StudentSchema.from_orm(user) for user in users]

    return StandardResponse(
        status = True,
        data = users_serialized,
        message = "List"
    )

@router.get('/student/{id}', response_model = StandardResponse)
async def get_student_info(id: str, user_service: StudentService = Depends(StudentService)):
    
    user = await user_service.get_user(id)
    
    if user is None:
        
        return JSONResponse(
            status_code = status.HTTP_404_NOT_FOUND,
            content = StandardResponse(
                status = False,
                data = None,
                message = "User info is not found"
        ).dict())
    
    return StandardResponse(
            status = True,
            data = StudentSchema.from_orm(user),
            message = "Success"
        )

@router.post('/student', response_model = StandardResponse)
async def create_student(student: StudentSchema, user_service: StudentService = Depends(StudentService)):
    user =  await user_service.create_user(student)
    
    if user['status']:

        return StandardResponse(
            status = True,
            data = StudentSchema.from_orm(user['data']),
            message = user['message']
        ) 
    
    return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = StandardResponse(
                status = user['status'],
                message = user['message']
        ).dict())  
        

@router.delete('/student/{id}', response_model = StandardResponse)
async def delete_student_info(id: str, user_service: StudentService = Depends(StudentService)):

    user =  await user_service.remove_user(id)
    
    if user['status']:

        return StandardResponse(
            status = True,
            message = user['message']
        ) 
    
    return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = StandardResponse(
                status = user['status'],
                message = user['message']
        ).dict())  

@router.put('/student/{id}', response_model = StandardResponse)
async def update_student_info(id: str, student: StudentSchema, user_service: StudentService = Depends(StudentService)):

    user =  await user_service.update_user(id, student)
    
    if user['status']:

        return StandardResponse(
            status = True,
            message = user['message'],
            data = StudentSchema.from_orm(user['data'])
        ) 
    
    return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = StandardResponse(
                status = user['status'],
                message = user['message']
        ).dict())  