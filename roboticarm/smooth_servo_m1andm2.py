import machine
import time

# Define pin numbers for each motor
MOTOR1_PIN = 15
MOTOR2_PIN = 8
MOTOR3_PIN = 7

START_motor1 = 50
START_motor2 = 40 

RED_CONTAINER_motor1 = 135
RED_CONTAINER_motor2 = 30


GREEN_CONTAINER_motor1 = 160
GREEN_CONTAINER_motor2 = 20


# Initialize PWM objects for each motor
MOTOR1 = machine.PWM(machine.Pin(MOTOR1_PIN))
MOTOR2 = machine.PWM(machine.Pin(MOTOR2_PIN))
MOTOR3 = machine.PWM(machine.Pin(MOTOR3_PIN))

MOTOR1.freq(50)  # Set PWM frequency for all motors

#motor1
current_duty1 = 0
starting_duty_cycle=int(6553 / 180 * START_motor1 + 1638)
#motor2
current_duty2 = 0
starting_duty_cycle2=int(6553 / 180 * START_motor2 + 1638)

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
        if duty_cycle > current_duty2: 
            for i in range(starting_duty_cycle2, duty_cycle - 1):
                MOTOR2.duty_u16(i)
                time.sleep_ms(1)
            current_duty2 = duty_cycle
        elif duty_cycle < current_duty2:
            for i in range(current_duty2, duty_cycle - 1, -1):
                MOTOR2.duty_u16(i)
                time.sleep_ms(1)
            current_duty2 = duty_cycle


def motor1(angle):
    duty_to_angle(angle, 1)
    
def motor2(angle):
    duty_to_angle(angle, 2)


# Test your motor control functions
motor2(START_motor2)
motor1(GREEN_CONTAINER_motor1)
motor2(GREEN_CONTAINER_motor2)
motor1(START_motor1)
motor2(START_motor2)
