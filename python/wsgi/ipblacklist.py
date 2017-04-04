#!/usr/bin/env python
#-*- coding:utf-8 -*-

class IPBlacklistMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        import pdb;pdb.set_trace()
        ip_addr = environ.get('HTTP_HOST').split(':')[0]
        if ip_addr not in ('127.0.0.1'):
            return forbidden(start_response)

        return self.app(environ, start_response)


def forbidden(start_response):
    start_response('403 Forbidden', [('Content-Type', 'text/plain')])
    return ['Forbidden']


def application(environ, start_response):
    import pdb;pdb.set_trace()
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['This is a python application!']


if __name__ == '__main__':
    import pdb;pdb.set_trace()
    from wsgiref.simple_server import make_server
    app = IPBlacklistMiddleware(application)
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
