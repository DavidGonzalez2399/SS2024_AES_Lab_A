#include <ArduinoMqttClient.h>
#include <WiFiNINA.h>

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = "Galaxy";        // your network SSID
char pass[] = "andrew2020";    // your network password

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[] = "192.168.17.44";
int        port     = 1883;
const char topic[]  = "ColorSensorReading";

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();

  // set the message receive callback
  mqttClient.onMessage(onMqttMessage);

  Serial.print("Subscribing to topic: ");
  Serial.println(topic);
  Serial.println();

  // subscribe to a topic
  mqttClient.subscribe(topic);

  // topics can be unsubscribed using:
  // mqttClient.unsubscribe(topic);

  Serial.print("Topic: ");
  Serial.println(topic);

  Serial.println();
}

void loop() {
  // call poll() regularly to allow the library to receive MQTT messages and
  // send MQTT keep alive which avoids being disconnected by the broker
  mqttClient.poll();
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
}

/*

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

*/
