from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import text
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Annotated
import jwt

from db import get_db
from utils import verify_password
from services.user_service import get_user_by_username, get_user_by_email, add_user
from services.auth_service import create_access_token, get_current_user

from models import Users
from schemas import SignUp, Login, Token

router = APIRouter()

@router.post("/users/signup")
def signup(user_info: SignUp, db: Session = Depends(get_db)):
  username = user_info.username
  email = user_info.email
  
  user = get_user_by_username(username, db)
  if user:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="user"
    )
  user = get_user_by_email(email, db)
  if user:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="email"
    )
  if add_user(user_info, db):
    return{"message": "User Created"}
  else: 
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="DB session failed to add user"
    )

#everything within ithis function right now is pretty much my 
@router.post("/users/login")
def login(
  form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
  db: Session = Depends(get_db),
):
  identifier = form_data.username
  password = form_data.password
  
  user = get_user_by_username(identifier, db)
  if not user: 
    user = get_user_by_email(identifier, db)

  if not user or not verify_password(password, user.password):
    #here is pretty much where theat authenticate_user function finishes
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
    )
    
  access_token_expires = timedelta(minutes=1440)
  access_token = create_access_token(data={"sub": str(user.userid)}, expires_delta=access_token_expires)
  
  return Token(access_token=access_token, token_type="bearer")

@router.get("/users/me")
def read_me(current_user: Users = Depends(get_current_user)):
    return {"id": current_user.userid}