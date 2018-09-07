#include "ros/ros.h"
#include <geometry_msgs/Twist.h>


/**
 * This tutorial demonstrates the use of timer callbacks.
 */

void callback1(const ros::TimerEvent&)
{
  ROS_INFO("Callback 1 triggered");
}

void callback2(const ros::TimerEvent&)
{
  ROS_INFO("Callback 2 triggered");
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "Turtlebot_cmd");
  ros::NodeHandle turtlebot_node_handler;
  ros::Publisher turtlebot_move_cmd_pub;
  
  geometry_msgs::Twist base_cmd;

  turtlebot_move_cmd_pub = turtlebot_node_handler.advertise<geometry_msgs::Twist>("cmd_vel_mux/input/navi", 1);

  ros::Rate r(1); // 10 hz
  while (ros::ok())
  {
    base_cmd.linear.x = 0.25;
    turtlebot_move_cmd_pub.publish(base_cmd);
    r.sleep();
  }
  

  
  
  // /**
  //  * Timers allow you to get a callback at a specified rate.  Here we create
  //  * two timers at different rates as a demonstration.
  //  */
  // ros::Timer timer1 = n.createTimer(ros::Duration(0.1), callback1);
  // ros::Timer timer2 = n.createTimer(ros::Duration(1.0), callback2);
  
  // ros::spin();
  
  return 0;
}