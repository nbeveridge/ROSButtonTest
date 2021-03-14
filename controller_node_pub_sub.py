#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Int64
from std_msgs.msg import String
import random
class controller:

    def __init__(self):
        #####   INITIALIZE CONTROLLER NODE
        rospy.init_node('controller_node_pub_sub')
        rate = rospy.Rate(10) # 10hz

        #####   INITIALIZE SENSORS, BALLOONS, AND BUTTONS

        #   SENSORS # CONTROLLER SUBS
        distal_sensor = distal_balloon_sensor()
       
        #   BALLOONS # CONTROLLER PUBS
        distal_balloon = distal_balloon_control()

        #   BUTTONS # CONTROLLER SUBS
        user = user_command()


        while not rospy.is_shutdown():

            #####   RUN SENSORS, BALLOONS, AND BUTTONS
            distal_sensor.distal_balloon_sensor_sub()

            distal_balloon.distal_balloon_control_pub()

            user.user_command_sub()

            rate.sleep()          

class user_command:
    def user_command_sub(self):
        rospy.Subscriber('user_command_node_pub', String, self.user_command_test_callback,queue_size=1)

    def user_command_test_callback(self,msg):
        rospy.loginfo("Key Pressed Is %s", str(msg.data))

class distal_balloon_control:
    def __init__(self):
        self.pub = rospy.Publisher('distal_balloon_node_pub', Bool, queue_size=1)


    def distal_balloon_control_pub(self):
        pub_state = random.choice([True, False])
        self.pub.publish(pub_state)


class distal_balloon_sensor:
   
    def distal_balloon_sensor_sub(self):
        rospy.Subscriber('distal_balloon_sensor_node_pub', Int64, self.sensor_test_callback,queue_size=1)

    def sensor_test_callback(self,msg):
        rospy.loginfo("Sensor Data Is %s", str(msg.data))





if __name__ == '__main__':
    try:
        controller = controller()
    except rospy.ROSInterruptException:
        pass