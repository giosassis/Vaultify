# uvicorn app.main:app --reload

from fastapi import FastAPI
from app.routes import auth_router

app = FastAPI()
app.include_router(auth_router.router)

@app.get("/")
def read_root():
    return {"message": "Hello, Vaultify!"}