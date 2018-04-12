#!/usr/bin/python

#=======================================================
# Program name: test_mqtt.py
# Desc: A simple test to connect a publisher MQTT
#       to a subscriber MQTT. Enter your IP address
#       in MY_IP and enter the broker IP address
#       for BROKER_IP
#
# Author: HARPi
# Date: 11.04.2018
#=======================================================

# Importing child_mqtt package
from child_mqtt import child_mqtt

NAME = "Test publisher"
TOPIC = "test/topic"
#MY_IP = "<ENTER_YOUR_IP_ADDRESS>"
#BROKER_IP = "<ENTER_BROKER_IP_ADDRESS>"
MY_IP = "192.168.1.187"
BROKER_IP = "192.168.1.176"
DESC = "A test description"

# You don't need to change this
child = child_mqtt(NAME, TOPIC, BROKER_IP, MY_IP, DESC)

print("I am %s" %child.get_name())
print("My topic is %s" %child.get_topic())
print("My IP address is %s" %child.get_ip())
print("I am publishing to %s" %child.get_broker_ip())

child.send_msg("Hello other MQTT")
child.send_msg("Did you receive my message?")
child.send_msg("Disconnecting from %s" %child.get_broker_ip())
child.disconnect()