from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import logging
import time

logging.basicConfig(level=logging.INFO)

class LoggingMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request, call_next):
        
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        logging.log(logging.INFO, f"Request {request.method} - {request.url} total duration {duration:.2f}s")
       
        return response