#!/usr/bin/python3
'''
takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states\
                 JOIN cities ON states.id = \
                 cities.state_id WHERE states.name\
                 LIKE %s ORDER BY cities.id ASC", (argv[4],))
    tmp = ""
    for row in cur.fetchall():
        print("{:s}{:s}".format(tmp, row[0]), end="")
        tmp = ", "
    print()
    cur.close()
    db.close()
