from sqlalchemy.orm import Session

from models import Users 
from schemas import SignUp

from utils import hash_password


def get_user_by_id(id: int, db: Session):
  return db.query(Users).filter(Users.userid == id).first()

def get_user_by_username(username: str, db: Session):
  return db.query(Users).filter(Users.username == username).first()

def get_user_by_email(email: str, db: Session):
  return db.query(Users).filter(Users.email == email).first()

def add_user(user_info: SignUp, db: Session):
  db_user = Users(
    username = user_info.username, 
    firstname = user_info.firstname,
    lastname = user_info.lastname, 
    email=user_info.email,
    password=hash_password(user_info.password)
  )
  try:
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return True
  except SQLAlchemyError:
    db.rollback()
    return False