#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from MySQL injections!"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = conn.cursor()
    state_name = sys.argv[4]
    cur.execute(
            'SELECT * FROM states WHERE CAST(name AS BINARY) ' +
            'LIKE %s ORDER BY id ASC;',
            [state_name]
        )
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
