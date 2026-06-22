import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

database_URL = os.getenv("DATABASE_URL")

engine = create_engine(database_URL, echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
