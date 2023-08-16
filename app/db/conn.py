import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

POD_NAME: str = os.getenv("POD_NAME", "pod-demo")

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_size=5,
    max_overflow=15,
    pool_recycle=120,
    connect_args={
        "application_name": POD_NAME,
    },
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
