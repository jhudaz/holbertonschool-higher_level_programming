#!/usr/bin/python3
""" module """
import MySQLdb
import sys

if __name__ == "__main__":
    db_conf = {
        'host':     'localhost',
        'user':     sys.argv[1],
        'passwd':   sys.argv[2],
        'db':       sys.argv[3],
        'port':     3306
    }
    db = MySQLdb.connect(**db_conf)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name like BINARY 'N%' ORDER BY id")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
