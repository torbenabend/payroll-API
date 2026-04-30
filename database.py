from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_URL = URL.create(
    "postgresql",
    username="postgres",
    password="2512",
    host="localhost",
    database="payroll-api"
)

engine = create_engine(database_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
