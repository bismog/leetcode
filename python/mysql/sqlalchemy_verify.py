#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlalchemy_declarative import Person, Address, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.bind = engine
session = Session()
person_all = session.query(Person).all()
person = session.query(Person).first()
print "First person'name is %s" % person.name

related_address = session.query(Address).filter(Address.person == person).one()
print "Related address(postcode) is: %s" % related_address.post_code

