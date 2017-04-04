#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://wsfdl.com/python/2013/10/14/%E7%90%86%E8%A7%A3WSGI%E6%A1%86%E6%9E%B6.html

from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['This is a python application!\n']

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8080, application)
    server.serve_forever()
