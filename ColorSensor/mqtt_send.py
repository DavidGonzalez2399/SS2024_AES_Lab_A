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

#defining publish function
def publish(topic,value,client):
        try:
            client.publish(topic, value)
            print(f"sent value {value} to topic {topic}")
        except OSError:
            print()
            print('Error: MQTT connection failed')
            






