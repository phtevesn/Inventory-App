from fastapi import Cookie, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from typing import Annotated

from config import settings
from schemas import TokenData
from models import Users
from db import get_db
from services.user_service import get_user_by_id

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login", auto_error=False)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt
  
def get_token_from_cookie(
  access_token: str | None = Cookie(default=None),
  bearer_token: str | None = Depends(oauth2_scheme), #if the header says its a bearer cookie
) -> str:
  if bearer_token:
      return bearer_token
  if access_token:
      return access_token
  raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Not authenticated",
      headers={"WWW-Authenticate": "Bearer"},
  )
  
async def get_current_user(token: str = Depends(get_token_from_cookie), db:Session = Depends(get_db)):
  credentials_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Could not validate credentials", 
    headers={"WWW-Authenticate": "Bearer"}
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    id = payload.get("sub")
    if id is None:
      print("hello")
      raise credentials_exception
    token_data = TokenData(id=id)
  except InvalidTokenError:
    raise credentials_exception
  
  user = get_user_by_id(int(token_data.id), db)
  if user is None:
    raise credentials_exception
  return user

async def get_current_active_user(current_user: Users = Depends(get_current_user)):
  return current_user