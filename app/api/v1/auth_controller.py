from fastapi import APIRouter, Depends
from validation.standard_schema import StandardResponse
from validation.auth_schema import AuthResponse, AuthSchema
from services.auth import AuthService
from validation.student_schema import UserResponseSchema

router = APIRouter()

@router.post('/authenticate', response_model = StandardResponse)
async def auth_token(user_credential: AuthSchema, auth_service: AuthService = Depends(AuthService)):
    
    user = await auth_service.authenticate(user_credential)
    
    if user['status']:
        
        ##user_info = UserResponseSchema.from_orm(user['data'])
        
        return StandardResponse(
            status = True,
            data = user['data'],
            message = "Auth token"
        )
        
    return StandardResponse(
        status = user['status'],
        message = user['message']
    )
    
    