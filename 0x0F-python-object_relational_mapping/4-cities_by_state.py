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
    query = """ SELECT
                    cities.id, cities.name, states.name
                FROM
                    cities
                INNER JOIN states ON
                    cities.state_id = states.id
                ORDER BY cities.id
            """
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
