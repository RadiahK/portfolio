 #include <Servo.h>                           // Include servo library
 
 Servo servoLeft;                             // Declare left servo signal
 Servo servoRight;                            // Declare right servo signal
 
 void setup(){
  // put your setup code here, to run once:
  servoLeft.attach(13);                      // Attach left signal to pin 13
   servoRight.attach(12);                      // Attach left signal to pin 12
 }
 
 
 void stayStill (int times){
   servoLeft.detach();
   servoRight.detach();
   delay(times);
   servoLeft.attach(13);
   servoRight.attach(12);
 }
 void moveForward (int times){
   servoLeft.writeMicroseconds(2000);
   servoRight.writeMicroseconds(0);
   delay(times);
 }
 void moveBackward (int times){
   servoLeft.writeMicroseconds(0);
   servoRight.writeMicroseconds(2000);
   delay (times);
 }
 void turnRight (int degree){
servoLeft.writeMicroseconds(2000);
servoRight.writeMicroseconds(2000);
  delay ((1100/80) * degree);
 }
 void turnLeft (int degree){
   servoLeft.writeMicroseconds(0);
   servoRight.writeMicroseconds(0);
   delay ((1100/80) * degree);
 }
 void loop(){
   moveForward(1000);
   moveBackward(1000);
 }
