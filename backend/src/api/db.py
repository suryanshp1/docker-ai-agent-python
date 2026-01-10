import os
import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = sqlmodel.create_engine(DATABASE_URL)

# database models
# does not creates db migrations
def init_db():
    print("Creating database tables....")
    SQLModel.metadata.create_all(engine)


# api routes
def get_session():
    with Session(engine) as session:
        yield session