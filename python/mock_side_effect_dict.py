#!/usr/bin/env python
from mock import Mock
values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]
#mock.side_effect = side_effect
#mock('a'), mock('b'), mock('c') # return (1, 2, 3) respectively 
 
class Foo(object):
    _fooValue = 123
    def callFoo(self):
        print "Foo:callFoo_"
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue
 
fooObj = Foo()
#fooList = [665, 666, 667]
#mockFoo = Mock(return_value = fooObj, side_effect = fooList)
#fooTest = mockFoo()
#print fooTest # returns 665
#fooTest = mockFoo()
#print fooTest # returns 666
#fooTest = mockFoo()
#print fooTest # returns 667
#fooTest = mockFoo()
#print fooTest # raises: StopIteration


mock_xxx = Mock(return_value = fooObj, side_effect = side_effect)
ro = mock_xxx('a')
print ro# returns 1
ro = mock_xxx('c')
print ro# returns 3
ro = mock_xxx('b')
print ro# returns 2
ro = mock_xxx('d')
print ro# returns KeyError: 'd'
