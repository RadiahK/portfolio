
 #include <Servo.h>                           // Include servo library
 int pushButton = 2;

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

void setup(){
  // put your setup code here, to run once:
  //servoLeft.attach(13);                      // Attach left signal to pin 13
  //servoRight.attach(12);                     // Attach left signal to pin 12
  Serial.begin(9600);
  pinMode(pushButton, INPUT);
}


void stayStill (int times){
  servoLeft.detach();
  servoRight.detach();
  delay(times);
  servoLeft.attach(13);
  servoRight.attach(12);
}
void moveForward (int times){
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(times);
}
void moveBackward (int times){
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(0);
  servoRight.writeMicroseconds(2000);
  delay (times);
}
void turnRight (int degree){
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(2000);
  delay ((1100/80) * degree);
}
void turnLeft (int degree){
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(0);
  servoRight.writeMicroseconds(0);
  delay ((1100/80) * degree);
}
void loop(){
 int buttonState = digitalRead(pushButton);
 Serial.println(buttonState);
 if (buttonState == 1){
  turnRight(90);
 }
}


