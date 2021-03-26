#!/usr/bin/python3
""" lists all states in database """
if __name__ == "__main__":
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                         passwd=password, db=db_name, charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
