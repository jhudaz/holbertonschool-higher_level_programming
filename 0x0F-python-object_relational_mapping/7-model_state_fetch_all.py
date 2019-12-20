#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.sql import select

if __name__ == "__main__":

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
    result = engine.execute("SELECT * FROM states ORDER BY id")
    for _r in result:
        print("{}: {}".format(_r[0], _r[1]))
