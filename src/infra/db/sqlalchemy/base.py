from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime


Base = declarative_base()


def create_database(engine) -> None:
    """Create database tables if not exist"""
    Base.metadata.create_all(bind=engine)
