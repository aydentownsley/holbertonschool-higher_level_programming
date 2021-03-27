#!/usr/bin/python3
"""Lists all states starting with 'N'"""
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
    cur.execute("SELECT * FROM states WHERE "
                "BINARY name='{}' ORDER BY id ASC"
                .format(stname))
    print(cur.fetchone())
    cur.close()
    db.close()
