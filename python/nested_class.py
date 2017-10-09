#!/usr/bin/env python

class A:
    class B:
        def __init__(self):
            print 'class b __init__'
            self.x = 0

    def __init__(self):
        print 'class a __init__'
        self.y = 0

aa = A()
ab = A.B()
print aa.y
print ab.x
