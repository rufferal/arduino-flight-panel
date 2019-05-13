#include "Joystick.h"

Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID, JOYSTICK_TYPE_MULTI_AXIS, 32, 1, true);

const int pinToButtonMap = 9;
const int pinToAxisMap = A0;

int buttonState = 0;
int axisState = 0;
int xMinimum = 1023;
int xMaximum = 0;


void setup() {
  pinMode(pinToButtonMap, INPUT_PULLUP);
  pinMode(pinToAxisMap, INPUT_PULLUP);
  pinMode(13, OUTPUT);

  Joystick.setXAxisRange(-127, 127);

  Joystick.begin();
  delay(1000);
  digitalWrite(13, HIGH);

  
  
}


void loop() {
  int curState = !digitalRead(pinToButtonMap);
  
  if (curState != buttonState) {
    Joystick.setButton(0, curState);
    buttonState = curState;
  }
  
  curState = analogRead(pinToAxisMap);
  if (curState > xMaximum) {
    xMaximum = curState;
  } else if (curState < xMinimum) {
    xMinimum = curState;
  }
  curState = map(curState, xMinimum, xMaximum, -127, 127);
  curState = (axisState * 2 + curState) / 3;
  if (curState != axisState) {
    Joystick.setXAxis(curState);
    axisState = curState;
  }

  delay(5);
  
}
