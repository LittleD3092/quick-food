#include<Servo.h> //test

// a Stepper , b 推桿 , c DC motor
const byte a_CLK = 2; // step
const byte a_CW  = 7;  // direction
const byte b_ENA = 11;
const byte b_IN1 = 9;
const byte b_IN2 = 10;
const byte c_IN1 = 6; //speed
const byte c_IN2 = 5; //direction

Servo myservo;

void setup()
{
    Serial.begin(57600);
    pinMode(a_CLK, OUTPUT);
    pinMode(a_CW,  OUTPUT);
    pinMode(b_ENA, OUTPUT);
    pinMode(b_IN1, OUTPUT);
    pinMode(b_IN2, OUTPUT);
    pinMode(c_IN1, OUTPUT);
    pinMode(c_IN2, OUTPUT);
    myservo.attach(3); 
}

// directions not yet confirmed
void a_task(int status)
{
    if (status == 1) // stop
    {
        digitalWrite(a_CLK, LOW);
    }
    else if (status == 2) // counterclockwise(?
    {
        digitalWrite(a_CW, LOW);
        digitalWrite(a_CLK, HIGH);
        delayMicroseconds(500);
        digitalWrite(a_CLK, LOW);
        delayMicroseconds(500);
    }
    else if (status == 3) // clockwise(?
    {
        digitalWrite(a_CW, HIGH);
        digitalWrite(a_CLK, HIGH);
        delayMicroseconds(500);
        digitalWrite(a_CLK, LOW);
        delayMicroseconds(500);
    }
}

void b_task(int status)
{
    if (status == 1) // stop
    {
        digitalWrite(b_IN1, LOW);
        digitalWrite(b_IN2, LOW);
        analogWrite(b_ENA, 0);
    }
    else if (status == 2) //縮短
    {
        digitalWrite(b_IN1, HIGH);
        digitalWrite(b_IN2, LOW);
        analogWrite(b_ENA, 240);
    }
    else if (status == 3) //伸長
    {
        digitalWrite(b_IN1, LOW);
        digitalWrite(b_IN2, HIGH);
        analogWrite(b_ENA, 240);
    }
}

// directions not yet confirmed
void c_task(int status)
{
    if (status == 1) // stop
    {
        analogWrite(c_IN1, 0);
        digitalWrite(c_IN2, HIGH);
    }
    else if (status == 2) // counterclockwise(?
    {
        analogWrite(c_IN1, 150);
        digitalWrite(c_IN2, HIGH);
    }
    else if (status == 3) // clockwise(?
    {
        analogWrite(c_IN1, 150);
        digitalWrite(c_IN2, LOW);
    }
}

void t_task(int status)  //test
{
    if(status == 1) //stop
    {
        myservo.write(90);
    }
    else if (status == 2) 
    {
        myservo.write(0);
    }
    else if (status == 3) 
    {
        myservo.write(180);
    }
}

void action(String message)
{
    char motor_type = message[0];
    char motor_status = message[1];

    switch (motor_type)
    {
    case 'a':
        a_task(int(motor_status - '0'));
    case 'b':
        b_task(int(motor_status - '0'));
    case 'c':
        c_task(int(motor_status - '0'));
    case 't':
        t_task(int(motor_status - '0'));
    }
}

String message;
void loop()
{
    if (Serial.available() > 0)
    {
        message = Serial.readString();
        Serial.println(message);
    }
    action(message);
}