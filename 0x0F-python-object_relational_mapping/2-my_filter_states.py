#!/usr/bin/python3
"""
Get states by user imput
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
    cursor.execute("SELECT * FROM states\
            WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC".format(argv[4]))
    row = cursor.fetchall()
    if row:
        for element in row:
            print(element)
    cursor.close()
    db.close()
