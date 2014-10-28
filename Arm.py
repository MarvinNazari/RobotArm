#!/usr/bin/python
from math import pi
import time

from Libraries.Adafruit_PWM_Servo_Driver import PWM
BasePin = 0
ShoulderPin = 1
ElbowPin = 2

SERVO_MIN 		= 150  # Min pulse length out of 4096
SERVO_MAX 		= 600  # Max pulse length out of 4096

class Arm(object):
	""" Arm """
	def __init__(self, debug = False):
		self.controller = PWM(0x40, debug)
		self.controller.setPWMFreq(60)			# Set frequency to 60 Hz
		
		# Configuring Servo pins
		self.base = BasePin
		self.shoulder = ShoulderPin
		self.elbow = ElbowPin

		
	def setServoPulse(channel, pulse):
		pulseLength = 1000000                   # 1,000,000 us per second
		pulseLength /= 60                       # 60 Hz
		print "%d us per period" % pulseLength
		pulseLength /= 4096                     # 12 bits of resolution
		print "%d us per bit" % pulseLength
		pulse *= 1000
		pulse /= pulseLength
		self.controller.setPWM(channel, 0, pulse)

	def setPWM(self, channel, on, off):
		self.controller.setPWM(channel, on, off)

	def getDegree(self, x):
		return (x - 0) * (SERVO_MAX - SERVO_MIN) // (180 - 0) + SERVO_MIN

	def setBase(self, angle):
		self.controller.setPWM(self.base, 0, self.getDegree(angle))

	def setShoulder(self, angle):
		self.controller.setPWM(self.shoulder, 0, self.getDegree(angle))

	def setElbow(self, angle):
		self.controller.setPWM(self.elbow, 0, self.getDegree(angle))


