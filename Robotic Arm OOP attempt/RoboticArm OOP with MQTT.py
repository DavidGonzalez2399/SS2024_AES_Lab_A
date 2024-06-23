from motor_class import Motor, most_common
from mqtt_receive import makeConnection,subscribe
from mqtt_send import publish
import time

readings=[]
conveyerBelt_message=0

def colorSensor_callback(topic, response):
    global readings
    readings.append(response)
    return response
def conveyerbelt_callback(topic,response):
    global conveyerBelt_message
    
    if response==b'1':
        conveyerBelt_message=1
    print(f'response is {response} flag is {conveyerBelt_message}')

client = makeConnection()

motor1_wait_ms=20
motor2_wait_ms=50
motor3_wait_ms=20
motor5_wait_ms=10
motor6_wait_ms=1 

motor_wait_list=[motor1_wait_ms,motor2_wait_ms,motor3_wait_ms,motor5_wait_ms,motor6_wait_ms]
motor1 = Motor(15,101,101,101,0,180,101,0)
motor2 = Motor(8,40,12,12,35,30,15,35)
motor3 = Motor(7,150,164,140,183,150,164,150)
motor5 = Motor(5,155,110,120,106,110,105,110)
motor6 = Motor(6,180,60,60,60,180,180,60)

motor_list=[motor1,motor2,motor3,motor5,motor6]
client.set_callback(conveyerbelt_callback)
subscribe('ConveyorBeltReading', client)
while 1:
    
    client.check_msg()
    while conveyerBelt_message==1:
        for i in range(len(motor_list)):
            motor_list[i].move_motor(motor_list[i].start,motor_list[i].conveyor,motor_wait_list[i])
        #motor3.move_motor(motor3.conveyor,motor3.conveyor_adjustment,motor3_wait_ms)
        #motor3.conveyor=motor3.conveyor_adjustment
        for i in range(len(motor_list)):
            motor_list[i].move_motor(motor_list[i].conveyor,motor_list[i].conveyor_adjustment,motor_wait_list[i])

        for i in range(len(motor_list)):
            motor_list[i].move_motor(motor_list[i].conveyor_adjustment,motor_list[i].color,motor_wait_list[i])

        client.set_callback(colorSensor_callback)
        subscribe('ColorSensorReading', client)
        start=time.ticks_ms()
        end=time.ticks_ms()
        while end-start<5000:
           time.sleep(0.5)
           client.check_msg()
           end=time.ticks_ms()
        result = most_common(readings)
        print(result)
        if result == b'blue':
            for i in range(len(motor_list)):
                motor_list[i].move_motor(motor_list[i].color,motor_list[i].storing,motor_wait_list[i])
            for i in range(len(motor_list)):    
                motor_list[i].move_motor(motor_list[i].storing,motor_list[i].start,motor_wait_list[i])
        else:
            for i in range(len(motor_list)):
                motor_list[i].move_motor(motor_list[i].color,motor_list[i].returnbox_adjustment,motor_wait_list[i])
            for i in range(len(motor_list)):
                motor_list[i].move_motor(motor_list[i].returnbox_adjustment,motor_list[i].returnbox,motor_wait_list[i])
            for i in range(len(motor_list)):
                motor_list[i].move_motor(motor_list[i].returnbox,motor_list[i].start,motor_wait_list[i])
        readings=[]
        publish('RoboticArm','1',client)
        client.set_callback(conveyerbelt_callback)
        subscribe('ConveyorBeltReading', client)
        conveyerBelt_message=0

