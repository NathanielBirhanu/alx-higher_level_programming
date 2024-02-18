#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """
    State class represents a table in the database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    connection_string = (
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
        f'?charset=utf8mb4'
    )
    engine = create_engine(connection_string, pool_pre_ping=True)
    Base.metadata.create_all(engine)
