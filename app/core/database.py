from typing import Generator

import re

from sqlalchemy import Select, create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

def resolve_table_name(): 
    words = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", class_name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", words).lower()


class Base(DeclarativeBase): 
    metadata = metadata

    __reprs_attr__ = []
    __repr_max_length = 15 

    @declared.attr.directive
    def __tablename__(cls) -> str:
        return resolve_table_name(cls.__name__) 


engine = create_engine(bind=engine)

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, autocommit=False)

def init_db():
    Base.metadata.create_all() 

def check_db_connection():
    with SessionLocal as session: 
        session.execute(text("SELECT 1"))

def get_db() -> [Generator, None, None]: 
    db = SessionLocal() 
    try:
        yield db
    finally: 
        db.close()
