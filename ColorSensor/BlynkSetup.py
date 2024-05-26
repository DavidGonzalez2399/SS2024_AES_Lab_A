from blynklib import Blynk
from connectToWifiLib import connectToWifi
import constants
connectToWifi(constants.SSID,constants.password)
BLYNK = Blynk(constants.BLYNK_AUTH_TOKEN)
def toggleBlynkLED(result):
        BLYNK.virtual_write(1,0)
        BLYNK.virtual_write(2,0)
        BLYNK.virtual_write(3,0)
        if result =='red':
              BLYNK.virtual_write(1,1)
        elif result == 'green':
              BLYNK.virtual_write(2,1)
        else:
              BLYNK.virtual_write(3,1)