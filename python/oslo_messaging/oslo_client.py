#!/usr/bin/env python

# coding: utf-8

# This example came from https://chrigl.de/posts/2014/08/27/oslo-messaging-example.html

from oslo.config import cfg
from oslo import messaging
import logging

logging.basicConfig()
log = logging.getLogger()

log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)

transport_url = 'rabbit://testing:test@10.21.19.254:5672/'
transport = messaging.get_transport(cfg.CONF, transport_url)

driver = 'messaging'

notifier = messaging.Notifier(transport, driver=driver, publisher_id='testing', topic='monitor')

notifier.info({'some': 'context'}, 'just.testing', {'heavy': 'payload'})
