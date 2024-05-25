import machine
import time

# Define pin numbers for each motor
MOTOR1_PIN = 15
MOTOR2_PIN = 8
MOTOR3_PIN = 7
MOTOR4_PIN = 6

START_motor1 = 50
START_motor2 = 40
START_motor3 = 120
START_motor4 = 180

RED_CONTAINER_motor1 = 135
RED_CONTAINER_motor2 = 30


GREEN_CONTAINER_motor1 = 160
GREEN_CONTAINER_motor2 = 10
GREEN_CONTAINER_motor3 = 140
GREEN_CONTAINER_motor4 = 70


# Initialize PWM objects for each motor
MOTOR1 = machine.PWM(machine.Pin(MOTOR1_PIN))
MOTOR2 = machine.PWM(machine.Pin(MOTOR2_PIN))
MOTOR3 = machine.PWM(machine.Pin(MOTOR3_PIN))
MOTOR4 = machine.PWM(machine.Pin(MOTOR4_PIN))

MOTOR1.freq(50)  # Set PWM frequency for all motors
MOTOR2.freq(50)  # Set PWM frequency for all motors
MOTOR3.freq(50)  # Set PWM frequency for all motors
MOTOR4.freq(50)  # Set PWM frequency for all motors

#motor1
current_duty1 = 0
starting_duty_cycle=int(6553 / 180 * START_motor1 + 1638)

def duty_to_angle(angle, which_motor):
    global current_duty1, starting_duty_cycle, current_duty2, starting_duty_cycle2
    
    duty_cycle = int(6553 / 180 * angle + 1638)
    
    if which_motor == 1:  
        # Motor 1 movement
        if duty_cycle > current_duty1: 
            for i in range(starting_duty_cycle, duty_cycle, 1):
                MOTOR1.duty_u16(i)
                time.sleep_ms(1)
            current_duty1 = duty_cycle
        elif duty_cycle < current_duty1:
            for i in range(current_duty1, duty_cycle, -1):
                MOTOR1.duty_u16(i)
                time.sleep_ms(1)
            current_duty1 = duty_cycle
    
    elif which_motor == 2:
        # Motor 2 movement
        MOTOR2.duty_u16(duty_cycle)
    elif which_motor == 3:
        # Motor 3 movement
        MOTOR3.duty_u16(duty_cycle)
    elif which_motor == 4:
        # Motor 3 movement
        MOTOR4.duty_u16(duty_cycle)


def motor1(angle):
    duty_to_angle(angle, 1)
    
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
def motor4(destiny):
    # Move MOTOR4 forward from 180 to 100 degrees
    duty_to_angle(destiny, 4)
    time.sleep(1)
    

# Test your motor control functions
motor1(START_motor1)
motor1(GREEN_CONTAINER_motor1)
motor2(START_motor2,GREEN_CONTAINER_motor2)
motor3(START_motor3,GREEN_CONTAINER_motor3)
motor4(GREEN_CONTAINER_motor4)
motor1(START_motor1)
motor4(START_motor4)
motor3(GREEN_CONTAINER_motor3,START_motor3)
motor2(GREEN_CONTAINER_motor2,START_motor2)