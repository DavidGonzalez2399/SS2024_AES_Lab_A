import machine
import time

# Define pin numbers for each motor
MOTOR1_PIN = 15
MOTOR2_PIN = 8
MOTOR3_PIN = 7
MOTOR5_PIN = 5
MOTOR6_PIN = 6

START_motor1 = 50
START_motor2 = 40
START_motor3 = 120
START_motor5 = 160
START_motor6 = 180

Conveyor_motor1 = 100
Conveyor_motor2 = 20
Conveyor_motor3 = 165
Conveyor_adjustment_motor3 = 140
Conveyor_motor5 = 110
Conveyor_motor6 = 90

# color sensor measuring
Color_motor1 = 0
Color_motor2 = 30
Color_motor3 = 160
Color_motor5 = 110
Color_motor6 = 90

#storing
Storing_motor1 = 180
Storing_motor2 = 30
Storing_motor3 = 150
Storing_motor5 = 110
Storing_motor6 = 180

# Initialize PWM objects for each motor
MOTOR1 = machine.PWM(machine.Pin(MOTOR1_PIN))
MOTOR2 = machine.PWM(machine.Pin(MOTOR2_PIN))
MOTOR3 = machine.PWM(machine.Pin(MOTOR3_PIN))
MOTOR5 = machine.PWM(machine.Pin(MOTOR5_PIN))
MOTOR6 = machine.PWM(machine.Pin(MOTOR6_PIN))

MOTOR1.freq(50)  # Set PWM frequency for all motors
MOTOR2.freq(50)  # Set PWM frequency for all motors
MOTOR3.freq(50)  # Set PWM frequency for all motors
MOTOR5.freq(50)
MOTOR6.freq(50)  # Set PWM frequency for all motors

#motor1
current_duty1 = 0
starting_duty_cycle=int(6553 / 180 * START_motor1 + 1638)

def duty_to_angle(angle, which_motor):
    
    duty_cycle = int(6553 / 180 * angle + 1638)
    
    if which_motor == 1:  
        # Motor 1 movement
        MOTOR1.duty_u16(duty_cycle)
    
    elif which_motor == 2:
        # Motor 2 movement
        MOTOR2.duty_u16(duty_cycle)
    elif which_motor == 3:
        # Motor 3 movement
        MOTOR3.duty_u16(duty_cycle)
    elif which_motor == 5:
        #Motor 5 movement
        MOTOR5.duty_u16(duty_cycle)
    elif which_motor == 6:
        # Motor 3 movement
        MOTOR6.duty_u16(duty_cycle)


def motor1(origin,destiny):
    # Move MOTOR3 forward from 120 to 180 degrees
    if origin < destiny:
        for i in range(origin, destiny, 1):
            duty_to_angle(i, 1)
            time.sleep_ms(20)
    elif destiny < origin:
        for i in range(origin, destiny, -1):
            duty_to_angle(i, 1)
            time.sleep_ms(20)
    
def motor2(origin,destiny):
    # Move MOTOR2 forward from 40 to 0 degrees
    if origin > destiny:
        for i in range(origin, destiny, -1):
            duty_to_angle(i, 2)
            time.sleep(0.09)
    elif destiny > origin:
        for i in range(origin, destiny, 1):
            duty_to_angle(i, 2)
            time.sleep(0.09)
def motor3(origin,destiny):
    # Move MOTOR3 forward from 120 to 180 degrees
    if origin < destiny:
        for i in range(origin, destiny, 1):
            duty_to_angle(i, 3)
            time.sleep_ms(20)
    elif destiny < origin:
        for i in range(origin, destiny, -1):
            duty_to_angle(i, 3)
            time.sleep_ms(20)

def motor6(destiny):
    # Move MOTOR4 forward from 180 to 100 degrees
    duty_to_angle(destiny, 6)
    time.sleep(1)
    
def motor5(origin,destiny):
    # Move MOTOR2 forward from 160 to 110 degrees
    if origin > destiny:
        for i in range(origin, destiny, -1):
            duty_to_angle(i, 5)
            time.sleep(0.09)
    elif destiny > origin:
        for i in range(origin, destiny, 1):
            duty_to_angle(i, 5)
            time.sleep(0.09)    

#grabing object from conveyor belt
motor1(START_motor1,Conveyor_motor1)
motor2(START_motor2,Conveyor_motor2)
motor3(START_motor3,Conveyor_motor3)
motor5(START_motor5,Conveyor_motor5)
motor6(Conveyor_motor6)
motor3(Conveyor_motor3,Conveyor_adjustment_motor3)
#measuring color
motor1(Conveyor_motor1,Color_motor1)
motor2(Conveyor_motor2,Color_motor2)
motor3(Conveyor_adjustment_motor3,Color_motor3)
motor5(Conveyor_motor5,Color_motor5)
motor6(Color_motor6)
#storing
motor1(Color_motor1,Storing_motor1)
motor2(Color_motor2,Storing_motor2)
motor3(Color_motor3,Storing_motor3)
motor5(Color_motor5,Storing_motor5)
motor6(Storing_motor6)
#going back to initial position
motor1(Storing_motor1,START_motor1)
motor2(Storing_motor2,START_motor2)
motor3(Storing_motor3,START_motor3)
motor5(Storing_motor5,START_motor5)