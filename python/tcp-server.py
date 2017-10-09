#!/usr/bin/env python
#encoding=UTF-8
import socket
from time import ctime
def tcp_server():
    #address=("127.0.0.1",8080)
    address=("10.43.167.19",8080)
    #初始化socket
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定端口地址
    tcp_server_socket.bind(address)
    #设置监听
    tcp_server_socket.listen(5)
    while True:
        print "wait a client connect..."
        #接受客户端连接
        con,addr=tcp_server_socket.accept()
        while True:
            try:
                con.settimeout(20)
                #接收数据
                buf =con.recv(1024)
#                 con.send('[%s]%s' %(ctime(),buf))
                if buf=="1":
                    con.send("1")
                elif buf=="2":
                    con.send("2")
                elif buf=="3":
                    con.send("3")
                    break
                else:
                    con.send("unknow command")
            except socket.timeout:
                print "time out"
        con.close()
        print "a client exit..."

if __name__=="__main__":
    tcp_server()
