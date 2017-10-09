#!/usr/bin/env python

class U(object):
    def __init__(self):
        self.__contains__ = '888'
        self.__contas = '000'
        self._U__contas = 'balabala'
        print 'right here'
    def __you_cannot_see_me(self):
        print 'wow, you can see me'
    def _U__you_cannot_see_me(self):
        print 'how could you get it?'

u = U()
print u.__contains__
print u._U__contas
#u.__you_cannot_see_me()
u._U__you_cannot_see_me()
u.vxvx = 123
print u.vxvx
