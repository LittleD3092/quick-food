int a=0;
void setup()
{
    Serial.begin(9600);
    pinMode(23, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(22, OUTPUT);
    pinMode(4, OUTPUT);
}

void loop()
{
    // 1: forward
    // 2: backward
    // 3: turn right
    // 4: turn left
    if (Serial.available() > 0)
    {
        a = Serial.read() - '0';
        Serial.println(a);
    }
    switch (a)
    {
    case 1:
        digitalWrite(23, HIGH);
        digitalWrite(24, HIGH);
        analogWrite(3, 255);
        analogWrite(4, 255);
        Serial.println("forward");
        break;
    case 2:
        digitalWrite(23, LOW);
        digitalWrite(24, LOW);
        analogWrite(3, 255);
        analogWrite(4, 255);
        Serial.println("backward");
        break;
    case 3:
        digitalWrite(23, LOW);
        digitalWrite(24, HIGH);
        analogWrite(3, 255);
        analogWrite(4, 255);
        Serial.println("turn right");
        break;
    case 4:
        digitalWrite(23, HIGH);
        digitalWrite(24, LOW);
        analogWrite(3, 255);
        analogWrite(4, 255);
          Serial.println("turn left");
        break;
    case 7:
        analogWrite(3, 0);
        analogWrite(4, 0);
        Serial.println("na");
        break;
    }
}
