from fastapi import FastAPI, APIRouter
from app.helpers import get_query
from app.database import pool


router = APIRouter()

@router.get("/login")
def login():
    pass
