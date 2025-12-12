from fastapi import FastAPI

from app.routes.users import router as users_router
from app.routes.messages import router as messages_router
from app.routes.conversations import router as conversations_router
from app.routes.friends import router as friends_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(messages_router, prefix="/messages", tags=["messages"])
app.include_router(conversations_router, prefix="/conversations", tags=["conversations"])
app.include_router(friends_router, prefix="/friends", tags=["friends"])



@app.get("/")
async def root():
    return {"message": "Hello World"}