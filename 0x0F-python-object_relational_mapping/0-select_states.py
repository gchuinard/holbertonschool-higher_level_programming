#!/usr/bin/python3
'''
Display all state in the database hbtn_0e_0_usa
'''


if __name == "__main__":
import sys
import MySQLdb

argv = sys.argv
db = MySQLdb.connect(host=localhost, user=root, passwd=root, db=hbtn_0e_0_usa)
cur = db.cursor()
states = cur.execut(SELECT * `states` ORD by `id` ASC)
print "Selected %s states" % states
print "Selected %s rows" % cur.rowcount
# Close all cursors
cur.close()
# Close all databases
db.close()

