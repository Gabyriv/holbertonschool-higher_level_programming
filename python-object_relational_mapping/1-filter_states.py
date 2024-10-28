#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = username,
        password = password,
        database = database_name
        )

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC""")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
