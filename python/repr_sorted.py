#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://www.thegeekstuff.com/2014/06/python-sorted/

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<name: %s, age: %s>" % (self.name, self.age)

def byname(person):
    return person.name

def byage(person):
    return person.age

jack = Person('Jack', 19)
adam = Person('Adam', 43)
becky = Person('Becky', 11)
people = [jack, adam, becky]

print(sorted(people))
print(sorted(people, key=byname))
print(sorted(people, key=byage))

