#!/usr/bin/env python

'''
Copyright (c) 2015, Mark Silliman
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

# A very basic TurtleBot script that moves TurtleBot forward indefinitely. Press CTRL + C to stop.  To run:
# On TurtleBot:
# roslaunch turtlebot_bringup minimal.launch
# On work station:
# python goforward.py

import math
import rospy
from geometry_msgs.msg import Twist
import time

def change_vel(linear, angular):
    msg = Twist()
    msg.linear.x = linear
    msg.angular.z = angular
    return msg

def runnode():
    # initiliaze
    rospy.init_node('GoForward', anonymous=False)

    rospy.loginfo('Turtlebot, make a square!')

    # Create a publisher which can "talk" to TurtleBot and tell it to move
    # Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2    
    pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)


    #TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
    r = rospy.Rate(10)

    # as long as you haven't ctrl + c keeping doing...
    try:
        while not rospy.is_shutdown():
            t1 = rospy.Time.now().to_sec()
            # Move forward
            move_cmd = change_vel(0.2,0)
            while rospy.Time.now().to_sec()-t1 < 2:
                pub.publish(move_cmd)
                r.sleep()
            
            # Turn left
            move_cmd = change_vel(0,math.pi/2)
            t1 = rospy.Time.now().to_sec()
            while rospy.Time.now().to_sec()-t1 < 1:
                pub.publish(move_cmd)
                r.sleep()
    except KeyboardInterrupt:
        rospy.loginfo('Ded.')
        pub.publish(Twist())

# int main(void){
if __name__ == '__main__':
    runnode()