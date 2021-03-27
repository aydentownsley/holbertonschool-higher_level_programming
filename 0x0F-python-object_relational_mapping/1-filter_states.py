#!/usr/bin/python3
"""Lists all states starting with 'N'"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    uname = sys.argv[1]
    pword = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=uname,
                         passwd=pword, db=dbname, charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE "
                "name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
