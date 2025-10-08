from fastapi import APIRouter, Depends, HTTPException, status, Response
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

@router.post("/users/login")
def login(
  response: Response,
  form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
  db: Session = Depends(get_db),
):
  identifier = form_data.username
  password = form_data.password
  
  user = get_user_by_username(identifier, db)
  if not user: 
    user = get_user_by_email(identifier, db)

  if not user or not verify_password(password, user.password):

    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid credentials",
    )
    
  access_token_expires = timedelta(minutes=1440)
  access_token = create_access_token(data={"sub": str(user.userid)}, expires_delta=access_token_expires)
  
  response.set_cookie(
    key="access_token",
    value=access_token,
    httponly=True,       # good security; JS can’t read it
    samesite="Lax",      # works on same-site (localhost:3000 → 8000)
    secure=False,        # set True only under HTTPS
    path="/",
    max_age=60*60*24,    # optional, 1 day
  )
  return {"message": "Login successful"}


@router.get("/users/me")
def me(current_user: Users = Depends(get_current_user)):
  return {"id": current_user.userid, "email": current_user.email}

@router.post("/users/logout")
def logout(response: Response):
  response.delete_cookie("access_token", path="/")
  return {"message": "you know how in clash royale the log rolls. instead of roll they say, autobots log out"}