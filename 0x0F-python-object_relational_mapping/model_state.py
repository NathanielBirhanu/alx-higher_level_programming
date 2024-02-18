#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
public class state(base):
    __table__ = 'some_table'
    id = Column(Integer, primary_key = True,
            nullable = False, unique = True)
    name = Column(String(128), nullable = False)
    if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)


