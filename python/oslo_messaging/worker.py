#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
    print(' Received %r' % body)
    time.sleep(body.count(b'.'))
    print(" Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

s_host = "10.21.19.254"
connection = pika.BlockingConnection(pika.ConnectionParameters(s_host))
channel = connection.channel()
# channel.queue_declare(queue='hello')
channel.queue_declare(queue='hello', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
    queue='hello',
#    no_ack=True
    )
print('Waiting for messages, to exit press Ctrl+C')
channel.start_consuming()
