import network
import time

def connectToWifi(SSID,password):
    wlan=network.WLAN(network.STA_IF) #setting up wireless standard
    wlan.active(True) # activating wifi
    wlan.connect(SSID,password)
    timeOutTimer=0

    while timeOutTimer<10 :
        if wlan.status() <0 or wlan.status()>=3: # if connection failed or succeeded stop the loop otherwise wait until timout runs out
            break
        print('waiting for connection')
        time.sleep(1)
        timeOutTimer += 1
    if wlan.status() !=3: # if connection failed
        raise RuntimeError('network connection failed')
    else: # if connection succeeded
        print("connected")
        wlan.ifconfig() 
        return wlan.ifconfig()[0] # return ip