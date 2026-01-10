from fastapi import FastAPI
import os

app = FastAPI()

MY_PROJECT = os.environ.get("MY_PROJECT", "default project")
API_KEY = os.environ.get("API_KEY") or "default"
if not API_KEY:
    raise ValueError("API_KEY is not set")


@app.get("/")
def read_root():
    return {"Hello": "World again!", "project_name": MY_PROJECT}
