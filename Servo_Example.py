#!/usr/bin/python

from Arm import Arm 
import time

# ===========================================================================
# Test
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = Arm(debug=False)
Arm = Arm()

SERVO_MIN 		= 150  # Min pulse length out of 4096
SERVO_MAX 		= 650  # Max pulse length out of 4096
SERVO_CENTER	= 375  # Center value for the servo, should be 0 degrees of rotation.


while (True):

	Arm.setBase(0)
	time.sleep(1)


	Arm.setBase(90)
	time.sleep(1)

	Arm.setBase(180)
	time.sleep(1)



