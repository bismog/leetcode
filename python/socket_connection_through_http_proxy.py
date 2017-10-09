#!/usr/bin/python
import socket
import sys



headers = """GET / HTTP/1.1\r\n
Host: google.com\r\n\r\n"""



socket = socket

#host = "165.139.179.225" #proxy server IP
#host = "23.105.204.159" #proxy server IP
host = "127.0.0.1" #proxy server IP
#port = 80              #proxy server port
#port = 8484             #proxy server port
port = 13579             #proxy server port

try:
    import pdb;pdb.set_trace()
    s = socket.socket()
    s.connect((host,port))
    s.send(("CONNECT {0}:{1} HTTP/1.1\r\n" + "Host: {2}:    {3}\r\n\r\n").format(socket.gethostbyname(socket.gethostname()),1000,port,host))
    print s.recv(1096)
    s.send(headers)
    response = s.recv(1096)
    print response
    s.close()
except socket.error,m:
    print str(m)
    s.close()
    sys.exit(1)
