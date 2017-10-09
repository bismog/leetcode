
from webob import Request
req = Request.blank('/article?id=1')
from pprint import pprint
req.environ
#{'wsgi.multithread': False, 'SCRIPT_NAME': '', 'wsgi.input': <_io.BytesIO object at 0x1c2e9b0>, 'REQUEST_METHOD': 'GET', 'HTTP_HOST': 'localhost:80', 'PATH_INFO': '/article', 'SERVER_PROTOCOL': 'HTTP/1.0', 'QUERY_STRING': 'id=1', 'wsgi.version': (1, 0), 'SERVER_NAME': 'localhost', 'wsgi.run_once': False, 'wsgi.errors': <open file '<stderr>', mode 'w' at 0x7f65073ce1e0>, 'wsgi.multiprocess': False, 'wsgi.url_scheme': 'http', 'SERVER_PORT': '80'}

