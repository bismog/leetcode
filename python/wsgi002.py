#!/usr/bin/env python

from __future__ import print_function   
from wsgiref.simple_server import make_server     

def myapp(environ, start_response):       
    response_headers = [('content-type', 'text/plain')]     
    start_response('200 OK', response_headers)     
    return ['Check the headers!']     

class Middleware:     
    def __init__(self, app):         
        self.wrapped_app = app       
    def __call__(self, environ, start_response):           
        def custom_start_response(status, headers, exc_info=None):             
            headers.append(('X-A-SIMPLE-TOKEN', "1234567890"))             
            return start_response(status, headers, exc_info)           
        return self.wrapped_app(environ, custom_start_response)   

app = Middleware(myapp)   
httpd = make_server('', 8080, app) 
print("Starting the server on port 8080") 
httpd.serve_forever()
