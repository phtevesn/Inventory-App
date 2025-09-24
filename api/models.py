from sqlalchemy import Column, Integer, String, BigInteger, DateTime, func
from sqlalchemy.orm import declarative_base 

Base = declarative_base()

class Users(Base):
  __tablename__ = "users"
  __table_args__ = {'schema': 'inv'}
  
  userid = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  email = Column(String, unique=True, nullable=False) 
  created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
  deleted_at = Column(DateTime(timezone=True), nullable=True)
  firstname = Column(String, nullable=False)
  lastname = Column(String, nullable=False)
  