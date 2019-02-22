#!/usr/bin/env python

import pika
import sys

s_host = "10.21.19.254"
connection = pika.BlockingConnection(pika.ConnectionParameters(s_host))
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True)
message = ''.join((sys.argv[1:]) or "Hello World")
channel.basic_publish(exchange='',
    routing_key='hello',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2)
    )
print("Sent Hello World!")
connection.close()


