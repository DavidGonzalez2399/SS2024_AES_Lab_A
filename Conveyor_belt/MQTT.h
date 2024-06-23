#ifndef MQTT_h
#define MQTT_h
#define PUBLISH_LED_PIN 6
#include "Arduino.h"
#include <ArduinoMqttClient.h>

char broker[] = "192.168.214.44";
int port = 1883;

unsigned int canContinue = 1;

MqttClient mqttClient(wifiClient);

void connectToMQTTBroker(){

  if (!mqttClient.connect(broker, port)) {
    while (1);
  }

  Serial.println("Connected to MQTT broker\n");

}

void publishMessage(String message, String topic){

  digitalWrite(PUBLISH_LED_PIN, HIGH);
  Serial.println("Publishing message ... \n");
  Serial.print(message);
  Serial.println();
  
  mqttClient.beginMessage(topic);
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
  Serial.println("Received a message with topic '");
  Serial.print(mqttClient.messageTopic());
  Serial.print("', length ");
  Serial.print(messageSize);
  Serial.println(" bytes:");

  String message = "";
  while (mqttClient.available()) {
    char c = (char)mqttClient.read();
    message += c;
    Serial.print(c);
  }
  Serial.println();
  Serial.println();
  

  if (message == "1") {
    canContinue = 0;
    publishMessage("1", "ConveyorBeltReading");
  } else if (message == "0") {
    canContinue = 1;
  }
}


#endif
