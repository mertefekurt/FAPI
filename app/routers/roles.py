from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user, require_role

router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("", response_model=schemas.RoleResponse)
def create_role(
    role: schemas.RoleCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("admin"))
):
    db_role = db.query(models.Role).filter(models.Role.name == role.name).first()
    if db_role:
        raise HTTPException(status_code=400, detail="rol zaten mevcut")
    
    db_role = models.Role(name=role.name, description=role.description)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    print(f"yeni rol oluşturuldu: {role.name}")
    return db_role

@router.get("", response_model=List[schemas.RoleResponse])
def get_roles(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    roles = db.query(models.Role).all()
    return roles

@router.get("/{role_id}", response_model=schemas.RoleResponse)
def get_role(
    role_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    role = db.query(models.Role).filter(models.Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="rol bulunamadı")
    return role

@router.post("/{role_id}/assign/{user_id}")
def assign_role_to_user(
    role_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("admin"))
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="kullanıcı bulunamadı")
    
    role = db.query(models.Role).filter(models.Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="rol bulunamadı")
    
    if role in user.roles:
        raise HTTPException(status_code=400, detail="kullanıcı zaten bu role sahip")
    
    user.roles.append(role)
    db.commit()
    print(f"rol atandı: {user.username} -> {role.name}")
    return {"message": "rol başarıyla atandı"}

@router.delete("/{role_id}/remove/{user_id}")
def remove_role_from_user(
    role_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("admin"))
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="kullanıcı bulunamadı")
    
    role = db.query(models.Role).filter(models.Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="rol bulunamadı")
    
    if role not in user.roles:
        raise HTTPException(status_code=400, detail="kullanıcı bu role sahip değil")
    
    user.roles.remove(role)
    db.commit()
    print(f"rol kaldırıldı: {user.username} -> {role.name}")
    return {"message": "rol başarıyla kaldırıldı"}

