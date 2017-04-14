#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://dbuser:dbuser@localhost:5432/test')
DBSession = sessionmaker(engine)
session = DBSession()

BaseModel = delcarative_base()

class User(BaseModel):
    __tablename__ = 'userxxx'

    id = Column(String, primary_key=True)
    username = Column(String, index=True)

class Session(BaseModel):
    __tablename__ = 'session'

    id = Column(String, primary_key=True)
    suser = Column(String, index=True)
    ip = Column(String)

query = session.query(Session, User.username).join(User, User.id == Session.suser)
for i in query:
    print dir(i)

