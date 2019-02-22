#!/usr/bin/env python

import pika
import sys

s_host = '10.21.19.254'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=s_host))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                        exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print('Sent %r:%r' % (severity, message))
connection.close()
