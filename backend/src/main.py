from fastapi import FastAPI
from api.db import init_db
from contextlib import asynccontextmanager
from api.chat.routing import router as chat_router
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup
    init_db()
    yield
    # after app shutdown
    pass

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chat")

MY_PROJECT = os.environ.get("MY_PROJECT", "default project")
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY is not set")


@app.get("/")
def read_root():
    return {"Hello": "World again!", "project_name": MY_PROJECT}
