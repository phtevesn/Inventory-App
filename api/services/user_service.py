from sqlalchemy.orm import Session

from models import Users 


def get_user_by_username(username: str, db: Session):
  return db.query(Users).filter(Users.username == username).first()
  

def get_user_by_email(email: str, db: Session):
  return db.query(Users).filter(Users.email == email).first()

