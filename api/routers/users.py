from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import get_db
from utils import hash_password

from models import Users

from schemas import SignUp

router = APIRouter()

@router.post("/users/signup")
def signup_health(user_info: SignUp, db: Session = Depends(get_db)):
  db_user = Users(
    username = user_info.username, 
    firstname = user_info.firstname,
    lastname = user_info.lastname, 
    email=user_info.email,
    password=hash_password(user_info.password)
  )
  
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  
  
  return{"message": "User Created"}