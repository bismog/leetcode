#!/usr/bin/env python

def permission(ptype):
    def decorator(f):
        f.role = ptype
        return f
    return decorator

@permission("admin")
def do_x():
    pass

@permission("normal_user")
def do_y():
    pass

@permission("guest")
def do_z():
    pass

role_x = getattr(do_x, 'role', "guest")
role_y = getattr(do_y, 'role', "guest")
role_z = getattr(do_z, 'role', "guest")
print role_x, role_y, role_z
