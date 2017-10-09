#!/usr/bin/env python
#coding=UTF-8

import socket
from time import ctime

#def udpServer():
#    buffer=2048
#    #address=(127.0.0.1,8080)www.2cto.com
#    address=(127.0.0.1,8080)
#    udpsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#    udpsock.bind(address)
#    while True:
#        print "wait for message..."
#        data,addr=udpsock.recvfrom(buffer)
#        udpsock.sendto('[%s]%s' %(ctime(),data),addr)
#        print '...received from and retuned to:',addr
#    udpsock.close()
#if __name__==__main__:
#    udpServer()

buffer_len = 2048
udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #参数SOCK_DGRAM对应的是UDP协议                   
name=socket.gethostname()
port=12348
 
udp_socket.bind((name,port))
while True:
    print("wait for message...")
    data,addr=udp_socket.recvfrom(buffer_len)                       #与TCP的区别。因为不需要事先建立链接，因此需要获取客户端的地址，并随时按照地址发送消息
    print("receive message from "+str(addr))
    data=("\""+data.decode("UTF-8")+"\""+" at time "+ctime()).encode("UTF-8")
    print("i get msg:"+data.decode("UTF-8"))
    udp_socket.sendto(data,addr)                              #向客户端发送消息
udp_socket.close()

