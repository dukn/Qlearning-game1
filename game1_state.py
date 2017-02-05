import numpy
import pygame
import os
from pygame.locals import *
from sys import exit
import random
import pygame.surfarray as surfarray 
import matplotlib.pyplot as plt 

position = 200,300
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
pygame.init()

screen = pygame.display.set_mode((500,500))

# create a bar, a coin and background.
back = pygame.Surface((500,500))
background = back.convert()
background.fill((0,0,0))
abar = pygame.Surface((200,100))
bar = abar.convert()
bar.fill((255,255,255))
acoin = pygame.Surface((100,100))
coin = acoin.convert()
coin.fill((255,255,255))
#font = pygame.font.SysFont("calibri",35)
# definitions
graph = [(0,0)]
class GameState(object):
	"""docstring for GameState"""
	def __init__(self):
		self.bar_x, self.bar_y = 200.,400.
		self.score = 0
		self.out = 0
		self.bar_move = 0.
		self.speed = 100.
		self.coin_x, self.coin_y = 0., 0.

	def gameframe(self,input_vector):
		pygame.event.pump()
		reward = 0

		if sum(input_vector) != 1:
			raise ValueError('Multiple input action!')

		if input_vector[1] == 1: # Left
			self.bar_move = - self.speed
		elif input_vector[2] == 1:
			self.bar_move = self.speed
		else:
			self.bar_move = 0

		screen.blit(background,(0,0))
		screen.blit(coin,(self.coin_x,self.coin_y))
		screen.blit(bar,(self.bar_x,self.bar_y))
		self.bar_x += self.bar_move

		# time 
		self.coin_y += 50.
		# RULES
		# for bar
		if self.bar_x <= 0.:
			self.bar_x = 0.
		if self.bar_x >= 300.:
			self.bar_x = 300

		# for coin
		if self.coin_y >= 400.:
			if self.coin_x >= self.bar_x and self.coin_x <= self.bar_x + 100: # win
				self.score += 1
				reward = 1
			else:
				self.out += 1
				reward = -1
			self.coin_x, self.coin_y = random.randint(0,4)*100 ,0.
		print "(score:penalty) : ( {} : {} )".format(self.score, self.out)
		graph.append((self.score,self.out))

		image_data = pygame.surfarray.array3d(pygame.display.get_surface())
		pygame.display.update()
		
		return image_data, reward , graph
