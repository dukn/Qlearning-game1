import pygame
import sys
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,500))

# create a bar, a coin and background
back = pygame.Surface((500,500))
background = back.convert()
background.fill((0,0,0))
abar = pygame.Surface((200,100))
bar = abar.convert()
bar.fill((255,255,255))
acoin = pygame.Surface((100,100))
coin = acoin.convert()
coin.fill((255,255,255))

# definitions
bar_x, bar_y = 200.,400.
score = 0
bar_move = 0.
speed = 100.
clock= pygame.time.Clock()
done = False
coin_x, coin_y = 0., 0.

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				bar_move = - speed
			elif event.key == K_RIGHT:
				bar_move = speed
		elif event.type == KEYUP:
			if event.key == K_RIGHT or event.key == K_LEFT:
				bar_move = 0.
	#
	screen.blit(background,(0,0))
	screen.blit(coin,(coin_x,coin_y))
	screen.blit(bar,(bar_x,bar_y))
	bar_x += bar_move

	# time 
	time_passed = clock.tick(10)
	time_sec = time_passed/1000.0
	coin_y += 50.
	# RULES
	# for bar
	if bar_x <= 0.:
		bar_x = 0.
	if bar_x >= 300.:
		bar_x = 300

	# for coin
	if coin_y >= 400.:
		if coin_x >= bar_x and coin_x <= bar_x + 100: # win
			score += 1
		coin_x, coin_y = random.randint(0,4)*100 ,0.
	print score


	pygame.display.update()

pygame.quit()