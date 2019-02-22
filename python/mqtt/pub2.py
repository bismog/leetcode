#!/usr/bin/env python

import paho.mqtt.client as mqtt

client = mqtt.Client()

broker = "myvm2" 
port = 1883
keepalive = 60
client.connect(broker, port, keepalive)

client.publish("onelittleboy", payload="doyoulikesomecandy?")

client.disconnect()
