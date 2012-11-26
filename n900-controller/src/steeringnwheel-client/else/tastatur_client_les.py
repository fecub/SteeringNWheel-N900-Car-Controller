'''
Created on 25.11.2010

@author: fecub
'''
import socket, pygame, sys, time
from pygame.locals import *


pygame.init()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # -----> accelBrake_server
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # -----> gearshift_server

ip = sys.argv[1]

hoch = '111'
runter ='116'
gangHoch = "117"
gangRunter = "118"
handbremse = "119"

running = True
resolution = (800,480)
bgcolor = (255,0,0)

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Lenkrad")
#pygame.display.toggle_fullscreen()
i=1
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		elif event.type == KEYDOWN:
			if event.key == K_RETURN:
				s.close()
				running = False
	gedruckteTasten2 = pygame.key.get_pressed()
			
	if ( gedruckteTasten2[K_LEFT]):
		taste = gangHoch
		s.sendto(taste, (ip, 49998))
	
	elif ( gedruckteTasten2[K_RIGHT]):
		taste = gangRunter
		s.sendto(taste, (ip, 49998))

	x = i%20
	i=i+1
	if( x == 0):
		gedruckteTasten = pygame.key.get_pressed()
		if ( gedruckteTasten[K_PERIOD]):
			taste = handbremse
			s.sendto(taste, (ip, 49998))

		elif ( gedruckteTasten[K_y]): 
			taste = hoch
			s.sendto(taste, (ip, 49999))
	
		elif ( gedruckteTasten[K_a]):
			taste = runter
			s.sendto(taste, (ip, 49999))
		else:
			s.sendto('ende', (ip, 49999))
			s.sendto('ende', (ip, 49998))
		screen.fill(bgcolor)
		pygame.display.flip()

