#include "DistanceSensor.h"
#include "WLAN.h"
#include "MQTT.h"

#define TRIG_PIN 12
#define ECHO_PIN 11
#define WLAN_CONNECTED_LED_PIN 7
#define PUBLISH_LED_PIN 6
#define nearThresholdCms 18


//set interval for sending messages (milliseconds)
const long interval = 1000;
unsigned long previousMillis = 0;

DistanceSensor distanceSensor(TRIG_PIN, ECHO_PIN);


/*

  Algorithm

  1. Connect to WiFi
  2. Connect to MQTT broker
  3. Repeat
    3.1 Every 1 second, check if box is detected. If true, publish the message "box detected" "box detection"
    3.2 else, go back to step 3

*/

void setup() {
  
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  pinMode(WLAN_CONNECTED_LED_PIN, OUTPUT);
  pinMode(PUBLISH_LED_PIN, OUTPUT);

  connectToWifi();

  connectToMQTTBroker();
 

}



void loop() {

  if(!mqttClient.connected()){

    digitalWrite(WLAN_CONNECTED_LED_PIN, LOW);

    connectToWifi();

    connectToMQTTBroker();

  } else {

    digitalWrite(WLAN_CONNECTED_LED_PIN, HIGH);

    unsigned long currentMillis = millis();
  
    if(distanceSensor.isObjectDetected(nearThresholdCms) && currentMillis - previousMillis >= interval){

      // save the last time a message was sent
      previousMillis = currentMillis;

      publishMessage();
      // Serial.print(distanceSensor.getDistanceToObject());
      // Serial.println("\n");
      
    }

    // call poll() regularly to allow the library to send MQTT keep alive which
    // avoids being disconnected by the broker
    mqttClient.poll();

  }

  delay(100); 

}
