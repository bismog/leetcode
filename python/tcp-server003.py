#!/usr/bin/env python
import SocketServer,time
import sys
class Myserver(SocketServer.BaseRequestHandler):
    userinfo={'fan':'123','te':'234','fei':'345'}
    def handle(self):
        print 'Now connect form ',self.client_address[0]
        while True:
            recvdata=self.request.recv(1024)
            if not recvdata:
                continue
            elif recvdata=='Now client connect to Server':
                self.request.sendall('OK,I am ready')
            elif recvdata.startswith('username'):
                self.username=recvdata.split(':')[-1]
                if Myserver.userinfo.has_key(self.username):
                    self.request.sendall('valid')
                else:
                    self.request.sendall('invalid')
            elif recvdata.startswith('userpasswd'):
                self.userpasswd=recvdata.split(':')[-1]
                print self.userpasswd
                if Myserver.userinfo[self.username]==self.userpasswd:
                    self.request.sendall('valid')
                    time.sleep(0.5)
                    self.request.sendall('%s broken connect with server'%time.strftime("%Y-%m-%d %X", time.localtime()))
                    break
                else:
                    self.request.sendall('invalid')
        print "broken connect with %s"%self.client_address[0]   
if __name__=='__main__':
    try:
        srv=SocketServer.ThreadingTCPServer(('127.0.0.1',8123),Myserver)
        srv.serve_forever()
    except KeyboardInterrupt:
        print "CTRL+C,break"
        sys.exit()
