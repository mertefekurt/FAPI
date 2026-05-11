from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.auth import get_current_user, require_role
from app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=List[schemas.UserResponse])
def get_users(
    db: Session = Depends(get_db),
    _current_user: models.User = Depends(require_role("admin")),
):
    """Return all users for callers with the admin role."""
    users = db.query(models.User).all()
    return users

@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Return a user profile when the caller is that user or an admin."""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="kullanıcı bulunamadı")
    
    is_admin = any(role.name == "admin" for role in current_user.roles)
    if current_user.id != user_id and not is_admin:
        raise HTTPException(status_code=403, detail="bu işlem için yetkiniz yok")
    
    return user
