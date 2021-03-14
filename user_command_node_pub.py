#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8

from datetime import datetime
import time

# import getch
# import keyboard
# import readkeys

import random


class button:
        def __init__(self,ButtonPins):
            self.ButtonPins = ButtonPins                

            pub = rospy.Publisher('user_command_node_pub', String, queue_size=1)
            rospy.init_node('user_command_node_pub', anonymous=True)
            rate = rospy.Rate(10) # 10hz
            while not rospy.is_shutdown():
                pub_state = self.random_button_test()
                pub.publish(pub_state)
                rate.sleep()


        def random_button_test(self):
            # # key = readkeys.getch()  # get a single character

            # # # key=ord(getch())
            # # # if ((key>=65)&(key<=68)|(key==115)|(key==113)|(key==97)):
            # # # rospy.loginfo(str(key))# to print on  terminal 
            # space = '______________________________________'
            # # return space+str(key)+space


            
            # key = str(keyboard.read_key())
            # return space + key + space

            pub_state = random.choice(['', '','','---------------','','','','','',''])
            return pub_state


if __name__ == '__main__':
    ButtonPins = rospy.get_param("button_gpio_pins")
    try:
        button = button(ButtonPins)
    except rospy.ROSInterruptException:
        pass

