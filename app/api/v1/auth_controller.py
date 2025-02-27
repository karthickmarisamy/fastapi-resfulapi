from fastapi import APIRouter
from validation.standard_schema import StandardResponse

router = APIRouter()

@router.get('/token', response_model = StandardResponse)
async def auth_token():
    return StandardResponse(
        status = True,
        data = [{"auth_token": "test"}],
        message = "Auth token"
    )