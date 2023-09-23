#include <SoftwareSerial.h>
SoftwareSerial HC06{0,1};
int LED =13;
int Buzzer = 12;
int motorPin = 11; 
int other = 10;
int In1 = 9;
int In2 = 8;
int In3 = 6;
int In4 = 7;
int ENA = 5;
int ENB = 11; 

void setup() {
  
HC06.begin(9600);
Serial.begin(9600);
pinMode(LED,OUTPUT);
pinMode(Buzzer,OUTPUT);
pinMode(motorPin, OUTPUT);
pinMode(other, OUTPUT);
pinMode(In1,OUTPUT);
pinMode(In2,OUTPUT);
pinMode(ENA,OUTPUT);
analogWrite(ENA,10);
analogWrite(ENB,12);


}

void loop() {
if(HC06.available()>0)
{
 char recieve = HC06.read();
 if(recieve == '1')
 {
   digitalWrite(LED,HIGH);
 }
 else if (recieve == '2')
 {
    digitalWrite(LED,LOW);
 }
 else if(recieve == '3')
 {
     digitalWrite(Buzzer,HIGH);
 }
 else if (recieve == '4')
 {
    digitalWrite(Buzzer,LOW);
 }
else if (recieve == '5')
 {  
    analogWrite(ENB,27);
    digitalWrite(In3,HIGH);
    digitalWrite(In4,LOW);   
    delay(2000);
    digitalWrite(In3,LOW);
    digitalWrite(In4,LOW);  

 } 
 else if (recieve == '6')
 {  analogWrite(ENB,12);
    digitalWrite(In4,HIGH);
    digitalWrite(In3,LOW);   
    delay(1000);
    digitalWrite(In4,LOW);
    digitalWrite(In3,LOW);   
 } 
 else if (recieve == '7')
 {
    digitalWrite(other,HIGH);
     
 } else if (recieve == '8')
 {
  
    delay(3000);

    
 } 
  else if (recieve == '9')
 {  // clockwise rotation
  
    delay(6000);
  
  
 } 



}
}
