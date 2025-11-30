from fastapi import FastAPI
from app.helpers import get_query
from app.database import get_db_connection

@app.get("/login")
def login():
    connection = get_db_connection()
    connection.cursor().execute()




@app.get("/")
async def root():
    return {"message": "Hello World"}