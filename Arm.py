#!/usr/bin/python

from Libraries.Adafruit_PWM_Servo_Driver import PWM
BasePin = 0
ShoulderPin = 1
ElbowPin = 2


class Arm(object):
	""" Arm """
	def __init__(self, debug = False):
		self.controller = PWM(0x40, debug)
		self.controller.setPWMFreq(60)					# Set frequency to 60 Hz
		
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


	def setBase(self, value):
		self.controller.setPWM(self.base, 0, value)

	def setShoulder(self, value):
		self.controller.setPWM(self.shoulder, 0, value)

	def setElbow(self, value):
		self.controller.setPWM(self.elbow, 0, value)


