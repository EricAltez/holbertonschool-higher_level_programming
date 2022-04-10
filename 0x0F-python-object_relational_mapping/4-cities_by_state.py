#!/usr/bin/python3
"""
get all cities
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3305,
            user=argv[1],
            password=argv[2],
            db=argv[3]
            )

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    row = cursor.fetchall()
    if row:
        for element in row:
            print(element)
    cursor.close()
    db.close()
