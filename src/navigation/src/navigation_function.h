/*

#include<ros/ros.h>
#include<bits/stdc++.h>
#include<stdlib.h>
#include<stdint.h>
#include<vector>

#include<geometry_msgs/PoseStamped.h>
#include<std_msgs/Int16MultiArray.h>

float robot_now_point_x ;
float robot_now_point_y ;
int robot_now_vel ;
int robot_now_pose ;
int temp_pose ;

void SLAM_POSE_Callback(const geometry_msgs::PoseStamped::ConstPtr&msg){
        quat_z = msg -> pose.orientation.z;
        robot_now_point_x = msg -> pose.position.x;
        robot_now_point_x = robot_now_point_x*100;
        robot_now_point_y = msg -> pose.position.y;
        robot_now_point_y = robot_now_point_y*100;

}

float qua2eular(float quat_z){
        int pose = (2*acos(quat_z))*180/3.1415;

        return pose;
}

void check_attitude(int temp_pose){
        int pose_error = 0;

        if(robot_now_pose > 150 && robot_now_pose < 210){
                pose_error = robot_now_pose - 180;

        }else if(robot_now_pose > 240 && robot_now_pose < 300 ){
                pose_error = robot_now_pose - 270;

        }else if(robot_now_pose > 60 && robot_now_pose < 120 ){
                pose_error = robot_now_pose - 90;

        }else{
                pose_error = robot_now_pose - 0;
        }

        if(pose_error > 0){
                //turn left
                std::cout << " turn_ccw "<<std::endl;
                controller_msg[2] = 2;

        }else if(pose_error < 0){
                //turn right
                std::cout << " turn_cw"<<std::endl;
                controller_msg[2] = 1;

        }else{
                //do nothing
               std::cout<<" go straight"<<std::endl;
               controller_msg[2] = 0;

        }

}

void move_plan_x(int set_point_x, int set_point_y, int set_pose){
        int error_low_x =set_point_x - point_error;
        int error_high_x = set_point_x + point_error; 
        int dis_to_setpoint = set_point_x - robot_now_point_x;
        controller_msg[0] = 1;

        robot_now_pose = qua2eular(quat_z);

        if (robot_now_point_x > error_low_x && robot_now_point_x < error_high_x){        //reached
                //done
                state_flag = true;
                set_vel(dis_to_setpoint);

        }else{                                                                                                                                        //not reached
                if(dis_to_setpoint > 0 ){
                        std::cout << " move forward               ";
                        check_attitude(temp_pose);
                        set_vel(dis_to_setpoint);

                }else{
                        std::cout << " move backward           ";
                        check_attitude(temp_pose);
                        set_vel(dis_to_setpoint);

                        }
        }
        
}

void move_plan_y(int set_point_x, int set_point_y, int set_pose){
        int error_low_y =set_point_y - point_error;
        int error_high_y = set_point_y + point_error; 
        int dis_to_setpoint = set_point_y - robot_now_point_y;
        controller_msg [0] = 1;

        robot_now_pose = qua2eular(quat_z);

        if (robot_now_point_y > error_low_y && robot_now_point_y < error_high_y){        //reached
                //done
                state_flag = true;
                set_vel(dis_to_setpoint);

        }else{                                                                                                                                        //not reached
                if(dis_to_setpoint > 0 ){
                        std::cout << " move left                ";
                        check_attitude(temp_pose);
                        set_vel(dis_to_setpoint);

                }else{
                        std::cout << " move right                    ";
                        check_attitude(temp_pose);
                        set_vel(dis_to_setpoint);

                        }
                }
                
}

void move_plan_r(int set_point_x, int set_point_y, int set_pose){
        int error_low_r = 0 - rotate_error;
        int error_high_r = 0 + rotate_error;

        robot_now_pose = qua2eular(quat_z);

        int deg_to_set_pose = robot_now_pose - set_pose;
        controller_msg [0] = 0;

        if(deg_to_set_pose > error_low_r && deg_to_set_pose < error_high_r){
                state_flag = true;
                controller_msg[2] = 0;
                controller_msg[1] = 0;

        }else if(deg_to_set_pose > 0 ){
                std::cout << " turn_ccw"<<std::endl;
                controller_msg[2] = 2;
                controller_msg[1] = 1;

        }else{
                std::cout << " turn_cw  "<<std::endl;
                controller_msg[2] = 1;
                controller_msg[1] = 1;
        }

}

void final_check(int set_point_x, int set_point_y, int set_pose){
        int error_low_x =set_point_x - point_error;
        int error_high_x = set_point_x + point_error; 
        int error_low_y =set_point_y - point_error;
        int error_high_y = set_point_y + point_error;

        if(robot_now_point_x > error_low_x && robot_now_point_x < error_high_x && robot_now_point_y > error_low_y && robot_now_point_y < error_high_y){
                done_flag = true;
        }else{
                done_flag = false;
        }
        
}

void set_vel(int distance_to_target){

        if(distance_to_target > 0){
                if(distance_to_target >= distence_to_target_max){
                        controller_msg[1] = set_vel_max;

                }else if(distance_to_target > distence_to_target_min && distance_to_target < distence_to_target_max){
                        controller_msg[1] = set_vel_med;

                }else{
                        controller_msg[1] = set_vel_min;

                }

        }else if(distance_to_target < 0){
                if(distance_to_target <= -1*distence_to_target_max){
                        controller_msg[1] = -1*set_vel_max;

                }else if(distance_to_target < -1*distence_to_target_min && distance_to_target > -1*distence_to_target_max){
                        controller_msg[1] = -1*set_vel_med;

                }else{
                        controller_msg[1] = -1*set_vel_min;

                }
        }else{
                controller_msg[1] = set_vel_stop;
                
        }
}

void MySigintHandler(int sig){
	ROS_INFO("shutting down!");
	ros::shutdown();
        exit(0);

}
*/