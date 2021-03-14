#!/usr/bin/env python


# motor node creates an object of type motor when the node is first run

# then constantly listens for messages to inflate or deflate

# recieves messages from a controller

#USE PARAMS FOR GPIO PINS,MAXSTEPS, AND MAYBE START LOCATION?







import rospy
from std_msgs.msg import Bool
# import RPi.GPIO as GPIO


#####################           remember to uncomment all the rpi gpio stuff


class stepper:
        def __init__(self,StepPins,maxSteps=3000,location = 0):

                ##################################################################
                # GPIO.setmode(GPIO.BCM)
 
                # for pin in StepPins:
                #         print("Setup pins")
                #         GPIO.setup(pin,GPIO.OUT)
                #         GPIO.output(pin, False)
                ##################################################################


                self.maxSteps = maxSteps
                self.location = location
                self.StepPins = StepPins

        ##################################################################
        # def moveToLoc (self, location):
        #         self.move(location-self.location)


        # def move (self,steps):

        #         StepPins = self.StepPins

        #         # Define simple sequence
        #         StepCount1 = 4
        #         Seq1 = []
        #         Seq1 = [i for i in range(0, StepCount1)]
        #         Seq1[0] = [1,0,0,0]
        #         Seq1[1] = [0,1,0,0]
        #         Seq1[2] = [0,0,1,0]
        #         Seq1[3] = [0,0,0,1]

        #         # Choose a sequence to use
        #         Seq = Seq1
        #         StepCount = StepCount1

        #         nb = steps

        #         StepCounter = 0
        #         if nb<0: sign=-1
        #         else: sign=1
        #         nb=sign*nb #times 2 because half-step
        #         #print("nbsteps {} and sign {}".format(nb,sign))
        #         for i in range(nb):
        #                 for pin in range(4):
        #                         xpin = StepPins[pin]
        #                         if Seq[StepCounter][pin]!=0:
        #                                 GPIO.output(xpin, True)
        #                         else:
        #                                 GPIO.output(xpin, False)
        #                 StepCounter += sign
        #         # If we reach the end of the sequence
        #         # start again
        #                 if (StepCounter==StepCount):
        #                         StepCounter = 0
        #                 if (StepCounter<0):
        #                         StepCounter = StepCount-1

        #         for pin in StepPins:
        #                 GPIO.output(pin, False)
        ##################################################################


class balloon:
        def __init__(self,StepPins,maxSteps=3000,startLocation = 0):
                self.maxSteps = maxSteps
                self.StepPins = StepPins
                self.startLocation = startLocation 

                self.stepper = stepper(self.StepPins,self.maxSteps,self.startLocation)  
                

                rospy.init_node('distal_balloon_node_sub')

                rospy.Subscriber('distal_balloon_node_pub', Bool, self.test_callback,queue_size=1)


        def test_callback(self,msg):
                pins = str(self.StepPins)
                typePins = type(self.StepPins)
                if msg.data == True:
                        rospy.loginfo(rospy.get_caller_id() + 'Forward %s %s', pins, typePins)
                else:
                        rospy.loginfo(rospy.get_caller_id() + 'Backward %s %s', pins, typePins)


        ##################################################################
        # def inflate_deflate(self,steps):
        #         self.stepper.move(steps)
        #         self.location = self.location+steps



        # def balloon_callback(msg):
        #         if msg.data == True:
        #                 self.inflate_deflate(1)
        #         else:
        #                 self.inflate_deflate(-1)
        ##################################################################




if __name__ == '__main__':
        StepPins = rospy.get_param("distal_stepper_gpio_pins")

        balloon = balloon(StepPins)
        rospy.spin()

        ##################################################################
        # GPIO.cleanup()
        ##################################################################