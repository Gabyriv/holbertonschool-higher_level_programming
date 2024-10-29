#!/usr/bin/python3

"""
Script that lists all states in the database.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd='',
        db=sys.argv[3]
        )

    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states ORDER BY states.id ASC""")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
