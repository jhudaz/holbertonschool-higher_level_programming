#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

if __name__ == "__main__":
    class State(Base):
        __tablename__ = "states"
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(256), nullable=False)

        dialect = "mysql"
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        host = "localhost"
        port = 3306

        engine = create_engine("{}://{}:{}@{}:{}/{}".format(
            dialect,
            user,
            passwd,
            host,
            port,
            db
        ))
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        try:
            state = session.query(State.id, State.name).first()
            session.commit()
            print("{}: {}".format(state[0], state[1]))
        except TypeError:
            print("")
