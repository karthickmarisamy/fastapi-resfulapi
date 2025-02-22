from fastapi import FastAPI
from core.middleware import LoggingMiddleware
from api.v1.student_controller import router as student_router

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.include_router(student_router, prefix='/api', tags=['student'])

@app.get('/')
def index():
    return {"success": True}