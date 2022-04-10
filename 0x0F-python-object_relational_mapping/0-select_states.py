#!/usr/bin/python3
"""
Get all states
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    row = cursor.fetchall()
    for element in row:
        print(element)
