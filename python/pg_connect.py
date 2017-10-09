#!/usr/bin/env python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='cmldb' user='postgres' host='localhost' password='postgres'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

#insert a tuple
cur.execute("""insert into userlist(name, sign) values('peng','2015-09-09')""")
#insert a couple of tuples
more_user = ({'username':'zhatao','signature':'2015-09-09'}, 
             {"username":'wenhan','signature':"2015-09-09"}, 
             {"username":'wenquan',"signature":"2015-09-09"})
try:
    cur.executemany("""insert into userlist(name, sign) values(%(username)s, %(signature)s)""", more_user)
except:
    print "insert failed"
#show tuples
cur.execute("""select * from userlist""")
table_userlist = cur.fetchall()
print "Show me the databases:"
for row in table_userlist:
    print "   ", row[0]

#try delete tuple with follow names
try:
    cur.execute("""delete from userlist where name='peng'""")
    cur.execute("""delete from userlist where name='zhatao'""")
    cur.execute("""delete from userlist where name='wenhan'""")
    cur.execute("""delete from userlist where name='wenquan'""")
except:
    print "delete failed"

#show tuples
cur.execute("""select * from userlist""")
table_userlist = cur.fetchall()
print "Show me the databases:"
for row in table_userlist:
    print "   ", row[0]

conn.commit()

