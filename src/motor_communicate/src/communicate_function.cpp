#include "motor_communicate/communicate_function.h"

wheel::wheel(uint8_t address){

    //set address
    this->controller_Address = address;

    this->target_speed = 0;
    this->last_target_speed = 0;

    // init serialData
    clearMsg();

    return;
}

void wheel::settingRpmData(int *xdata, int xlength, int *ydata, int ylength){

    this->rpm_X_Data = xdata;
    this->rpm_X_Data_Length = xlength;

    this->rpm_Y_Data = ydata;
    this->rpm_Y_Data_Length = ylength;

    return;
}

void wheel::settingRpmBias(int *xdata, int xlength, int *ydata, int ylength){

    this->rpm_X_Bias = xdata;
    this->rpm_X_Bias_Length = xlength;

    this->rpm_Y_Bias = ydata;
    this->rpm_Y_Bias_Length = ylength;

    return;
}

void wheel::settingRpmRotation(int speed)
{
    this->rpm_Rotation = speed;

    return;
}

void wheel::settingXPID(float data_load[3], float data_unload[3]){

    this->x_Pid_data_load = data_load;

    std::cout << "wheel " << (int)this->controller_Address << "x pid load p " << this-> x_Pid_data_load[0];
    std::cout << " i " <<  this-> x_Pid_data_load[1];
    std::cout << " d " <<  this-> x_Pid_data_load[2] << std::endl;


    this->x_Pid_data_unload = data_unload;

    std::cout << "wheel " << (int)this->controller_Address << "x pid unload p " << this-> x_Pid_data_unload[0];
    std::cout << " i " <<  this-> x_Pid_data_unload[1];
    std::cout << " d " <<  this-> x_Pid_data_unload[2] << std::endl;

    return;
}

void wheel::settingYPID(float data_load[3], float data_unload[3]){

    this->y_Pid_data_load = data_load;

    std::cout << "wheel " << (int)this->controller_Address << "y pid load p " << this-> y_Pid_data_load[0];
    std::cout << " i " <<  this-> y_Pid_data_load[1];
    std::cout << " d " <<  this-> y_Pid_data_load[2] << std::endl;

    this->y_Pid_data_unload = data_unload;

    std::cout << "wheel " << (int)this->controller_Address << "y pid unload p " << this-> y_Pid_data_unload[0];
    std::cout << " i " <<  this-> y_Pid_data_unload[1];
    std::cout << " d " <<  this-> y_Pid_data_unload[2] << std::endl;

    return;
}

void wheel::settingRotationPID(float *data_load, float *data_unload){

    this->rotation_Pid_data_load = data_load;

    std::cout << "wheel " << (int)this->controller_Address << "rotation pid load p " << this-> rotation_Pid_data_load[0];
    std::cout << " i " <<  this-> rotation_Pid_data_load[1];
    std::cout << " d " <<  this-> rotation_Pid_data_load[2] << std::endl;

    this->rotation_Pid_data_unload = data_unload;

    std::cout << "wheel " << (int)this->controller_Address << "rotation pid unload p " << this-> rotation_Pid_data_unload[0];
    std::cout << " i " <<  this-> rotation_Pid_data_unload[1];
    std::cout << " d " <<  this-> rotation_Pid_data_unload[2] << std::endl;

    return;
}

void wheel::set_X_Speed(int speed, int bias){

    if(this->controller_Address == 0){
        return;
    }

    clearMsg();

    this->msg.length = 8;
    this->msg.data[0] = controller_Address;
    this->msg.data[1] = 0x06;
    this->msg.data[3] = 0x43;

    short int speedValue;

    if(abs(speed) < this->rpm_X_Data_Length){    
        speedValue = (short int)this->rpm_X_Data[abs(speed)]; 
    }

    if(bias == 1){
        speedValue += this->rpm_X_Bias[abs(speed)];
    }
    else if(bias == 2){
        speedValue -= this->rpm_X_Bias[abs(speed)];
    }

    if(speed < 0){
        speedValue = -1*speedValue;
    }

    this->msg.data[4] = ((speedValue >> 8) & 0xff);
    this->msg.data[5] = (speedValue & 0xff);

    CRC16Generate(&this->msg);
    transmitData(&this->msg);
    receiveData(&this->msg);


    this->last_target_speed = this->target_speed;
    this->target_speed = speedValue;

    //std::cout << "wheel " << this->controller_Address << " target speed" << speedValue << std:: endl;

    return;
};

void wheel::set_Y_Speed(int speed, int bias){

    if(this->controller_Address == 0){
        return;
    }

    clearMsg();

    this->msg.length = 8;
    this->msg.data[0] = controller_Address;
    this->msg.data[1] = 0x06;
    this->msg.data[3] = 0x43;

    short int speedValue;

    if(abs(speed) < this->rpm_X_Data_Length){    
        speedValue = (short int)this->rpm_Y_Data[abs(speed)]; 
    }

    if(bias == 1){
        speedValue += this->rpm_Y_Bias[abs(speed)];
    }
    else if(bias == 2){
        speedValue -= this->rpm_Y_Bias[abs(speed)];
    }

    if(speed < 0){
        speedValue = -1*speedValue;
    }

    this->msg.data[4] = ((speedValue >> 8) & 0xff);
    this->msg.data[5] = (speedValue & 0xff);

    CRC16Generate(&this->msg);
    transmitData(&this->msg);
    receiveData(&this->msg);

    this->last_target_speed = this->target_speed;
    this->target_speed = speedValue;

    //std::cout << "wheel " << this->controller_Address << " target speed" << speedValue << std:: endl;

    return;
};

void wheel::setRoatation(int direction){

    if(this->controller_Address == 0){
        return;
    }

    clearMsg();

    this->msg.length = 8;
    this->msg.data[0] = this->controller_Address;
    this->msg.data[1] = 0x06;
    this->msg.data[3] = 0x43;

    short int speedValue = (short int)rpm_Rotation;

    if(direction == 1){
        this->msg.data[4] = (speedValue >> 8) & 0xff;
        this->msg.data[5] = speedValue & 0xff;
    }
    else if (direction == 2){
        speedValue = -1*speedValue;
        this->msg.data[4] = (speedValue >> 8) & 0xff;
        this->msg.data[5] = speedValue & 0xff;
    }

    CRC16Generate(&this->msg);
    transmitData(&this->msg);
    receiveData(&this->msg);

    this->last_target_speed = this->target_speed;
    this->target_speed = speedValue;

    //std::cout << "wheel " << this->controller_Address << " target speed" << speedValue << std:: endl;

    return;
}

void wheel::setPID(int direction, int speed, bool load){

    uint32_t *ptr;
    float p_val;
    float i_val;
    float d_val;

    if(load){
        if(direction == 0){
            p_val = rotation_Pid_data_load[0];
            i_val = rotation_Pid_data_load[1];
            d_val = rotation_Pid_data_load[2];
        }
        else if(direction == 1){
            p_val = x_Pid_data_load[0];
            i_val = x_Pid_data_load[1];
            d_val = x_Pid_data_load[2];
        }
        else if(direction == 2){
            p_val = y_Pid_data_load[0];
            i_val = y_Pid_data_load[1];
            d_val = y_Pid_data_load[2];
        }
    }else{
        if(direction == 0){
            p_val = rotation_Pid_data_unload[0];
            i_val = rotation_Pid_data_unload[1];
            d_val = rotation_Pid_data_unload[2];
        }
        else if(direction == 1){
            p_val = x_Pid_data_unload[0];
            i_val = x_Pid_data_unload[1];
            d_val = x_Pid_data_unload[2];
        }
        else if(direction == 2){
            p_val = y_Pid_data_unload[0];
            i_val = y_Pid_data_unload[1];
            d_val = y_Pid_data_unload[2];
        }
    }
    
    //rotation p
    ptr = (unsigned int *)&(p_val);

    clearMsg();
    msg.length = 8;
    msg.data[0] = this->controller_Address;
    msg.data[1] = 0x06;
    msg.data[2] = 0x00;
    msg.data[3] = 0xc0;
    msg.data[4] = (0xff & (*ptr >> 24));
    msg.data[5] = (0xff & (*ptr >> 16));
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    clearMsg();
    msg.length = 8;
    msg.data[0] = this->controller_Address;
    msg.data[1] = 0x06;
    msg.data[2] = 0x00;
    msg.data[3] = 0xc1;
    msg.data[4] = (0xff & (*ptr >> 8));
    msg.data[5] = (0xff & *ptr);
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //rotation i
    ptr = (unsigned int *)&(i_val);

    clearMsg();
    msg.length = 8;
    msg.data[0] = this->controller_Address;
    msg.data[1] = 0x06;
    msg.data[2] = 0x00;
    msg.data[3] = 0xc2;
    msg.data[4] = (0xff & (*ptr >> 24));
    msg.data[5] = (0xff & (*ptr >> 16));
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    clearMsg();
    msg.length = 8;
    msg.data[0] = this->controller_Address;
    msg.data[1] = 0x06;
    msg.data[2] = 0x00;
    msg.data[3] = 0xc3;
    msg.data[4] = (0xff & (*ptr >> 8));
    msg.data[5] = (0xff & *ptr);
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    //rotation d
    ptr = (unsigned int *)&(d_val);

    clearMsg();
    msg.length = 8;
    msg.data[0] = this->controller_Address;
    msg.data[1] = 0x06;
    msg.data[2] = 0x00;
    msg.data[3] = 0xc4;
    msg.data[4] = (0xff & (*ptr >> 24));
    msg.data[5] = (0xff & (*ptr >> 16));
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);

    clearMsg();
    msg.length = 8;
    msg.data[0] = this->controller_Address;
    msg.data[1] = 0x06;
    msg.data[2] = 0x00;
    msg.data[3] = 0xc5;
    msg.data[4] = (0xff & (*ptr >> 8));
    msg.data[5] = (0xff & *ptr);
    CRC16Generate(&msg);
    transmitData(&msg);
    receiveData(&msg);        
    
    return;
}

void wheel::stop(){

    if(this->controller_Address == 0){
        return;
    }

    clearMsg();

    this->msg.length = 8;
    this->msg.data[0] = controller_Address;
    this->msg.data[1] = 0x06;
    this->msg.data[3] = 0x40;
    this->msg.data[5] = 0x01;

    CRC16Generate(&this->msg);
    transmitData(&this->msg);
    receiveData(&this->msg);

    this->last_target_speed = this->target_speed;
    this->target_speed = 0;
    //std::cout << "wheel : " << (int)this->controller_Address << " stop()" << std::endl;
    return;
}

void wheel::freeStop(){

    if(this->controller_Address == 0){
        return;
    }

    clearMsg();

    this->msg.length = 8;
    this->msg.data[0] = controller_Address;
    this->msg.data[1] = 0x06;
    this->msg.data[3] = 0x40;
    this->msg.data[5] = 0x02;

    CRC16Generate(&this->msg);
    transmitData(&this->msg);
    receiveData(&this->msg);

    this->last_target_speed = this->target_speed;
    this->target_speed = 0;

    return;
}

void wheel::getRpm(){
     
    clearMsg();
    this->msg.length = 8;
    this->msg.data[0] = this->controller_Address;
    this->msg.data[1] = 0x03;

    this->msg.data[2] = 0x00;
    this->msg.data[3] = 0x34;

    this->msg.data[4] = 0x00;
    this->msg.data[5] = 0x02;

    CRC16Generate(&this->msg);
    transmitData(&this->msg);
    receiveData(&this->msg);

    if(this->msg.length >= 9){
        int rpm_local = 0;
        rpm_local |= this->msg.data[3];
        rpm_local = (rpm_local << 8);
        rpm_local |= this->msg.data[4];

        if(this->msg.data[6]){
            rpm_local = rpm_local * 10;
        }

        if(this->target_speed < 0){
            rpm_local = -1*rpm_local;
        }
        else if(this->target_speed == 0 && this->last_target_speed < 0){
            rpm_local = -1*rpm_local;
        }

        this->current_rpm = rpm_local;

        std::cout << "wheel " << (int)this->controller_Address << " rpm " << rpm_local << std::endl;

        rpm_local = 0;
    }
    else{
        ROS_INFO("wheel_%d reading rpm error\n", this->controller_Address);
    }

    return;
}

int wheel::output_rpm(){

    return this->current_rpm;
}

int wheel::output_target(){

    return this->target_speed;
}

void wheel::clearMsg(){

    for(int i = 0; i < 20; i++){
        this->msg.data[i] = 0;
    }

    this->msg.length = 0;
    
    return;
}