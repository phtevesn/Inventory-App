from config import settings
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from models import Base 

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True)

# 1) Make sure the schema exists
with engine.connect() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS inv"))
    conn.commit()

# 2) Create all tables defined on Base, in schema=inv
Base.metadata.create_all(bind=engine)
