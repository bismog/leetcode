#!/usr/bin/env python
from mock import Mock
 
class Foo(object):
    _fooValue = 123
    def callFoo(self):
        print "Foo:callFoo_"
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
fooObj = Foo()
print fooObj # returns: <__main__.Foo object at 0x68550>
 
mockFoo = Mock(return_value = fooObj)
mockObj = mockFoo()
print mockObj # returns: <__main__.Foo object at 0x68550>
 
# working with the mocked instance
print mockObj._fooValue # returns: 123
mockObj.callFoo() # returns: Foo:callFoo_
mockObj.doFoo("narf") # returns: Foo:doFoo:input =  narf 
