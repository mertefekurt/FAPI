import re
from fastapi import HTTPException

def validate_password_strength(password: str):
    if len(password) < 8:
        raise HTTPException(
            status_code=400,
            detail="şifre en az 8 karakter olmalı"
        )
    if not re.search(r"[A-Za-z]", password):
        raise HTTPException(
            status_code=400,
            detail="şifre en az bir harf içermeli"
        )
    if not re.search(r"[0-9]", password):
        raise HTTPException(
            status_code=400,
            detail="şifre en az bir rakam içermeli"
        )

def validate_username(username: str):
    if len(username) < 3:
        raise HTTPException(
            status_code=400,
            detail="kullanıcı adı en az 3 karakter olmalı"
        )
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        raise HTTPException(
            status_code=400,
            detail="kullanıcı adı sadece harf, rakam ve alt çizgi içerebilir"
        )

def validate_role_name(role_name: str):
    if len(role_name) < 2:
        raise HTTPException(
            status_code=400,
            detail="rol adı en az 2 karakter olmalı"
        )
    if not re.match(r"^[a-zA-Z0-9_]+$", role_name):
        raise HTTPException(
            status_code=400,
            detail="rol adı sadece harf, rakam ve alt çizgi içerebilir"
        )

