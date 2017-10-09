#!/usr/bin/env python
from mock import Mock
 
class Foo(object):
    _fooValue = 123
    def callFoo(self):
        print "Foo:callFoo_"
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
fooObj = Foo()
fooList = [665, 666, 667]
mockFoo = Mock(return_value = fooObj, side_effect = fooList)
 
fooTest = mockFoo()
print fooTest # returns 665
fooTest = mockFoo()
print fooTest # returns 666
fooTest = mockFoo()
print fooTest # returns 667
fooTest = mockFoo()
print fooTest # raises: StopIteration
