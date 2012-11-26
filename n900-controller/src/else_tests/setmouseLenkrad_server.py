'''
Created on 12.03.2011

@author: fecub
'''

from Xlib import X, display
import socket, sys


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
		
		#print x
		y-=400
		y*=-1
		
		
		d = display.Display()
		screen = d.screen()
		root = screen.root
		root.warp_pointer(y,300)
		d.sync()

finally:
	s.close()
	
	
	
