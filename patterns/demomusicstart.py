import random
import cubehelper
import os
import math
import pygame

STARTDELAY = 2.0
END = STARTDELAY + 5.217370

def loadsounds(dirname, namelist):
	sounds = []
	for name in namelist:
		newsound = pygame.mixer.Sound(dirname + name + '.wav')
		sounds.append(newsound)
	return sounds

class Pattern(object):

	def init(self):
		pygame.init()
		pygame.mixer.init( )
		pygame.mixer.set_num_channels(1)
		self.isaac = pygame.mixer.Sound('patterns/isaac.wav')
		self.isaacplayed = False
		self.double_buffer = True
		self.timer = 0.0
		return 1.0 / 20

	def tick(self):
		if self.isaacplayed == False and self.timer > STARTDELAY:
			self.isaac.play()
			self.sleepyplayed = True
		self.timer += 0.05
		if self.timer >= END:
			raise StopIteration

