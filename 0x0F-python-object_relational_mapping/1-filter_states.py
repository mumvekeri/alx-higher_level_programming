#!/usr/bin/python3
"""A script that lists all states with a name starting with N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if _name_ == "_main_":
    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    # Fetch all the rows
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the database
    cur.close()
    db.close()
