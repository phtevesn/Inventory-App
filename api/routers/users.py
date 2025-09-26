from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import get_db
from utils import hash_password, verify_password

from models import Users

from schemas import SignUp, Login

router = APIRouter()

@router.post("/users/signup")
def signup(user_info: SignUp, db: Session = Depends(get_db)):
  username = user_info.username
  email = user_info.email
  
  user = db.query(Users).filter(Users.username == username).first()
  if user:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="user"
    )
  user = db.query(Users).filter(Users.email == email).first()
  if user:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="email"
    )
  
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


@router.post("/users/login")
def login(login_info: Login, db: Session = Depends(get_db)):
  identifier = login_info.usernameOrEmail
  password = login_info.password
  
  user = db.query(Users).filter((Users.username == identifier) | (Users.email == identifier)).first()
      
  if not user or not verify_password(password, user.password):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
    )

  return {"message": "Login successful"}