#!/usr/bin/env python

import pika

# These examples came from https://www.rabbitmq.com/getstarted.html
# and https://github.com/rabbitmq/rabbitmq-tutorials/tree/master/python

def callback(ch, method, properties, body):
    print(' Received %r' % body)

s_host = "10.21.19.254"
connection = pika.BlockingConnection(pika.ConnectionParameters(s_host))
channel = connection.channel()
channel.queue_declare(queue='hello')
# channel.basic_publish(exchange='',
#     routing_key='hello',
#     body='Hello World!')
# print("Sent Hello World!")
channel.basic_consume(callback,
    queue='hello',
    no_ack=True)
print('Waiting for messages, to exit press Ctrl+C')
channel.start_consuming()

# connection.close()
