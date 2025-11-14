from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, roles

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth & Role Management API")

app.include_router(auth.router)
app.include_router(roles.router)

@app.get("/")
def root():
    return {"message": "auth ve role management api'si"}

