#include <Wire.h>

const int led1 = 13;
const int led2 = 12;
void setup() 
{
  // put your setup code here, to run once:
  Wire.begin(8);

  Wire.onReceive(receiveEvent);

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
}
void receiveEvent(int number){
  while (Wire.available()){
    char d = Wire.read();
    if (d == 0)
    {
        digitalWrite(led1, HIGH); 
    }
    else if (d == 1)
    {
        digitalWrite(led1, LOW); 
    }
    else if (d == 2)
    {
        digitalWrite(led2, HIGH); 
    }
    else if (d == 3)
    {
        digitalWrite(led2, LOW); 
    }
  }
}
void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
}
