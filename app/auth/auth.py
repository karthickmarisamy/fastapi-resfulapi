from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, status

from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel

from config.config import settings

## Initialize password context (password hashing and verification)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

## JWT token creation and validation
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    
## Create JWT Token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_IN_MINTUES)
    
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    
    return encode_jwt

## Decode the JWT token
def verify_access_token(token: str):
    
    credential_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Invaild access token",
        headers = {"WWW-Authenticate": "Bearer"},
    )
    
    try:
        
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        
        if username is None:
            raise HTTPException
        return username
    
    except JWTError:
        raise credential_exception
        