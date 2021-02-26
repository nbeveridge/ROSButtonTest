#!/usr/bin/env python

import rospy
from std_srvs.srv import SetBool
import RPi.GPIO as GPIO

proximal_stepper_gpio = [1,2,3,4]
distal_stepper_gpio = [5,6,7,8]
proximal_locomotion_stepper_gpio = [9,10,11,12]
distal_locomotion_stepper_gpio = [13,14,15,16]


def gpio_callback(req):

    return { 'success': True,
            'proximal_stepper_gpio': '[1,2,3,4]',
            'distal_stepper_gpio': [5,6,7,8],
            'proximal_locomotion_stepper_gpio':[9,10,11,12],
            'distal_locomotion_stepper_gpio':[13,14,15,16]
            }

if __name__ == '__main__':
    rospy.init_node('gpio_node_server')#initialize the node

    rospy.Service('return_gpio_pins', SetBool, gpio_callback)
    rospy.loginfo("Service server started. Ready to get requests.")

    rospy.spin()

    GPIO.cleanup()