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

class IPBlacklistMiddleware(object):
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        ip_addr = environ.get('HTTP_HOST').split(':')[0]
        if ip_addr not in ('127.0.0.1'):
            start_response('403 Forbidden', [('Content-Type', 'text/plain')])
            return ['Forbidden']
        # return ['This is a animal applicaltion!\r\n']
        return self.application(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **local_conf):
        def _factory(application):
            return cls(application)
        return _factory

if __name__ == '__main__':
    application = loadapp('config:/home/git/leetcode/python/wsgi/api-paste_2.ini')
    server = eventlet.spawn(wsgi.server,
        eventlet.listen(('', 8080)), application)
    server.wait()


