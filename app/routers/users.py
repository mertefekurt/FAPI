from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user, require_role

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=List[schemas.UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("admin"))
):
    users = db.query(models.User).all()
    return users

@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="kullanıcı bulunamadı")
    
    if current_user.id != user_id and not any(role.name == "admin" for role in current_user.roles):
        raise HTTPException(status_code=403, detail="bu işlem için yetkiniz yok")
    
    return user

