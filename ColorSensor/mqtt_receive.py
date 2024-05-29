import network
import time
from umqtt.simple import MQTTClient
import constants
from connectToWifiLib import connectToWifi

#setting up mqtt parameters
mqttBroker = constants.mqttBroker
mqttClient = constants.mqttClient
mqttUser = constants.mqttUser
mqttPW = constants.mqttPW

#setting up the client 
def mqttConnect():
    client = MQTTClient(mqttClient, mqttBroker, keepalive=60)
    client.connect()
    print('MQTT connected')
    return client

def makeConnection():
    connectToWifi(constants.SSID,constants.SSID_password)
    return mqttConnect()

#what to do once a message is received
def my_callback(topic, response):
    print(response)
    pass

#defining subscription function
def subscribe(topic, client):
    client.subscribe(topic)
    print("Subscribe Done")
    
## Add the following code section to the subscriber code
'''
client = makeConnection()
client.set_callback(my_callback)
subscribe('/color', client)
while True:
   time.sleep(0.5)
   client.check_msg()
'''