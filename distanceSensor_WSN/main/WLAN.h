#ifndef WLAN_h
#define WLAN_h
#include "Arduino.h"
#include <WiFiNINA.h>


WiFiClient wifiClient;

void connectToWifi(String ssid, String pass){

  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

}

#endif