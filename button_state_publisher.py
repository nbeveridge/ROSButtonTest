#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
BUTTON_GPIO = 16
if __name__ == '__main__':
    rospy.init_node('button_state_publisher')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.cleanup()