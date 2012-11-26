'''
Created on 25.11.2010

@author: fecub
'''
import socket 
import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 800, 480
black = 0, 0, 0
button1 = pygame.image.load("images/1.jpg")
screen = pygame.display.set_mode(size)
screen.fill(black)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
pygame.init()

size = width, height = 800, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)
screen.fill(black)

screen.blit(button1, (0,0))
pygame.display.flip()
try:
	s.bind(("", 50000))
	x1 = 0
	y1 = 0
	while True:
		daten, addr = s.recvfrom(1024)
		
		coord = daten
		coord=coord.split(',')
		x = int(coord[1])
		y = int(coord[0])
		
		x1 = (x1 - x)
		y1 = (y1 - x)
		
		print x1
		print y1
		if (x1 > 10 and y1 > 15 or x1 < -10 and y1 < -15):
			screen.fill(black)
			screen.blit(button1, (x, y ))
			pygame.display.flip()
			x1 = x
			y1 = y
		else:
			x1 = x
			y1 = y
		
		
		
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
				sys.exit()
			 elif event.type == KEYDOWN and event.key == K_ESCAPE:
					sys.exit()

finally:
	s.close()
	
	
	