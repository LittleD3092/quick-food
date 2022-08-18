import serial
from time import sleep
import sys
COM_PORT = 'COM5'  
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)
try:
    while True:
        choice = input('enter').lower()
        if choice == '1':
            print('forward')
            ser.write(b'1')  
            sleep(0.5)              
        elif choice == '2':
            print('backward')
            ser.write(b'2')
            sleep(0.5)
        elif choice == '3':
            print('turn left')
            ser.write(b'3')
            sleep(0.5)
        elif choice == '4':
            print('turn right')
            ser.write(b'4') 
            sleep(0.5)
        elif choice == '0':
            ser.close()
            print('seeu ')
            sys.exit()
        else:
            print('wrong')
            ser.write(b'7')
            sleep(0.5)
        
        while ser.in_waiting:
            try:
                mcu_feedback = ser.readline().decode()  
                print('reacting.....', mcu_feedback)
            except:
                print("serial read error")

except KeyboardInterrupt:
    ser.close()
    print('seeu')