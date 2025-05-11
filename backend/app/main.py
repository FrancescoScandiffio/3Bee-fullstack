from fastapi import FastAPI

from app.api.endpoints import chat

app = FastAPI()

app.include_router(chat.router)
