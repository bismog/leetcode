#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlalchemy import create_engine, text, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column(String)
    count = Column(Integer)

    def __repr__(self):
        return "<Product(id='%d', name='%s', count='%d')>"%(self.id, self.name, self.count)
     
# DB_CON_STR = 'mysql+mysqldb://projectxxx:projectxxx@127.0.0.1:13306/test?charset=utf8'
# engine = create_engine(DB_CON_STR, echo=False)
engine = create_engine('mysql+mysqldb://projectxxx:projectxxx@127.0.0.1:13306/test?charset=utf8')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# res = session.query(Product).filter(text("id=1")).one()
# print res.id, res.name, res.count

# via sql clause
sql = text("select name from products")
res = session.execute(sql).fetchall()

for row in res:
    for col in row:
        print col,
    print
