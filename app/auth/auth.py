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
    
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    print(f"Plain password {plain_password}")
    print(f"Hashed password {hash_password}")
    return pwd_context.verify(plain_password, hashed_password)

## Create JWT Token
def create_access_token(user_data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = user_data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_IN_MINTUES)

    # Update expiration
    to_encode.update({"exp": expire})

    # Encode the token
    encode_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

    return encode_jwt

## Decode the JWT token
def verify_access_token(token: str):
    
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid access token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:

        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])

        user_id: str = payload.get("sub")

        if user_id is None:
            raise credential_exception

        user_data = {
            "id": user_id,
            "name": payload.get("name"),
            "email": payload.get("email"),
            "phone": payload.get("phone"),
            "age": payload.get("age")
        }
        
        return user_data

    except JWTError:
        raise credential_exception