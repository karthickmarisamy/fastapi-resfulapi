from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path = Path(__file__).resolve().parent.parent / '.env')

from fastapi import FastAPI
from controllers.student_controller import router as student_router

app = FastAPI()

app.include_router(student_router, prefix='/api', tags=['student'])

@app.get('/')
def index():
    return {"success": True}