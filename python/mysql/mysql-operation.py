#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb

try:
    # conn = MySQLdb.connect(user='daisy', passwd='daisy', host='localhost', port=13306)
    conn = MySQLdb.connect(user='daisy', passwd='daisy', host='127.0.0.1', port=13306)
except MySQLdb.ERROR as e:
    print "connect mysql failed."
    exit(1)
conn.select_db('daisy')
cur = conn.cursor()


def insertdb():
    pass

def selectdb():
    # sql = 'select * from components'
    # exsql = sql % ('python')
    # count = cur.execute(exsql)
    count = cur.execute('select * from components')
    # for row in cur:
    #     print row
    result = cur.fetchall()
    print result
    cur.close()
    conn.close()

selectdb()
