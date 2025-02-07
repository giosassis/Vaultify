# uvicorn app.main:app --reload

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.routes import auth_router
from fastapi.middleware.cors import CORSMiddleware


limiter = Limiter(key_func=get_remote_address)
origins = ["http://localhost:3000", "https://localhost:3000"]

app = FastAPI()
app.include_router(auth_router.router)

@app.on_event("startup")
async def startup():
    print("Starting app...")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello, Vaultify!"}