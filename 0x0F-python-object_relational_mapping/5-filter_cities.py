#!/usr/bin/python3
"""list all cities from database"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    uname = sys.argv[1]
    pword = sys.argv[2]
    dbname = sys.argv[3]
    stname = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=uname,
                         passwd=pword, db=dbname, charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN"
                " states ON cities.state_id = states.id"
                " WHERE states.name = %s ORDER BY cities.id ASC", [stname])
    query_rows = cur.fetchall()
    end = 0
    for row in query_rows:
        if end == 1:
            print(", ", end="")
        end = 1
        print(row[0], end="")
    cur.close()
    db.close()
