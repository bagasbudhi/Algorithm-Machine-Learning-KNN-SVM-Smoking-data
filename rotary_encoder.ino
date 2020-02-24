///////////////////////////// encoder ky040 /////////////
// int pinA = 3;  // Connected to CLK on KY-040
// int pinB = 4;  // Connected to DT on KY-040
// int encoderPosCount = 0; 
// int pinALast;  
// int aVal;
// boolean bCW;
//
// void setup() { 
//   pinMode (pinA,INPUT);
//   pinMode (pinB,INPUT);
//   /* Read Pin A
//   Whatever state it's in will reflect the last position   
//   */
//   pinALast = digitalRead(pinA);   
//   Serial.begin (9600);
// } 
//
// void loop() { 
//   aVal = digitalRead(pinA);
//   if (aVal != pinALast){ // Means the knob is rotating
//     // if the knob is rotating, we need to determine direction
//     // We do that by reading pin B.
//     if (digitalRead(pinB) != aVal) {  // Means pin A Changed first - We're Rotating Clockwise
//       encoderPosCount ++;
//       bCW = true;
//     } else {// Otherwise B changed first and we're moving CCW
//       bCW = false;
//       encoderPosCount--;
//     }
//     Serial.print ("Rotated: ");
//     if (bCW){
//       Serial.println ("counterclockwise");
//     }else{
//       Serial.println("clockwise");
//     }
//     Serial.print("Encoder Position: ");
//     Serial.println(encoderPosCount);
//     
//   } 
//   pinALast = aVal;
// } 
//
//


///////////////////// encoder autonic ////////////////

volatile unsigned int temp, counter = 0; //This variable will increase or decrease depending on the rotation of encoder
    
void setup() {
  Serial.begin (9600);

  pinMode(2, INPUT_PULLUP); // internal pullup input pin 2 
  
  pinMode(3, INPUT_PULLUP); // internalเป็น pullup input pin 3
//Setting up interrupt
  //A rising pulse from encodenren activated ai0(). AttachInterrupt 0 is DigitalPin nr 2 on moust Arduino.
  attachInterrupt(0, ai0, RISING);
   
  //B rising pulse from encodenren activated ai1(). AttachInterrupt 1 is DigitalPin nr 3 on moust Arduino.
  attachInterrupt(1, ai1, RISING);
  }
   
  void loop() {
  // Send the value of counter
  if( counter != temp ){
  Serial.println (counter);
  temp = counter;
  }
  }
   
  void ai0() {
  // ai0 is activated if DigitalPin nr 2 is going from LOW to HIGH
  // Check pin 3 to determine the direction
  if(digitalRead(3)==LOW) {
  counter++;
  }else{
  counter--;
  }
  }
   
  void ai1() {
  // ai0 is activated if DigitalPin nr 3 is going from LOW to HIGH
  // Check with pin 2 to determine the direction
  if(digitalRead(2)==LOW) {
  counter--;
  }else{
  counter++;
  }
  }
