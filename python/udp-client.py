#!/usr/bin/env python
#encoding=UTF-8

import socket
import sys

'''
def udpClient():
	address=('localhost',8080)
	udpClientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建socket
	while True:
		data=raw_input('>')
		if not data:
			break
		udpClientSocket.sendto(data,address) #发送数据
		data,addr=udpClientSocket.recvfrom(2048)
		print data
	 udpClientSocket.close()

if __name__==__main__:
	udpClient()
'''

reload (sys)
sys.setdefaultencoding('utf8')  
 
buffer_len = 2048
host="10.43.167.19"
port=12348
#udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
while True:
	data=raw_input("please input: ")
	if not data:
		break
	udp_socket.sendto(data,(host,port))                       #无需connect，直接通过主机ip和端口访问主机
	data,addr=udp_socket.recvfrom(buffer_len)
	print("receive ack from server:"+data.decode("UTF-8"))
udp_socket.close()

