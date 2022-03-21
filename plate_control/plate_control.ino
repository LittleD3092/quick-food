
void setup() {
  pinMode(23,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(22,OUTPUT);
  pinMode(4,OUTPUT);// put your setup code here, to run once:

}

void loop() {
  analogWrite(3,255);
  analogWrite(4,255);
  digitalWrite(22,HIGH);
  digitalWrite(23,HIGH);
  delay(1000);
  analogWrite(3,255);
  analogWrite(4,255);
  digitalWrite(22,LOW);
  digitalWrite(23,LOW);
  delay(1000);
}
