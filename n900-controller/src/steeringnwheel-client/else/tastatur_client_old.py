'''
Created on 25.11.2010

@author: fecub
'''

import socket, pygame,  sys
from pygame.locals import *


pygame.init()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#ip = raw_input("IP-adresse: ")
#ip='1.1.1.5'
#ip = '192.168.2.14'
#ip = '10.12.41.175'
ip = sys.argv[1]


hoch = '111'
runter ='116'

running = True
resolution = (800,480)
bgcolor = (255,0,0)
#timer = pygame.time.Clock()
 
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Lenkrad")
#pygame.display.toggle_fullscreen()
 
while running:
	#timer.tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		elif event.type == KEYDOWN:
			if event.key == K_RETURN:
				s.close()
				running = False

	gedruckteTasten = pygame.key.get_pressed()
	
	if ( gedruckteTasten[K_y]): 
		taste = hoch
		s.sendto(taste, (ip, 49999))
	elif ( gedruckteTasten[K_a]):
		taste = runter
		s.sendto(taste, (ip, 49999))
	else:
		s.sendto('ende', (ip, 49999))
		
	 
 
	screen.fill(bgcolor)
	pygame.display.flip()


