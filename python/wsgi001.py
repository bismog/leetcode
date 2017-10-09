#!/usr/bin/env python

from __future__ import print_function
from wsgiref.simple_server import make_server
from urlparse import parse_qs

def myapp(environ, start_response):
     msg = 'No Message!'
     response_headers = [('content-type', 'text/plain')]
     start_response('200 OK', response_headers)
     qs_params = parse_qs(environ.get('QUERY_STRING'))       
     if 'msg' in qs_params:             
         msg = qs_params.get('msg')[0]       
     return ['Your message was: {}'.format(msg)]

app = myapp   
httpd = make_server('', 8080, app) 
print("Starting the server on port 8080") 
httpd.serve_forever()
