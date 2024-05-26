import colorSensorClass
# import BlynkSetup
myColorSensor = ColorSensor(0,1,2,3,4)
while True:
    red= myColorSensor.measureRed()
    green = myColorSensor.measureGreen()
    blue = myColorSensor.measureBlue()
    # print(f'blue = {blue}')
    colors=[red,green,blue]
    result=myColorSensor.decide_color(red,green,blue)
    print(f'color is {result}')
    # BLYNK.virtual_write(0, result)
    # toggleBlynkLED(result)
    time.sleep(2)
    # BLYNK.run()