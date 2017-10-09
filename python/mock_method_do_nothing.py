#!/usr/bin/env python
from mock import Mock

class Foo(object):
    def callFoo(self):
        print "Foo:callFoo_"

mockFoo = Mock(spec = Foo)
mockFoo.callFoo()   # nothing happens, which is fine

