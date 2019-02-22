#!/usr/bin/env python

import pika

def callback(ch, method, properties, body):
    print('%r ' % body)

s_host = '10.21.19.254'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=s_host))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

print('Waiting for logs, to exit press Ctrl+C')

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
