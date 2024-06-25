from blynklib import Blynk
from connectToWifiLib import connectToWifi
import constants
#connectToWifi(constants.SSID,constants.SSID_password)
BLYNK = Blynk(constants.BLYNK_AUTH_TOKEN)
def ShowColorReading(result):
        BLYNK.virtual_write(1,0)
        BLYNK.virtual_write(2,0)
        BLYNK.virtual_write(3,0)
        if result =='red':
              BLYNK.virtual_write(0,'Red')
        elif result == 'green':
              BLYNK.virtual_write(0,'Green')
        else:
              BLYNK.virtual_write(0,'Blue')
def showBoxDetected(boxDetected):
    BLYNK.virtual_write(1,boxDetected)
def showconveyerBeltState(conveyerBeltState):
    BLYNK.virtual_write(3,boxDetected)
def showRoboticArmState(RoboticArmState):
    BLYNK.virtual_write(2,RoboticArmState)