#!/usr/bin/env python
#encoding=UTF-8
import socket

def tcp_client():
    address=("127.0.0.1",8080)
    #初始化socket
    #xxx_socket=socket(AF_INET, SOCK_STREAM)
    tcp_client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #建立连接
    tcp_client_socket.connect(address)
    while True:
        #input data
        data=raw_input("input data:")
        #send request
        tcp_client_socket.send(data)
        print "receive ack:"+tcp_client_socket.recv(1024)
        if data==3:
            break
    tcp_client_socket.close()

if __name__=="__main__":
    tcp_client()

