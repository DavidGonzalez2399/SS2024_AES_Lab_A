from mqtt_receive import makeConnection,subscribe,mqttConnect

from BlynkSetup import BLYNK, 

#creating MQTT client
client=makeConnection()

result=''
boxDetected=0
conveyerBeltState=0
roboticArmState=0

def colorSensorCallback(topic,response):
    global result
    response = response.decode("utf-8")
    print(f'color sensor = {response}')
    result = response
    BLYNK.virtual_write(0,response)
def boxDetectionCallback(topic,response):
    global boxDetected
    if response==b'1': 
        boxDetected=1
    else:
        boxDetected=0
    BLYNK.virtual_write(1,boxDetected)
    print(f'box detection = {boxDetected}')
def conveyerBeltCallback(topic,response):
    global conveyerBeltState
    if response==b'1': 
        conveyerBeltState=1
    else:
        conveyerBeltState=0
    
    BLYNK.virtual_write(3,conveyerBeltState)
    
def roboticArmCallback(topic,response):
    global roboticArmState
    if response==b'1': 
        roboticArmState=1
    else:
        roboticArmState=0
    roboticArmState=response
    BLYNK.virtual_write(2,roboticArmState)
    
while 1:
    client.set_callback(colorSensorCallback)
    subscribe('colorSensorReading', client)
    client.check_msg()
    client.check_msg()
    subscribe('BoxDetection', client)
    client.set_callback(boxDetectionCallback)
    client.check_msg()
    BLYNK.run()