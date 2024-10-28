#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '',
    database = 'hbtn_0e_0_usa'
    )

cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

for row in cur.fetchall():
    print(row)

cur.close()
db.close()
