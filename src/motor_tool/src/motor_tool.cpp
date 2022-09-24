#include <ros/ros.h>
#include <iostream>
#include <cstdint>

extern "C"{
#include <motor_tool/motor_function.h>
}

void readRegister();
void writeRegister();
void settingController(uint8_t address);
void settingPID(uint8_t address, char type);
void clearMsg(serialData *targetMsg);

serialData msg;

int main(int argc, char **argv){
    ros::init(argc, argv, "motor_tool");
    ros::NodeHandle rosNh;

    int mode = 0;

    serialInit();

    while(ros::ok()){

        std::cout << "choose mode 1:read register 2:write register 3:setting controller 4:PID setting" << std::endl;
        std::cin >> mode;
        std::cin.get();

        if(mode == 1){
            readRegister();
            CRC16Generate(&msg);
            transmitData(&msg);
            receiveData(&msg);
        }
        else if(mode == 2){
            writeRegister();
            CRC16Generate(&msg);
            transmitData(&msg);
            receiveData(&msg);

        }
        else if(mode == 3){
            int address;
            std::cout << "enter target address:" << std::endl;
            std::cin  >> std::dec >> address;
            std::cin.get();
            settingController((uint8_t)address);
        }
        else if(mode == 4){
            int address;
            char type;
            std::cout << "enter target address:" << std::endl;
            std::cin >> std::dec >> address;
            std::cin.get();
            std::cout << "p or i or d ?" << std::endl;
            std::cin >> type;
            std::cin.get();
            settingPID((uint8_t)address, type);
        }
        else{
            continue;
        }
    }


    return 0;
}

void readRegister(){
    int input = 0;

    clearMsg(&msg);
    msg.length = 8;
    std::cout << "enter controller address: (dec)" << std::endl;
    std::cin >> std::dec >> input;
    std::cin.get();
    msg.data[0] = (uint8_t)input;
    std::cout << std::endl;

    msg.data[1] = 0x03;

    std::cout << "enter register address: (hex)" << std::endl;
    std::cin >> std::hex >> input;
    std::cin.get();
    msg.data[3] = (0xff & input);
    msg.data[2] = (0xff & (input >> 8));
    std::cout << std::endl;
    std::cout << "enter numbers of registers: (dec)" << std::endl;
    std::cin >> std::dec >> input;
    std::cin.get();
    msg.data[5] = (0xff & input);
    msg.data[4] = (0xff & (input >> 8));
    std::cout << std::endl;

    return;
}

void writeRegister(){
    int input;

    clearMsg(&msg);
    msg.length = 8;
    std::cout << "enter target address: (dec)" << std::endl;
    std::cin >> std::dec >> input;
    std::cin.get();
    msg.data[0] = (uint8_t)input;
    std::cout << std::endl;

    msg.data[1] = 0x06;

    std::cout << "enter register address: (hex)" << std::endl;
    std::cin >> std::hex >> input;
    std::cin.get();
    msg.data[3] = (0xff & input);
    msg.data[2] = (0xff & (input >> 8));
    std::cout << std::endl;

    std::cout << "enter data: (dec)" << std::endl;
    std::cin >> std::dec >> input;
    std::cin.get();
    msg.data[5] = (0xff & input);
    msg.data[4] = (0xff & (input >> 8));
    std::cout << std::endl;

    return ;
}

void settingController(uint8_t address){

    //0x6a = 0x271(625)
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x6a;
    msg.data[4] = 0x02;
    msg.data[5] = 0x71; 
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x6b = 0x271(625)
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x6b;
    msg.data[4] = 0x02;
    msg.data[5] = 0x71;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x6c = 500
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x6c;
    msg.data[4] = 0x01;
    msg.data[5] = 0xf4;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x93 = 1
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x93;
    msg.data[5] = 0x01;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x94 = 0
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x94;
    msg.data[5] = 0x00;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x70 = 0
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x70;
    msg.data[5] = 0x00;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x79 = 0
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x79;
    msg.data[5] = 0x00;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x7a = 0
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x7a;
    msg.data[5] = 0x00;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x73 = 2
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x73;
    msg.data[5] = 0x02;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //0x74 = 10
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0x74;
    msg.data[5] = 0x0a;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);
    
    //0xe1 = 1
    clearMsg(&msg);
    msg.length = 8;
    msg.data[0] = address;
    msg.data[1] = 0x06;
    msg.data[3] = 0xe1;
    msg.data[5] = 0x01;
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    return;
}

void settingPID(uint8_t address, char type){
    float floatinput;
    unsigned int *input_ptr;
    unsigned int  input;

    std::cout << "enter data: p(0.001~1) i(0.001~1) d(0.001~1) (dec)" << std::endl;
    std::cin >> std::dec >> floatinput;
    std::cin.get();

    input_ptr = (unsigned int *)&floatinput;
    input = *input_ptr;

    if(type == 'p'){
        clearMsg(&msg);
        msg.length = 8;
        msg.data[0] = address;
        msg.data[1] = 0x06;
        msg.data[2] = 0x00;
        msg.data[3] = 0xc0;
        msg.data[4] = (0xff & (input >> 24));
        msg.data[5] = (0xff & (input >> 16));
        CRC16Generate(&msg);
        transmitData(&msg);
        receiveData(&msg);

        clearMsg(&msg);
        msg.length = 8;
        msg.data[0] = address;
        msg.data[1] = 0x06;
        msg.data[2] = 0x00;
        msg.data[3] = 0xc1;
        msg.data[4] = (0xff & (input >> 8));
        msg.data[5] = (0xff & input);
        CRC16Generate(&msg);
        transmitData(&msg);
        receiveData(&msg);
    }
    else if(type == 'i'){
        clearMsg(&msg);
        msg.length = 8;
        msg.data[0] = address;
        msg.data[1] = 0x06;
        msg.data[2] = 0x00;
        msg.data[3] = 0xc2;
        msg.data[4] = (0xff & (input >> 24));
        msg.data[5] = (0xff & (input >> 16));
        CRC16Generate(&msg);
        transmitData(&msg);
        receiveData(&msg);

        clearMsg(&msg);
        msg.length = 8;
        msg.data[0] = address;
        msg.data[1] = 0x06;
        msg.data[2] = 0x00;
        msg.data[3] = 0xc3;
        msg.data[4] = (0xff & (input >> 8));
        msg.data[5] = (0xff & input);
        CRC16Generate(&msg);
        transmitData(&msg);
        receiveData(&msg);
    }
    else if(type == 'd'){
        clearMsg(&msg);
        msg.length = 8;
        msg.data[0] = address;
        msg.data[1] = 0x06;
        msg.data[2] = 0x00;
        msg.data[3] = 0xc4;
        msg.data[4] = (0xff & (input >> 24));
        msg.data[5] = (0xff & (input >> 16));
        CRC16Generate(&msg);
        transmitData(&msg);
        receiveData(&msg);

        clearMsg(&msg);
        msg.length = 8;
        msg.data[0] = address;
        msg.data[1] = 0x06;
        msg.data[2] = 0x00;
        msg.data[3] = 0xc5;
        msg.data[4] = (0xff & (input >> 8));
        msg.data[5] = (0xff & input);
        CRC16Generate(&msg);
        transmitData(&msg);
        receiveData(&msg);
    }
    
    return;
}

void clearMsg(serialData *targetMsg){
    for(int i = 0; i < 20; i++){
        targetMsg->data[i]= 0;
    }

    targetMsg->length = 0;

    return;
}