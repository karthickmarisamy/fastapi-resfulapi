from pydantic import BaseModel
from typing import Optional

class StandardResponse(BaseModel):
    
    status: str
    data: Optional[dict] = None
    message: Optional[str] = None
    