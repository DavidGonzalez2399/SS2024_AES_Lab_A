from machine import Pin
import time

#global variables to hold values accessed by interrupts
num_cycles=0
interrupt_flag=0


class ColorSensor:
    #initializing pins
    def __init__(self,S0,S1,S2,S3,S_out):
        self.S0=Pin(S0,Pin.OUT)
        self.S1=Pin(S1,Pin.OUT)
        self.S2=Pin(S2,Pin.OUT)
        self.S3=Pin(S3,Pin.OUT)
        self.S_out=Pin(S_out, Pin.IN, Pin.PULL_UP)
    #interrupt handler    
    def S_out_int(self,S_out):
        global interrupt_flag
        global num_cycles
        interrupt_flag=1
        num_cycles +=1
    # num cycles initialized as 0, recording start time, waiting until the interrupt is triggered 100 times, calculating the frequency by the time variance
    def measure_color(self):
        global num_cycles
        num_cycles =0
        start=time.ticks_us()
        self.S_out.irq(trigger=Pin.IRQ_FALLING,handler=self.S_out_int)
        while num_cycles<100:
            pass
        self.S_out.irq(trigger=Pin.IRQ_FALLING,handler=None)
        return (time.ticks_us()-start)/num_cycles
    
    #functions to set filter to measure different colors
    def measureRed(self):
        self.S2.low()
        self.S3.low()
        return self.measure_color()
    def measureGreen(self):
        self.S2.high()
        self.S3.high()
        return self.measure_color()
    def measureBlue(self):
        self.S2.low()
        self.S3.high()
        return self.measure_color()
    
    #compare color values to decide which is lowest
    def decide_color(self,red,green,blue):
        if red<blue:
            if red<green:
                return "red"
            else:
                return "green"
        else:
            if blue<green:
                return("blue")
            else:
                return("green")