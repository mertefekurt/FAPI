from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
from app.database import engine, Base
from app.routers import auth, roles, users
from app.exceptions import validation_exception_handler, integrity_error_handler

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth & Role Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)

app.include_router(auth.router)
app.include_router(roles.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "auth ve role management api'si"}

