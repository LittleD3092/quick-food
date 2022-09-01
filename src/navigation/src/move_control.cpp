/*
	linear unit = centimeter
	velicity unit = m/s
	rotation unit = degrees

        initial head direction = 180 degree 

        subscribe geometry_msgs pose from /slam_out_pose(hector-slam) as a basis for robot's attitude.
	lidar model : velodyne vlp-16 (motor speed = 1200rpm)
	to client:
		subscribe geometry_msgs pose from main_control. 
		if the move is completed send done to client & watting for the next command from main_control.
		
	to controller:
		[1][2][3][4]:

		[1]direction
			0 = rotation mode & 1 = X-direction & 2 = Y-direction
		[2]velocity
			velocity( + or - )     0 : stop      1 : minimum velocity   2 : medium velocity   3 : maximum velocity
		
		[3]rotation
			0 = do nothing & 1 = cw  & 2 = ccw

        [4]head_direction
            imform controller of the current nose orientation
            0, 90, 180, 270, 

v1: 
        complete basic operating functions.

v2:
        fixed a stray issue caused by machine rotation.

*/

#include<ros/ros.h>
#include<bits/stdc++.h>
#include<stdlib.h>
#include<stdint.h>
#include<vector>

#include<geometry_msgs/PoseStamped.h>
#include <sensor_msgs/LaserScan.h>
#include<std_msgs/Int16MultiArray.h>
#include"nav/Service_msg.h"
#include"nav/main2nav.h"

//demo
__int16_t target[3] = {0, 0, 180};

//error
int point_error = 3;
int rotate_error = 2;

int distence_to_target_max = 50;
int distence_to_target_min = 30;

int set_vel_max = 3;
int set_vel_med = 2;
int set_vel_min = 1; 
int set_vel_stop = 0;

//robot data
float robot_now_point_x = 0;
float robot_now_point_y = 0;
int robot_now_vel = 0;
int robot_now_pose = 0;
int temp_pose = 0;

//flag
bool state_flag = false;
bool done_flag = false;

//else
float quat_z = 0;
float eular_z = 0;
std::vector<int16_t> controller_msg{5, 5, 5,180};

void MySigintHandler(int sig);
void SLAM_POSE_Callback(const geometry_msgs::PoseStamped::ConstPtr &msg);
bool Srv_Callback(nav::main2nav::Request &req, nav::main2nav::Response &res);

float qua2eular(float); //only for z-axis rotation
void check_attitude(); 
void move_plan_x(int ,int, int);
void move_plan_y(int ,int, int);
void move_plan_r(int ,int, int);
void final_check(int, int, int);
void set_vel(int);

sensor_msgs::LaserScan scan_msg;

int main(int argc, char** argv){

	ros::init(argc, argv,"qua2eular");
	ros::NodeHandle n;

	ros::Subscriber sub = n.subscribe("/slam_out_pose", 100, SLAM_POSE_Callback);
	ros::ServiceClient client = n.serviceClient<nav::Service_msg>("controller_command",100);
	ros::ServiceServer service = n.advertiseService("main2nav",Srv_Callback);

	nav::Service_msg srv_command;

	signal(SIGINT, MySigintHandler);
	while(ros::ok()){

		while(done_flag == false){
			while(state_flag == false){
				move_plan_x(target[0], target[1], target[2]);

				srv_command.request.direction = controller_msg[0];
				srv_command.request.velocity = controller_msg[1];
				srv_command.request.rotation = controller_msg[2];
                srv_command.request.head_direction = controller_msg[3];

				if(client.call(srv_command)){
						ROS_INFO("connect success");
				}else{
						ROS_INFO("connect fail");
				}

				ros::spinOnce();

			}
			state_flag = false;

			while(state_flag == false){
				move_plan_y(target[0], target[1], target[2]);

				srv_command.request.direction = controller_msg[0];
				srv_command.request.velocity = controller_msg[1];
				srv_command.request.rotation = controller_msg[2];
                srv_command.request.head_direction = controller_msg[3];

				if(client.call(srv_command)){
						ROS_INFO("connect success");
				}else{
						ROS_INFO("connect fail");
				}

				ros::spinOnce();

			}
			state_flag = false;

			while(state_flag == false){
				move_plan_r(target[0], target[1], target[2]);

				srv_command.request.direction = controller_msg[0];
				srv_command.request.velocity = controller_msg[1];
				srv_command.request.rotation = controller_msg[2];

				if(client.call(srv_command)){
						ROS_INFO("connect success");
				}else{
						ROS_INFO("connect fail");
				}

				ros::spinOnce();

			}
			state_flag = false;

			final_check(target[0], target[1], target[2]);

		}
			
		ros::spinOnce();

	}

	return 0;
}   

// This function is a call back function for the subscriber.
// Precondition: msg is a geometry message of other node
// Postcondition: robot_now_point_x, robot_now_point_y, quat_z are updated
void SLAM_POSE_Callback(const geometry_msgs::PoseStamped::ConstPtr& msg){
	quat_z = msg -> pose.orientation.z;
	robot_now_point_y = (msg -> pose.position.x*-100);
	robot_now_point_x = (msg -> pose.position.y*-100);
	//due to the 90 degree deflection of the mounting direction of vlp-16 

}

// This function is a call back function for the service server. 
// main_control node will be the client.
// Precondition: req is a service request of other node, res can be anything
// Postcondition: global variable target is updated. If the done_flag is true, return true.
bool Srv_Callback(nav::main2nav::Request& req, nav::main2nav::Response& res){

	target[0] = req.main_x;
	target[1] = req.main_y;
	target[2] = req.rotation;

	if(done_flag == true){
		return true;

	}else{
		return false;

	}
		
}

// This function calculate the pose from the quaternion quat_z.
// Precondition: quat_z is the z-axis rotation of the robot
// Postcondition: pose is the z-axis rotation of the robot
float qua2eular(float quat_z){
	int pose = (2*acos(quat_z))*180/3.1415;

	return pose;
}

// This function is to check the attitude of the robot.
// Precondition: global variable robot_now_pose and controller_msg are updated
// Postcondition: global variable controller_msg is updated
void check_attitude(){
	int pose_error = 0;

	if(robot_now_pose >= 135 && robot_now_pose < 225){  
		pose_error = robot_now_pose - 180;
                controller_msg[3] = 180;

	}else if(robot_now_pose >= 225 && robot_now_pose < 315 ){ 
		pose_error = robot_now_pose - 270;
                controller_msg[3] = 270;

	}else if(robot_now_pose >= 45 && robot_now_pose < 135 ){ 
		pose_error = robot_now_pose - 90;
                controller_msg[3] = 90;

	}else{
		pose_error = robot_now_pose - 0; 
                controller_msg[3] = 0;
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

// This function is to plan the move position of x axis.
// Precondition: set_point_x, set_point_y, set_pose is the target position's x, y and rotation angle.
//               global variable point_error, robot_now_point_x, controller_msg, robot_now_pose, state_flag is present.
// Postcondition: global variable robot_now_pose, controller_msg, state_flag is updated.
//                If the robot is not in the target position, function set_vel() is called.
void move_plan_x(int set_point_x, int set_point_y, int set_pose){
	int error_low_x = set_point_x - point_error;
	int error_high_x = set_point_x + point_error; 
	int dis_to_setpoint = set_point_x - robot_now_point_x;
	controller_msg[0] = 1;

	robot_now_pose = qua2eular(quat_z);

	if (robot_now_point_x > error_low_x && robot_now_point_x < error_high_x){        //reached
		//done
		state_flag = true;
		controller_msg[1] = set_vel_stop;

	}else{                                                                                                                                        //not reached
		if(dis_to_setpoint > 0 ){
			std::cout << " move forward               ";
			check_attitude();
			set_vel(dis_to_setpoint);

		}else{
			std::cout << " move backward           ";
			check_attitude();
			set_vel(dis_to_setpoint);

		}
	}
		
}

// This function is to plan the move position of y axis.
// Precondition: set_point_x, set_point_y, set_pose is the target position's x, y and rotation angle.
//               global variable point_error, robot_now_point_y, controller_msg, robot_now_pose, state_flag is present.
// Postcondition: global variable robot_now_pose, controller_msg, state_flag is updated.
//                If the robot is not in the target position, function set_vel() is called.
void move_plan_y(int set_point_x, int set_point_y, int set_pose){
	int error_low_y =set_point_y - point_error;
	int error_high_y = set_point_y + point_error; 
	int dis_to_setpoint = set_point_y - robot_now_point_y;
	controller_msg [0] = 2;

	robot_now_pose = qua2eular(quat_z);

	if (robot_now_point_y > error_low_y && robot_now_point_y < error_high_y){        //reached
		//done
		state_flag = true;
		controller_msg[1] = set_vel_stop;

	}else{                                                                           //not reached
		if(dis_to_setpoint > 0 ){
			std::cout << " move right                ";
			check_attitude();
			set_vel(dis_to_setpoint);

		}else{
			std::cout << " move left                    ";
			check_attitude();
			set_vel(dis_to_setpoint);

		}
	}
				
}

// This function is to plan the move position of rotation angle.
// Precondition: set_point_x, set_point_y, set_pose is the target position's x, y and rotation angle.
//               global variable point_error, robot_now_pose, controller_msg, state_flag is present.
// Postcondition: global variable robot_now_pose, controller_msg, state_flag is updated.
//                If the robot is not in the target position, controller_msg is updated.
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
		std::cout << " plan_r_turn_ccw"<<std::endl;
		controller_msg[2] = 2;
		controller_msg[1] = 1;

	}else{
		std::cout << " plan_r_turn_cw  "<<std::endl;
		controller_msg[2] = 1;
		controller_msg[1] = 1;
	}

}

// This function is for checking whether the robot is in the target position.
// Precondition: set_point_x, set_point_y, set_pose is the target position's x, y and rotation angle.
//               global variable point_error, robot_now_point_x, and robot_now_point_y is present.
// Postcondition: done_flag is updated according to the result.
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

// This function is to set the velocity of the robot.
// Precondition: distance_to_target is the distance to the target position.
//               global variable distance_to_target_max, distance_to_target_min, 
//               set_vel_max, set_vel_med, set_vel_min, set_vel_stop is present.
// Postcondition: global variable controller_msg is updated according to the result.
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

// This function is for shutting down the node.
// Precondition: sig can be any signal.
// Postcondition: node is shut down. The program is terminated.
void MySigintHandler(int sig){
	ROS_INFO("shutting down!");
	ros::shutdown();
	exit(0);

}

//----v1----2022/8/10----tingweiou----nycu dme
//----v2----2022/8/20----tingweiou----nycu dme
