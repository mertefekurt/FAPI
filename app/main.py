from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, roles, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth & Role Management API")

app.include_router(auth.router)
app.include_router(roles.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "auth ve role management api'si"}

