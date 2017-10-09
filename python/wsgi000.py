#!/usr/bin/env python

from __future__ import print_function
from wsgiref.simple_server import make_server
import pdb

def myapp(environ, start_response):
     pdb.set_trace()
     msg = 'No Message!'
     response_headers = [('content-type', 'text/plain')]
     start_response('200 OK', response_headers)
     return ['Hello World!']

app = myapp   
httpd = make_server('', 8090, app) 
print("Starting the server on port 8090") 
httpd.serve_forever()

