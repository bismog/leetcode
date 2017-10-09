#!/usr/bin/env python

def f(n, x): # these `n`, `x` have nothing to do with `n` and `x` from main()
    n = 2    # put `n` label on `2` balloon
    x.append(4) # call `append` method of whatever object `x` is referring to.
    print 'In f():', n, x
    x = []   # put `x` label on `[]` ballon, but has no effect on the original list 
    #del x
    x.append(999)
    
_n=1
_x=[1,3,'a','xxx']
f(_n,_x)
print _n, _x
