#include "WLAN.h"
#include "MQTT.h"



void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  connectToWifi();

  connectToMQTTBroker();

  mqttClient.onMessage(onMqttMessage); // Set callback

  subscribeToTopic("BoxDetection");
  
  conveyorBelt.move();
  
}

void loop() {
if (!mqttClient.connected()) {


    digitalWrite(LED_BUILTIN, LOW);
    connectToWifi();
    connectToMQTTBroker();

  } else if (conveyorBelt.canContinue) {
    
    conveyorBelt.move();

  } else {

    conveyorBelt.stop(); 

  }

  mqttClient.poll();
}