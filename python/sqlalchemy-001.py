#!/usr/bin/env python

#from logging import logger
from sqlalchemy import create_engine

#e = create_engine("mysql://podm:podm@localhost/podm", connect_args={"encoding":"utf8", "port":3306})
e = create_engine("mysql://podm:podm@localhost/podm", connect_args={"charset":"utf8", "port":3306})
conn = e.connect()
result = conn.execute("select * from tmc")
#names = []
#for row in result:
#    names.append(row[0])
#print names
for row in result:
    print row
    #logger.debug(row)
