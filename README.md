# FAPI

![FAPI cover](assets/readme-cover.svg)

FastAPI authentication and role-management service with JWT login, password hashing, SQLite persistence, role assignment, and guarded user endpoints.

## Run locally

```bash
git clone https://github.com/mertefekurt/FAPI.git
cd FAPI
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API surface

- `POST /auth/register` for account creation
- `POST /auth/login` for bearer-token login
- `GET /auth/me` for the current user profile
- `/roles` endpoints for role creation, listing, and assignment
- `/users` endpoints protected by the admin role

## Files

```text
app/main.py          FastAPI application setup
app/auth.py          JWT, password, and role dependencies
app/routers/         auth, role, and user routes
app/models.py        SQLAlchemy models
app/schemas.py       Pydantic request/response models
app/validators.py    password, username, and role checks
```
