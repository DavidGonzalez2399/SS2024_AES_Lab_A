#ifndef MQTT_h
#define MQTT_h
#define PUBLISH_LED_PIN 6
#include "Arduino.h"
#include <ArduinoMqttClient.h>

MqttClient mqttClient(wifiClient);

const char broker[] = "test.mosquitto.org";
int        port     = 1883;
const char topic[]  = "box detection";
const char message[] = "box detected";

void connectToMQTTBroker(){

  if (!mqttClient.connect(broker, port)) {
    while (1);
  }

}

void publishMessage(){

  digitalWrite(PUBLISH_LED_PIN, HIGH);
  
  mqttClient.beginMessage(topic);
  mqttClient.print(message);
  mqttClient.endMessage();

  digitalWrite(PUBLISH_LED_PIN, LOW);

}

#endif