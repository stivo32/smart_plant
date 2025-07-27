from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from smart_plant.config import DB_FILE

Base = declarative_base()

create_engine = create_engine(f"sqlite:///{DB_FILE}", echo=True, connect_args={"check_same_thread": False})
session_factory = sessionmaker(bind=create_engine)

def init_db():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=create_engine)
