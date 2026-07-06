# FAPI

FastAPI authentication and role-management service.

![FAPI cover](assets/readme-cover.svg)

## Run

```bash
git clone https://github.com/mertefekurt/FAPI.git
cd FAPI
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Surface

- `/auth/register`, `/auth/login`, `/auth/me`
- role creation, listing, and assignment
- admin-guarded user listing
- SQLAlchemy models with SQLite persistence
