from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class StandardResponse(BaseModel, Generic[T]):
    
    status: bool
    data: Optional[T] = None
    message: Optional[str] = None
    