import time

#importing color sensor class
from colorSensorClass import ColorSensor

#importing MQTT functions
from mqtt_send import makeConnection,publish

#creating MQTT client
client=makeConnection()
mqttTopic = "ColorSensorReading"

#initializing Color sensor
myColorSensor = ColorSensor(0,1,2,3,4)

while True:
    red= myColorSensor.measureRed()
    green = myColorSensor.measureGreen()
    blue = myColorSensor.measureBlue()
    colors=[red,green,blue]
    result=myColorSensor.decide_color(red,green,blue)
    print([red,green,blue])
    publish(mqttTopic,result,client)
    time.sleep(0.5)