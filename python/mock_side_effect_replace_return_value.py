#!/usr/bin/env python
from mock import Mock
 
class Foo(object):
    _fooValue = 123
    def callFoo(self):
        print "Foo:callFoo_"
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
fooObj = Foo()
#mockFoo = Mock(return_value = fooObj)
#mockObj = mockFoo()

mockFoo = Mock(return_value = fooObj, side_effect = StandardError)
mockObj = mockFoo() # raises: StandardError
