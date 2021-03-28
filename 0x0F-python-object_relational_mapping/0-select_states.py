#!/usr/bin/python3
'''
Display all state in the database hbtn_0e_0_usa
'''


if __name__ == "__main__":
    import sys
    import MySQLdb

    argv = sys.argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
