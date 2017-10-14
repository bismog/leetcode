#!/usr/bin/env python
#-*- coding:utf-8 -*-

# https://www.codementor.io/sheena/understanding-sqlalchemy-cheat-sheet-du107lawl
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
# from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy import (Column, Integer, String, Boolean,
    ForeignKey, DateTime, Sequence, Float)
import datetime

Base = declarative_base()

# DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
engine = create_engine('mysql+mysqldb://projectxxx:projectxxx@127.0.0.1:13306/test?charset=utf8')
DBSession = sessionmaker(bind=engine)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, Sequence('book_seq'), primary_key=True)
    name = Column(String(50))
    # author_id = Column(Integer, ForeignKey('authors.id'))
    price = Column(Float)
    date_added = Column(DateTime, default=datetime.datetime.now)
    promote = Column(Boolean, default=False)

# Create Table
# Book.metadata.create_all(engine)

session = DBSession()

# # Inset table records
# book1 = Book(name='Ting ting traveling', price=19.8)
# book2 = Book(name='Youngers novel', price=29.5)
# session.add(book1)
# session.add(book2)
# session.commit()

# Query and interaction 
lbooks = session.query(Book)
for lbook in lbooks:
    print lbook.name, lbook.price

lbooks = session.query(Book).filter_by(price=29.5)
for lbook in lbooks:
    print lbook.name, lbook.price

lbooks = session.query(Book).filter(Book.price>20)
for lbook in lbooks:
    print lbook.name, lbook.price

from sqlalchemy import or_
lbooks = session.query(Book).filter(or_(Book.price<20,Book.name=='Youngers novel'))
for lbook in lbooks:
    print lbook.name, lbook.price


from sqlalchemy import desc
lbooks = session.query(Book).order_by(desc(Book.price))
for lbook in lbooks:
    print lbook.name, lbook.price

# Other useful methods
count = session.query(Book).count()
print 'We have at least %d books.' % count

book_a = session.query(Book).get(1)
print book_a.name, book_a.price

book_b = session.query(Book).get(2)
print book_b.name, book_b.price

book_first = session.query(Book).first()
print book_first.name, book_first.price
