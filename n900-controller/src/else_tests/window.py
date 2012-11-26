'''
Created on 28.11.2010

@author: fecub
'''


import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 800, 480
black = 0, 0, 0
screen = pygame.display.set_mode(size)
screen.fill(black)

pygame.init()

screen = pygame.display.set_mode(size)
screen.fill(black)

pygame.display.flip()

x=0
y=0
while True:
	
	x,y = pygame.mouse.get_pos()
	print x
	print y

	for event in pygame.event.get():
		 if event.type == pygame.QUIT:
			sys.exit()
		 elif event.type == KEYDOWN and event.key == K_ESCAPE:
				sys.exit()
