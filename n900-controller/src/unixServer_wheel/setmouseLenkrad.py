'''
Created on 12.03.2011

@author: fecub
'''

from Xlib import display
import socket, time
import math
import subprocess


screen_size = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
screen_size = screen_size.split("x")
screen_size_x = int(screen_size[0])
screen_size_x_half = screen_size_x / 2

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("", 50000))
x1 = 0
y1 = 0

d = display.Display()
screen = d.screen()
root = screen.root

android = True

while True:
	time.sleep(0.1)
	daten, addr = s.recvfrom(1024)
	#print daten
	coord = daten
	coord=coord.split(',')
	
	if (android):
		x = float(coord[1])
		y = float(coord[0])
		pointer = int(math.floor(float(((x/3)*210) + screen_size_x_half)))
	else:
		x = int(coord[1])
		y = int(coord[0])

		pointer = y + screen_size_x_half
	
	print pointer
	root.warp_pointer(pointer,300)
	d.sync()
s.close()