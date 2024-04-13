#!/usr/bin/python3
"""A Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL
    conn = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3],
                            charset="utf8")
    # Create a cursor object using cursor() method
    cur = conn.cursor()
    # Execute SQL query to select all states from states table
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the rows in a list of lists
    query_rows = cur.fetchall()
    # Print each row
    for row in query_rows:
        print(row)
    # Close cursor and connection
    cur.close()
    conn.close()
