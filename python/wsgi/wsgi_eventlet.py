#!/usr/bin/env python
#-*- coding:utf-8 -*-
# http://wsfdl.com/openstack/2013/10/18/%E7%90%86%E8%A7%A3nova-api%E7%9A%84WSGI%E6%A1%86%E6%9E%B6.html
import eventlet
from eventlet import wsgi

class AnimalApplication(object):
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return ['This is a animal application!\r\n']


if __name__ == '__main__':
    application = AnimalApplication()
    wsgi.server(eventlet.listen(('', 8080)), application)
