import machine
import time




class Motor:
    def __init__(self,pin,start,conveyor,conveyor_adjustment,color,storing):
        self.pin=pin
        self.start=start
        self.conveyor=conveyor
        self.color=color
        self.storing=storing
        self.conveyor_adjustment=conveyor_adjustment
        self= machine.PWM(machine.Pin(self.pin))
        self.freq(50)
    def duty_to_angle(self,angle):
        duty_cycle = int(6553 / 180 * angle + 1638)
        machine.PWM(machine.Pin(self.pin)).duty_u16(duty_cycle)
    def move_motor(self,origin,destiny,wait_ms):
        if origin < destiny:
            for i in range(origin, destiny, 1):
                self.duty_to_angle(i)
                time.sleep_ms(wait_ms)
        elif destiny < origin:
            for i in range(origin, destiny, -1):
                self.duty_to_angle(i)
                time.sleep_ms(wait_ms)
    