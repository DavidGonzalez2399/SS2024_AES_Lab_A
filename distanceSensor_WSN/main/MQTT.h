#ifndef MQTT_h
#define MQTT_h
#define PUBLISH_LED_PIN 6
#include "Arduino.h"
#include <ArduinoMqttClient.h>

MqttClient mqttClient(wifiClient);

const char broker[] = "192.168.162.44";
int        port     = 1883;
const char publishingTopic[] = "BoxDetection";

void connectToMQTTBroker(){

  if (!mqttClient.connect(broker, port)) {
    while (1);
  }

  Serial.println("Connected to MQTT broker\n");

}

void publishMessage(String message){

  digitalWrite(PUBLISH_LED_PIN, HIGH);
  Serial.println("Publishing message ... \n");
  Serial.print(message);
  Serial.println();
  
  mqttClient.beginMessage(publishingTopic);
  mqttClient.print(message);
  mqttClient.endMessage();

  Serial.println("Published message \n");
  Serial.print(message);
  Serial.println();
  digitalWrite(PUBLISH_LED_PIN, LOW);

}

void subscribeToTopic(String subscribingTopic){

  Serial.print("Subscribing to topic: ");
  Serial.println(subscribingTopic);
  Serial.println();

  // subscribe to a topic
  mqttClient.subscribe(subscribingTopic);

  Serial.println("Subscribed to topic: \n");
  Serial.println(subscribingTopic);
  Serial.println();

}

void onMqttMessage(int messageSize) {
  // we received a message, print out the topic and contents
  Serial.println("Received a message with topic '");
  Serial.print(mqttClient.messageTopic());
  Serial.print("', length ");
  Serial.print(messageSize);
  Serial.println(" bytes:");

  // use the Stream interface to print the contents
  while (mqttClient.available()) {
    Serial.print((char)mqttClient.read());
  }
  Serial.println();
  Serial.println();

  publishMessage("0");

}

#endif