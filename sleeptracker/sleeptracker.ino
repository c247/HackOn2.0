#include <Math.h>
int greenLed = 2;         
int yellowLed = 3;          
int blueLed = 4;            

int lightSensorPin = A0;        
int analogValue;
const int flexPin = A5;
int flexValue;

int buzz = 10;

void setup() {
Serial.begin(9600);  
  //Set pins to outputs
  pinMode(greenLed, OUTPUT);
  pinMode(yellowLed,OUTPUT);
  pinMode(blueLed,OUTPUT);
}
int prevnext [2] = {0,0};
int count = 0;
// ORDER OF OUTPUT SENSOR light, flex
void loop(){
  //Storing Input
  flexValue = analogRead(flexPin);
  analogValue = analogRead(lightSensorPin);
if (count == 0) {
  prevnext[0] = analogValue;
  count = 1;
}
prevnext[1] = analogValue;
if (abs((prevnext[1] - prevnext[0])*100)/abs(prevnext[0]) > 5 || (flexValue <= 12)) {
   Serial.print(flexValue);
   Serial.print(",");
   Serial.println(analogValue);
}

prevnext[0] = analogValue;  
 
  if(analogValue < 5){            
    digitalWrite(blueLed, HIGH);
  }
  else if(analogValue >= 5 && analogValue <= 100){
    digitalWrite(yellowLed, HIGH);
  }
  else{
    digitalWrite(greenLed, HIGH);
  }
  delay(200);
  digitalWrite(greenLed, LOW);
  digitalWrite(yellowLed, LOW);
  digitalWrite(blueLed, LOW);

if (flexValue <= 12) {
   tone(buzz, 1000, 500);
}
}
