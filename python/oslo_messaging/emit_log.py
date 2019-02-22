#!/usr/bin/env python

import pika
import sys

s_host = "10.21.19.254"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=s_host))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
message = ''.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message
                     )
print(" Sent %r" % message)
connection.close()
