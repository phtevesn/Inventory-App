from fastapi import APIRouter
from sqlalchemy import text
from db import engine

router = APIRouter()

@router.get("/health/db")
def db_health():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar_one()
    return {"ok": True, "db": result}