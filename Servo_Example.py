#!/usr/bin/python

from Arm import Arm 
import time

# ===========================================================================
# Test
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = Arm(debug=False)
Arm = Arm()

SERVO_MIN = 150  # Min pulse length out of 4096
SERVO_MAX = 600  # Max pulse length out of 4096
SERVO_CENTER		= 400		# Center value for the servo, should be 0 degrees of rotation.


while (True):
  # Change speed of continuous servo on channel O

  Arm.setBase(SERVO_CENTER)
  Arm.setShoulder(SERVO_MIN)
  Arm.setElbow(SERVO_MIN)

  time.sleep(1)

  Arm.setBase(SERVO_MAX)
  Arm.setShoulder(SERVO_MAX)
  Arm.setElbow(SERVO_MAX)

  time.sleep(1)



