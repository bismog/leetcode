#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import Person, Address, Base

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()

new_person = Person(name='new_person')
session.add(new_person)
session.commit()

new_address = Address(post_code='00000', person=new_person, street_name='Wall Street')
session.add(new_address)
session.commit()


