from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import logging
import time
from fastapi import Request, HTTPException
from typing import Callable
from auth.auth import verify_access_token
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.INFO)


class JWTMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next: Callable):
        
        try:
            
            if request.url.path.startswith("/api/authenticate"):
                return await call_next(request)
            
            authorization: str = request.headers.get("Authorization")

            if not authorization:
                raise HTTPException(status_code = 403, detail = "Authorization token is missing")
            
            token = authorization.split('Bearer ')[-1]
            payload = verify_access_token(token)
            request.state.user = payload
            
        except HTTPException as e:
            
            return JSONResponse(
                content = {"error": "Invalid or expired token", "detail": e.detail},
                status_code = e.status_code,
            )
                
        return await call_next(request)
        
class LoggingMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next: Callable):
        
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        logging.log(logging.INFO, f"Request {request.method} - {request.url} total duration {duration:.2f}s")
       
        return response