import pathlib
from fastapi import (
    FastAPI,
    Request
)
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.db.mongoclient import get_db
from app.users.routers import router as user_router

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=str(BASE_DIR / '.env'))

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)

@app.on_event("startup")
def on_startup():
    global conn
    conn = get_db()
    print(f"Connected to MongoDB")

@app.get("/api")
async def hello_world():
    print("conn", conn)
    return {"Hello": "World"}
