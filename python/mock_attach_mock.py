#!/usr/bin/env python
from mock import Mock
class Foo(object):
    _fooValue = 123
    def callFoo(self):
        print "Foo:callFoo_"
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
class Bar(object):
    _barValue = 456
    def callBar(self): pass
    def doBar(self, argValue): pass
 
mockFoo = Mock(spec = Foo)
print mockFoo # returns <Mock spec='Foo' id='507120'>
mockBar = Mock(spec = Bar)
print mockBar # returns: <Mock spec='Bar' id='2784400'>
mockFoo.attach_mock(mockBar, 'fooBar')# attach the second mock to the first
print mockFoo # returns: <Mock spec='Foo' id='495312'>
print mockFoo._fooValue # returns: <Mock name='mock._fooValue' id='428976'>
print mockFoo.callFoo()
print mockFoo.fooBar #returns: <Mock spec='Bar' id='2784400'>
print mockFoo.fooBar._barValue # returns: <Mock name='mock.fooBar._barValue' id='2788016'>
print mockFoo.fooBar.callBar() # returns: <Mock name='mock.fooBar.callBar()' id='2819344'>
print mockFoo.fooBar.doBar("narf") # returns: <Mock name='mock.fooBar.doBar()' id='4544528'>
