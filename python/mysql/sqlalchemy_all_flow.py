#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('mysql://daisy:daisy@127.0.0.1:13306/test')


class Fruit(Base):
    __tablename__ = 'fruit'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    color = Column(String(50), nullable=False)

    def __init__(self, name, color):
        self.name = name
        self.color = color

# Create table
Fruit.metadata.create_all(engine)

# Create sqlalchemy session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
fruit1 = Fruit('apple', 'red')
fruit2 = Fruit('banana', 'yellow')
fruit3 = Fruit('grape', 'purple')
session.add(fruit1)
session.add(fruit2)
session.add(fruit3)
session.commit()

# Till now, we can get following data from table 'fruit':
# [<:>]# mysql test -h 127.0.0.1 -udaisy -pdaisy -P 13306 -se 'select * from fruit'
# id      name    color
# 1       apple   red
# 2       banana  yellow
# 3       grape   purple

# Query data inserted before
all_fruits = session.query(Fruit).all()
for fruit in all_fruits:
    print fruit.name, fruit.color
