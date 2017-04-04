#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://wsfdl.com/openstack/2013/10/18/%E7%90%86%E8%A7%A3nova-api%E7%9A%84WSGI%E6%A1%86%E6%9E%B6.html
# More about paste.ini configuration: http://www.choudan.net/2013/07/28/OpenStack-paste-deploy%E4%BB%8B%E7%BB%8D.html
import eventlet
from eventlet import wsgi
from paste.deploy import loadapp

class AnimalApplication(object):
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return ['This is a animal applicaltion!\r\n']

    @classmethod
    def factory(cls, global_conf, **kwargs):
        return cls()

if __name__ == '__main__':
    application = loadapp('config:/home/git/leetcode/python/wsgi/api-paste.ini')
    server = eventlet.spawn(wsgi.server,
        eventlet.listen(('', 8080)), application)
    server.wait()
