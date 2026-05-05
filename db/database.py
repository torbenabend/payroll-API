from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


database_URL = URL.create(
    "postgresql",
    username="postgres",
    password="2512",
    host="localhost",
    database="payroll-api"
)

engine = create_engine(database_URL, echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
