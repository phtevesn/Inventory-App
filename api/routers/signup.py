from fastapi import APIRouter


router = APIRouter()

@router.get("/signup")
def signup_health():
  return{"ok": True}