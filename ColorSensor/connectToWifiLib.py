import network
import time

def connectToWifi(SSID,password):
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID,password)
    timeOutTimer=0

    while timeOutTimer<10 :
        if wlan.status() <0 or wlan.status()>=3:
            break
        print('waiting for connection')
        time.sleep(1)
        timeOutTimer += 1
    if wlan.status() !=3:
        raise RuntimeError('network connection failed')
    else:
        print("connected")
        wlan.ifconfig()
        return wlan.ifconfig()[0]