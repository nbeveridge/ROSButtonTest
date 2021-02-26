#!/usr/bin/env python
import rospy
from std_srvs.srv import SetBool
import RPi.GPIO as GPIO
import time


def gpio_req_callback():
    rospy.wait_for_service('gpio_node_server')
    try:
        gpio_node_server = rospy.ServiceProxy('gpio_node_server', SetBool)
        resp = set_led_state(gpio_node_server)
        print(resp)
    except rospy.ServiceException as e:
        rospy.logerr(e)
        
if __name__ == '__main__':
    rospy.init_node('gpio_node_client')
    
    while(True):
        gpio_req_callback()
        time.sleep(50)

    rospy.spin()
    GPIO.cleanup()