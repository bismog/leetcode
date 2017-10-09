#!/usr/bin/env python
from mock import Mock
mockFoo = Mock(name = "Foo")   # create the mock object
print mockFoo                  # returns: <Mock name='Foo' id='494864'>
print repr(mockFoo)            # still returns: <Mock name='Foo' id='494864'>
