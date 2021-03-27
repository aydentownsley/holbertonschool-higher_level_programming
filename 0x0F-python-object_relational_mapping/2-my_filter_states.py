#!/usr/bin/python3
"""Lists all states starting with 'N'"""
import MySQLdb
import sys


if __name__ == "__main__":

    uname = sys.argv[1]
    pword = sys.argv[2]
    dbname = sys.argv[3]
    stname = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=uname, passwd=pword, db=dbname)

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE "
                "BINARY name='{}' ORDER BY id ASC"
                .format(stname))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
