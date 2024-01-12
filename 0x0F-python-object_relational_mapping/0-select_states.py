#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if _name_ == "_main_":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
