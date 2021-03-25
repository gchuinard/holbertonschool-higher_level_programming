#!/usr/bin/python3
'''
Display all state in the database hbtn_0e_0_usa
'''


if __name == "__main__":
    import sys
    import MySQLdb

    argv = sys.argv
    db = MySQLdb.connect(host=localhost,
                         user=root,
                         passwd=root,
                         db=hbtn_0e_0_usa)
    cur = db.cursor()
    cur.execute(SELECT * states ORD by id ASC)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
