#include "WLAN.h"
#include "MQTT.h"

#define stepPin 2
#define dirPin 5 
#define WLAN_CONNECTED_LED_PIN 7
#define SUBSCRIBE_TO_COLOR_SENSOR_LED_PIN 5

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  pinMode(stepPin, OUTPUT); 
  pinMode(dirPin, OUTPUT);
  digitalWrite(dirPin, HIGH);

  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(WLAN_CONNECTED_LED_PIN, OUTPUT);
  pinMode(SUBSCRIBE_TO_COLOR_SENSOR_LED_PIN, OUTPUT);

  connectToWifi();

  connectToMQTTBroker();

  mqttClient.onMessage(onMqttMessage); // Set callback

  subscribeToTopic("BoxDetection");
  
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(dirPin, HIGH);
  digitalWrite(stepPin, HIGH); 
  delayMicroseconds(400); 
  digitalWrite(stepPin, LOW); 
  delayMicroseconds(400);
}

void loop() {
if (!mqttClient.connected()) {
    digitalWrite(LED_BUILTIN, LOW);
    connectToWifi();
    connectToMQTTBroker();
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(dirPin, HIGH);
    digitalWrite(stepPin, HIGH); 
    delayMicroseconds(400); 
    digitalWrite(stepPin, LOW); 
    delayMicroseconds(400);
  } else if (canContinue) {
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(dirPin, HIGH);
    digitalWrite(stepPin, HIGH); 
    delayMicroseconds(400); 
    digitalWrite(stepPin, LOW); 
    delayMicroseconds(400);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
    digitalWrite(dirPin, LOW);
    digitalWrite(stepPin, LOW); 
  }
  mqttClient.poll();
}
