
'''
Created on 12.03.2011

@author: fecub
'''

import Xlib.display
import Xlib.X
import Xlib.XK
import Xlib.protocol.event
import Xlib.ext.xtest
import socket, sys


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
keycode = None
try:
	s.bind(("", 49999))
	i=0
	display = Xlib.display.Display()
	
	while True:
		daten, addr = s.recvfrom(1024)
		if (daten != 'ende'):
			keycode = daten
		if keycode == '111' or keycode == '116':
			print '%d up/down' % i
			Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, int(keycode) )
			display.sync()
		if keycode == '117':
			# A
			Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, int(keycode) )
			display.sync()
		if keycode == '118':
			# Y
			Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, int(keycode) )
			display.sync()
		if keycode == '119':
			# SPACE
			Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, int(keycode) )
			display.sync()
		if daten == 'ende':
			if keycode != None:
				Xlib.ext.xtest.fake_input(display, Xlib.X.KeyRelease, int(keycode) )
				keycode = None
				display.sync()
			daten = None
			continue

finally:
	s.close()
