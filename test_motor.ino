#include "Arduino.h"


//-- Driver pin
const static int PWM_R = 7;
const static int PWM_L = 6;
const static int EN_R = 3;
const static int EN_L = 2;
//-- Encoder pin
const static int OUT_A = 8;
const static int OUT_B = 9;
//-- Encoder stuff
int counter(0);
int state(0);
int state_B(0);
int last_state(0);

void setup() {
  
  //-- Initialize serial
  Serial.begin(9600);
  
  delay(2000);
  //-- Driver setup
  pinMode(EN_R, OUTPUT);
  pinMode(EN_L, OUTPUT);
  pinMode(PWM_R, OUTPUT);
  pinMode(PWM_L, OUTPUT);
  
  //-- Encoder setup
  pinMode(OUT_A, INPUT);
  pinMode(OUT_B, INPUT);
  last_state = digitalRead(OUT_A);
}



void loop() {

    
  //-- Enable the driver
  digitalWrite(EN_R, HIGH);
  digitalWrite(EN_L, HIGH);

  //-- Write PWM
  analogWrite(PWM_R, 200);
  analogWrite(PWM_L, 0);
  delay(2000);
  
  //-- current sensor
  unsigned int x=0;
float AcsValue=0.0,Samples=0.0,AvgAcs=0.0,AcsValueF=0.0;

  for (int x = 0; x < 150; x++){ //Get 150 samples
  AcsValue = analogRead(A0);     //Read current sensor values   
  Samples = Samples + AcsValue;  //Add samples together
  delay (3); // let ADC settle before next sample 3ms
}
AvgAcs=Samples/150.0;//Taking Average of Samples

//((AvgAcs * (5.0 / 1024.0)) is converitng the read voltage in 0-5 volts
//2.5 is offset(I assumed that arduino is working on 5v so the viout at no current comes
//out to be 2.5 which is out offset. If your arduino is working on different voltage than 
//you must change the offset according to the input voltage)
//0.185v(185mV) is rise in output voltage when 1A current flows at input
AcsValueF = (2.5 - (AvgAcs * (5.0 / 1024.0)) )/0.185;
Serial.print(AcsValueF);//Print the read current on Serial monitor
  delay(50);

  
  
  
  
  
  

  //-- Encoder part
  state = digitalRead(OUT_A);
  state_B = digitalRead(OUT_B);
  Serial.print("A : ");Serial.println(state);
  Serial.print("B : ");Serial.println(state_B);
  if(state != last_state){
    if(state_B != state){
      counter++;
    }else{
      counter--;
    }
    Serial.print("Position : ");
    Serial.println(counter);
  }
  last_state = state;
  delay(10);

 
  
}


//Position : -101
//-0.19A : 0
//B : 0
//-0.26A : 1
//B : 1
//Position : -102
//0.11A : 1
//B : 1
//-0.07A : 0
//B : 0
//Position : -103
//-0.37A : 0
//B : 1
//-0.03A : 1










 
