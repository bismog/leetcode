#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('10.21.19.254'))
channel = connection.channel()
channel.queue_delete(queue='hello')
connection.close()
