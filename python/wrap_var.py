#!/usr/bin/env python
# -*- coding:utf-8 -*-

def _wrap_dict(v):                                                                                                                                                                                        
    for k in v.keys():                                                                                                                                                                                    
        if v[k] is not None:                                                                                                                                                                              
            v[wrap_var(k)] = wrap_var(v[k])                                                                                                                                                               
    return v                                                                                                                                                                                              
                                                                                                                                                                                                          
                                                                                                                                                                                                          
def _wrap_list(v):                                                                                                                                                                                        
    for idx, item in enumerate(v):                                                                                                                                                                        
        if item is not None:                                                                                                                                                                              
            v[idx] = wrap_var(item)                                                                                                                                                                       
    return v                                                                                                                                                                                              
                                                                                                                                                                                                          
                                                                                                                                                                                                          
def wrap_var(v):                                                                                                                                                                                          
    if isinstance(v, dict):                                                                                                                                                                               
        v = _wrap_dict(v)                                                                                                                                                                                 
    elif isinstance(v, list):                                                                                                                                                                             
        v = _wrap_list(v)                                                                                                                                                                                 
    else:                                                                                                                                                                                                 
        if v is not None and not isinstance(v, AnsibleUnsafe):                                                                                                                                            
            v = UnsafeProxy(v)                                                                                                                                                                            
    return v

