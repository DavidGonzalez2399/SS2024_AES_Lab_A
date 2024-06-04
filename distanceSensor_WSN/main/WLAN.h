#ifndef WLAN_h
#define WLAN_h
#include "Arduino.h"
#include <WiFiNINA.h>

char ssid[] = "Galaxy S23 Ultra 00AC";        // your network SSID (name)
char pass[] = "Germany.4";    // your network password (use for WPA, or use as key for WEP)

WiFiClient wifiClient;

void connectToWifi(){

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