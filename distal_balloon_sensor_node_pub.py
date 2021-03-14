#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

from datetime import datetime
import time



class sensor:
        def __init__(self,SensorPins):
            self.SensorPins = SensorPins                

            pub = rospy.Publisher('distal_balloon_sensor_node_pub', Int64, queue_size=1)
            rospy.init_node('distal_balloon_sensor_node_pub', anonymous=True)
            rate = rospy.Rate(10) # 10hz
            while not rospy.is_shutdown():
                pub_state = self.read_sensor_test()
                pub.publish(pub_state)
                rate.sleep()

        def read_sensor_test(self):
            pins = str(self.SensorPins[0])
            now = str(round(time.time() * 1000))
            ret = int(pins+pins+pins+pins+now)
            return ret

            


if __name__ == '__main__':
    SensorPins = rospy.get_param("distal_sensor_gpio_pins")
    try:
        sensor = sensor(SensorPins)
    except rospy.ROSInterruptException:
        pass