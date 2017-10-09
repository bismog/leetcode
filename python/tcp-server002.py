#!/usr/bin/env python 
#encoding=UTF-8

#from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH) 
#from time import ctime 
import SocketServer
#from SocketServer import *
from time import ctime

#HOST = '' 
#PORT = 21567 
#ADDR = (HOST, PORT) 
# 
#class MyRequestHandler(SRH): 
#    def handle(self): 
#        print '...connected from:', self.client_address 
#        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline())) 
#        tcpServ = TCP(ADDR, MyRequestHandler) 
#        print 'waiting for connection...' 
#        tcpServ.serve_forever() 


class MyRequestHandler(SocketServer.StreamRequestHandler): 
        
    '''在 BaseRequest 类中，这个函数什么也不做: 
    def handle(self): 
        pass 
    在有客户消息进来的时候，handle()函数就会被调用。'''
    def handle(self): 
        print '...connected from:', self.client_address[0] 
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline())) 

if __name__=="__main__":
    srv = SocketServer.TCPServer(("10.43.167.19", 8080), MyRequestHandler) 
    print 'waiting for connection...' 
    srv.serve_forever()
