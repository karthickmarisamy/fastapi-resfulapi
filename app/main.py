from fastapi import FastAPI
from core.middleware import LoggingMiddleware
from api.v1.student_controller import router as student_router
from api.v1.auth_controller import router as auth_router

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.include_router(student_router, prefix='/api', tags=['student'])
app.include_router(auth_router, prefix='/api', tags=['auth'])

@app.get('/')
def index():
    return {"success": True}

@app.get("/routes")
def get_routes():
    return [{"path": route.path, "name": route.name, "methods": route.methods} for route in app.routes]
