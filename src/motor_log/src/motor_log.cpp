#include <ros/ros.h>
#include <string>
#include <fstream>
#include <iomanip>
#include <unistd.h>
#include <pwd.h>
#include <chrono>
#include <motor_communicate/motor_info.h>

std::fstream output_file;
ros::Time start_point;

void log_callback(const motor_communicate::motor_info::ConstPtr &data);

int main(int argc, char **argv){

    ros::init(argc, argv, "motor_log");
    ros::NodeHandle rosNh;
    
    std::string output_file_path;

    uid_t userid;
    struct passwd *pwd;

    time_t start;
    tm *start_struct;

    std::chrono::system_clock::time_point start_stamp = std::chrono::system_clock::now();
    start = std::chrono::system_clock::to_time_t(start_stamp);
    start_struct = std::localtime(&start);

    userid = getuid();
    pwd = getpwuid(userid);
    output_file_path.append(pwd->pw_dir);
    output_file_path.append("/Desktop/motor_log/");
    output_file_path.append(std::to_string(1900 +  start_struct->tm_year));
    output_file_path.append("_");
    output_file_path.append(std::to_string(start_struct->tm_mon + 1));
    output_file_path.append("_");
    output_file_path.append(std::to_string(start_struct->tm_mday));
    output_file_path.append("_");
    output_file_path.append(std::to_string(start_struct->tm_hour));
    output_file_path.append("_");
    output_file_path.append(std::to_string(start_struct->tm_min));
    output_file_path.append("_");
    output_file_path.append(std::to_string(start_struct->tm_sec));
    output_file_path.append("_motor_log.txt");

    output_file.open(output_file_path, std::ios::out | std::ios::app);

    ros::Subscriber sub = rosNh.subscribe("/motor_log", 1000, log_callback);

    start_point = ros::Time::now();

    ros::spin();

    output_file.close();

    return  0;
}

void log_callback(const motor_communicate::motor_info::ConstPtr &data){

    ros::Duration duration = data->head.stamp - start_point;

    std::cout << duration.toSec() << std::endl;
    output_file << duration.toSec() << " // ";
    output_file << "wheel: 1 " << "target: " << data->wheel_1_target << " " << "rpm: " << data->wheel_1_rpm << " ";
    output_file << "wheel: 2 " << "target: " << data->wheel_2_target << " " << "rpm: " << data->wheel_2_rpm << " ";
    output_file << "wheel: 3 " << "target: " << data->wheel_3_target << " " << "rpm: " << data->wheel_3_rpm << " ";
    output_file << "wheel: 4 " << "target: " << data->wheel_4_target << " " << "rpm: " << data->wheel_4_rpm << " ";
    output_file << std::endl;

    return;
}