from db.database import Base, engine
import models


def reset_db():
    Base.metadata.drop_all(bind=engine, checkfirst=True)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_db()
