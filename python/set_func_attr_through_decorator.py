#!/usr/bin/env python

def type(typev1, typev2):
    def decorator(f):
        f.xtype = typev1
        f.ytype = typev2
        return f
    return decorator

@type("xyz", "opq")
def ff():
    pass

attrx = getattr(ff, 'xtype', "abc")
attry = getattr(ff, 'ytype', "abc")
print attrx, attry
