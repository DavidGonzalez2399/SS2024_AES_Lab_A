#ifndef ConveyorBelt_h
#define ConveyorBelt_h

#include <Arduino.h>

class ConveyorBelt {

  private:

    int _stepPin;
    int _dirPin;
    

  public:

  int canContinue;
  
  ConveyorBelt(int stepPin, int dirPin){

    _stepPin = stepPin;
    _dirPin = dirPin;
    canContinue = 1;

    pinMode(stepPin, OUTPUT); 
    pinMode(dirPin, OUTPUT);
    digitalWrite(dirPin, HIGH);

    pinMode(LED_BUILTIN, OUTPUT);

  };


  void move(){

    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(_dirPin, HIGH);
    digitalWrite(_stepPin, HIGH); 
    delayMicroseconds(400); 
    digitalWrite(_stepPin, LOW); 
    delayMicroseconds(400);

  };


  void stop(){

    digitalWrite(LED_BUILTIN, LOW);
    digitalWrite(_dirPin, LOW);
    digitalWrite(_stepPin, LOW); 

  }
  

};





#endif 