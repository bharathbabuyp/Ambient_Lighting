int tr,tg,tb,lr,lg,lb,rr,rg,rb;
void setup() {
  Serial.begin(9600);
  //top
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  // left
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(3,OUTPUT);
  //right
  pinMode(2,OUTPUT);
  pinMode(1,OUTPUT);
  pinMode(0,OUTPUT);
}
void loop() {

 if (Serial.available()>0)
 {
  if(Serial.peek()=='c')
  {
    Serial.read();
  
  tr=Serial.parseInt();
  tg=Serial.parseInt();
  tb=Serial.parseInt();

  lr=Serial.parseInt();
  lg=Serial.parseInt();
  lb=Serial.parseInt();

  rr=Serial.parseInt();
  rg=Serial.parseInt();
  rb=Serial.parseInt();
  

analogWrite(11,rr);
analogWrite(10,rg);
analogWrite(9,rb);

analogWrite(6,lr);
analogWrite(5,lg);
analogWrite(3,lb);

//analoggWrite(2,rr);
//analoggWrite(1,rg);
//analoggWrite(0,rb);

  }
 if(Serial.available()>0){
  Serial.read();
 }
 }
 }
 //void analoggWrite(int pin, int value)
//{
   
 // digitalWrite(pin,HIGH);
 // delay(3);
  
 // digitalWrite(pin,LOW);
 // delay((256*3-3*value)/value);
 //}
