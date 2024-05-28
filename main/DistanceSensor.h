#ifndef DistanceSensor_h
#define DistanceSensor_h
#include "Arduino.h" 


class DistanceSensor {

private:

  int _trigPin;
  int _echoPin;
  float _soundSpeed_cmPerSecond = 0.0343;
  long _distanceToObject;


public:

  DistanceSensor(int trigPin, int echoPin){
    
    _trigPin = trigPin;
    _echoPin = echoPin;
    _soundSpeed_cmPerSecond = 0.0343;

    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);

  };

  int getTrigPin(){

    return _trigPin;

  };

  int getEchoPin(){

    return _echoPin;

  };

  void transmitUltrasound(){

    digitalWrite(_trigPin, LOW);
    delayMicroseconds(5);
    digitalWrite(_trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(_trigPin, LOW);

  }

  long getDistanceToObject(){

    transmitUltrasound();

    return (pulseIn(_echoPin, HIGH)/2) / 29.1;

  }

  bool isObjectDetected(float thresholdDistance){

    return getDistanceToObject() < thresholdDistance;

  }
  

};

#endif